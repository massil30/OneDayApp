#!/usr/bin/env python3
"""
OneDayApp - Build Flutter Apps in One Day
Main workflow orchestrator for generating Flutter applications with LLM assistance.
"""

import os
import sys
import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

from llm_provider import LLMProvider
from app_generator import AppGenerator
from theme_selector import ThemeSelector
from folder_structure import FolderStructureGenerator

console = Console()


class OneDayAppWorkflow:
    """Main workflow orchestrator for OneDayApp."""

    def __init__(self):
        self.llm = LLMProvider()
        self.app_generator = AppGenerator(self.llm)
        self.theme_selector = ThemeSelector()
        self.folder_generator = FolderStructureGenerator()
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)

    def run(self):
        """Run the complete OneDayApp workflow."""
        console.print(Panel.fit(
            "[bold cyan]OneDayApp Workflow[/bold cyan]\n"
            "Build Flutter Apps in One Day with LLM Assistance",
            border_style="cyan"
        ))

        try:
            # Step 1: Generate app idea
            idea = self.generate_idea()
            
            # Step 2: Search for inspiration and define theme
            theme = self.select_theme_and_inspiration()
            
            # Step 3: Generate specification
            spec = self.generate_specification(idea, theme)
            
            # Step 4: Allow user to update specification
            final_spec = self.review_and_update_specification(spec)
            
            # Step 5: Create app folder structure
            folder_structure = self.create_folder_structure(final_spec)
            
            # Step 6: Build the full app
            self.build_application(final_spec, folder_structure)
            
            console.print("\n[bold green]✓ OneDayApp workflow completed successfully![/bold green]")
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Workflow interrupted by user.[/yellow]")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[bold red]Error: {str(e)}[/bold red]")
            sys.exit(1)

    def generate_idea(self) -> Dict:
        """Step 1: Generate an app idea using LLM."""
        console.print("\n[bold]Step 1: Generating App Idea[/bold]")
        
        # Get user context if they want to provide any
        context = Prompt.ask(
            "What kind of app are you interested in? (Press Enter for LLM to decide)",
            default=""
        )
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Generating app idea...", total=None)
            
            prompt = self._build_idea_prompt(context)
            response = self.llm.generate(prompt)
            
        idea = self._parse_idea_response(response)
        
        console.print(Panel(
            f"[bold]App Name:[/bold] {idea['name']}\n"
            f"[bold]Description:[/bold] {idea['description']}\n"
            f"[bold]Target Users:[/bold] {idea['target_users']}\n"
            f"[bold]Key Features:[/bold]\n" + "\n".join(f"  • {f}" for f in idea['features']),
            title="Generated App Idea",
            border_style="green"
        ))
        
        if not Confirm.ask("Do you want to proceed with this idea?", default=True):
            if Confirm.ask("Generate a new idea?"):
                return self.generate_idea()
            else:
                raise KeyboardInterrupt()
        
        # Save idea
        self._save_to_file("idea.json", idea)
        return idea

    def select_theme_and_inspiration(self) -> Dict:
        """Step 2: Search for inspiration and select design theme."""
        console.print("\n[bold]Step 2: Theme Selection & Inspiration[/bold]")
        
        # Get inspiration from LLM
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Searching for design inspiration...", total=None)
            
            inspiration_prompt = self._build_inspiration_prompt()
            inspiration = self.llm.generate(inspiration_prompt)
        
        console.print(Panel(
            inspiration,
            title="Design Inspiration",
            border_style="blue"
        ))
        
        # Let user select theme
        theme = self.theme_selector.select_theme()
        
        theme_data = {
            "theme": theme,
            "inspiration": inspiration,
            "selected_at": datetime.now().isoformat()
        }
        
        self._save_to_file("theme.json", theme_data)
        return theme_data

    def generate_specification(self, idea: Dict, theme: Dict) -> Dict:
        """Step 3: Generate specification document."""
        console.print("\n[bold]Step 3: Generating Specification Document[/bold]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Creating specification...", total=None)
            
            prompt = self._build_specification_prompt(idea, theme)
            response = self.llm.generate(prompt)
        
        spec = self._parse_specification_response(response)
        
        console.print(Panel(
            Markdown(self._format_specification(spec)),
            title="Generated Specification",
            border_style="magenta"
        ))
        
        self._save_to_file("specification.json", spec)
        self._save_to_file("specification.md", self._format_specification(spec))
        
        return spec

    def review_and_update_specification(self, spec: Dict) -> Dict:
        """Step 4: Allow user to review and update specification."""
        console.print("\n[bold]Step 4: Review & Update Specification[/bold]")
        
        if not Confirm.ask("Would you like to make changes to the specification?", default=False):
            return spec
        
        console.print("\n[cyan]Choose what to update:[/cyan]")
        console.print("1. Edit specification manually")
        console.print("2. Request AI to make specific changes")
        console.print("3. Keep current specification")
        
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"], default="3")
        
        if choice == "1":
            spec = self._manual_edit_specification(spec)
        elif choice == "2":
            spec = self._ai_update_specification(spec)
        
        self._save_to_file("specification_final.json", spec)
        self._save_to_file("specification_final.md", self._format_specification(spec))
        
        return spec

    def create_folder_structure(self, spec: Dict) -> Dict:
        """Step 5: Create app folder structure."""
        console.print("\n[bold]Step 5: Creating App Folder Structure[/bold]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Generating folder structure...", total=None)
            
            structure = self.folder_generator.generate(spec)
        
        console.print(Panel(
            self._format_folder_tree(structure),
            title="App Folder Structure",
            border_style="yellow"
        ))
        
        # Create actual folders
        app_name = spec.get('app_name', 'my_flutter_app').lower().replace(' ', '_')
        app_dir = self.output_dir / app_name
        
        self.folder_generator.create_folders(structure, app_dir)
        
        console.print(f"\n[green]✓ Folder structure created at: {app_dir}[/green]")
        
        self._save_to_file("folder_structure.json", structure)
        
        return structure

    def build_application(self, spec: Dict, folder_structure: Dict):
        """Step 6: Build the full application."""
        console.print("\n[bold]Step 6: Building Full Application[/bold]")
        
        app_name = spec.get('app_name', 'my_flutter_app').lower().replace(' ', '_')
        app_dir = self.output_dir / app_name
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Building application files...", total=None)
            
            self.app_generator.generate_app(spec, folder_structure, app_dir)
        
        console.print(f"\n[green]✓ Application built successfully at: {app_dir}[/green]")
        console.print("\n[cyan]Next steps:[/cyan]")
        console.print(f"1. cd {app_dir}")
        console.print("2. flutter pub get")
        console.print("3. flutter run")

    # Helper methods
    def _build_idea_prompt(self, context: str) -> str:
        """Build prompt for idea generation."""
        base_prompt = """Generate a creative and practical mobile app idea for a Flutter application.

The app should be:
- Feasible to build in one day with proper planning
- Useful and solve a real problem
- Have clear target users
- Include 3-5 key features

Provide your response in JSON format with the following structure:
{
    "name": "App Name",
    "description": "Brief description of the app",
    "target_users": "Who will use this app",
    "features": ["Feature 1", "Feature 2", "Feature 3"],
    "problem_solved": "What problem does this app solve"
}
"""
        if context:
            base_prompt += f"\nUser context: {context}"
        
        return base_prompt

    def _build_inspiration_prompt(self) -> str:
        """Build prompt for design inspiration."""
        return """Provide design inspiration for a mobile application. Suggest:

1. Modern design trends that work well for mobile apps
2. Color palette suggestions
3. UI/UX best practices
4. Reference to popular apps with good design
5. Specific design elements that could enhance user experience

Keep the response concise but informative."""

    def _build_specification_prompt(self, idea: Dict, theme: Dict) -> str:
        """Build prompt for specification generation."""
        return f"""Create a detailed specification document for a Flutter mobile application.

App Idea:
{json.dumps(idea, indent=2)}

Design Theme:
{theme['theme']['name']}

The specification should include:
1. App Overview
2. Technical Requirements
3. Feature Specifications (detailed)
4. Screen Layouts and Navigation
5. Data Models
6. API Requirements (if any)
7. Design Guidelines
8. Testing Requirements

Provide your response in JSON format with structured sections."""

    def _parse_idea_response(self, response: str) -> Dict:
        """Parse LLM response for idea generation."""
        try:
            # Try to extract JSON from response
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response[start:end])
        except:
            pass
        
        # Fallback to default structure
        return {
            "name": "My Flutter App",
            "description": response[:200],
            "target_users": "Mobile users",
            "features": ["Feature 1", "Feature 2", "Feature 3"],
            "problem_solved": "Solves user needs"
        }

    def _parse_specification_response(self, response: str) -> Dict:
        """Parse LLM response for specification."""
        try:
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response[start:end])
        except:
            pass
        
        return {
            "app_name": "My Flutter App",
            "specification": response,
            "created_at": datetime.now().isoformat()
        }

    def _format_specification(self, spec: Dict) -> str:
        """Format specification for display."""
        if isinstance(spec.get('specification'), str):
            return spec['specification']
        
        return json.dumps(spec, indent=2)

    def _format_folder_tree(self, structure: Dict, indent: int = 0) -> str:
        """Format folder structure as tree."""
        lines = []
        prefix = "  " * indent
        
        if isinstance(structure, dict):
            for key, value in structure.items():
                if isinstance(value, dict):
                    lines.append(f"{prefix}📁 {key}/")
                    lines.append(self._format_folder_tree(value, indent + 1))
                elif isinstance(value, list):
                    lines.append(f"{prefix}📁 {key}/")
                    for item in value:
                        lines.append(f"{prefix}  📄 {item}")
                else:
                    lines.append(f"{prefix}📄 {key}")
        
        return "\n".join(lines)

    def _manual_edit_specification(self, spec: Dict) -> Dict:
        """Allow manual editing of specification."""
        console.print("\n[yellow]Opening specification for manual editing...[/yellow]")
        console.print("[dim]The specification has been saved to specification.md[/dim]")
        console.print("[dim]Please edit the file and save it, then press Enter to continue.[/dim]")
        
        Prompt.ask("Press Enter when you're done editing")
        
        # In a real implementation, we would reload the edited file
        return spec

    def _ai_update_specification(self, spec: Dict) -> Dict:
        """Use AI to update specification based on user feedback."""
        feedback = Prompt.ask("\nWhat changes would you like to make?")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Updating specification...", total=None)
            
            prompt = f"""Update the following specification based on this feedback:

Feedback: {feedback}

Current Specification:
{json.dumps(spec, indent=2)}

Provide the updated specification in the same JSON format."""
            
            response = self.llm.generate(prompt)
            updated_spec = self._parse_specification_response(response)
        
        console.print(Panel(
            Markdown(self._format_specification(updated_spec)),
            title="Updated Specification",
            border_style="magenta"
        ))
        
        return updated_spec

    def _save_to_file(self, filename: str, data):
        """Save data to output file."""
        filepath = self.output_dir / filename
        
        if filename.endswith('.json'):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        else:
            with open(filepath, 'w') as f:
                if isinstance(data, dict):
                    f.write(json.dumps(data, indent=2))
                else:
                    f.write(str(data))


def main():
    """Main entry point."""
    workflow = OneDayAppWorkflow()
    workflow.run()


if __name__ == "__main__":
    main()
