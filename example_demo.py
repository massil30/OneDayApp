#!/usr/bin/env python3
"""
Demo script showing OneDayApp workflow without requiring API keys.
This demonstrates the structure and flow without making actual LLM calls.
"""

from pathlib import Path
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()


def demo_workflow():
    """Run a demo of the OneDayApp workflow."""
    console.print(Panel.fit(
        "[bold cyan]OneDayApp Workflow Demo[/bold cyan]\n"
        "This demo shows the workflow without requiring API keys",
        border_style="cyan"
    ))

    # Step 1: Idea Generation
    console.print("\n[bold]Step 1: Generating App Idea (Demo)[/bold]")
    
    demo_idea = {
        "name": "FitTracker Pro",
        "description": "A comprehensive fitness tracking app for users who want to monitor their workouts, nutrition, and progress over time.",
        "target_users": "Fitness enthusiasts, gym-goers, and health-conscious individuals",
        "features": [
            "Workout logging and tracking",
            "Nutrition diary with calorie counter",
            "Progress photos and measurements",
            "Exercise library with instructions",
            "Social features to share achievements"
        ],
        "problem_solved": "Helps users stay consistent with their fitness goals by providing an all-in-one tracking solution"
    }
    
    console.print(Panel(
        f"[bold]App Name:[/bold] {demo_idea['name']}\n"
        f"[bold]Description:[/bold] {demo_idea['description']}\n"
        f"[bold]Target Users:[/bold] {demo_idea['target_users']}\n"
        f"[bold]Key Features:[/bold]\n" + "\n".join(f"  • {f}" for f in demo_idea['features']),
        title="Generated App Idea (Demo)",
        border_style="green"
    ))

    if not Confirm.ask("Continue with demo?", default=True):
        return

    # Step 2: Theme Selection
    console.print("\n[bold]Step 2: Theme Selection & Inspiration (Demo)[/bold]")
    
    console.print(Panel(
        "[bold cyan]Design Inspiration:[/bold cyan]\n\n"
        "• Use bold, energetic colors to motivate users\n"
        "• Include progress visualizations (charts, graphs)\n"
        "• Make workout logging quick and easy\n"
        "• Use card-based layouts for different activities\n"
        "• Include motivational elements and achievements",
        title="Design Inspiration (Demo)",
        border_style="blue"
    ))
    
    demo_theme = {
        "name": "Material Design",
        "colors": {
            "primary": "#6200EE",
            "secondary": "#03DAC6",
            "accent": "#FF0266",
            "background": "#FFFFFF",
            "text": "#000000"
        }
    }
    
    console.print(f"\n[green]✓ Demo Theme Selected: {demo_theme['name']}[/green]")

    # Step 3: Specification
    console.print("\n[bold]Step 3: Specification Document (Demo)[/bold]")
    
    demo_spec = {
        "app_name": "FitTracker Pro",
        "version": "1.0.0",
        "platform": "Flutter (iOS & Android)",
        "features": demo_idea['features'],
        "screens": [
            "Home Dashboard",
            "Workout Logger",
            "Nutrition Diary",
            "Progress Tracker",
            "Exercise Library",
            "Profile Settings"
        ],
        "data_models": [
            "User",
            "Workout",
            "Exercise",
            "Meal",
            "ProgressEntry"
        ],
        "theme": demo_theme
    }
    
    console.print(Panel(
        f"[bold]App:[/bold] {demo_spec['app_name']}\n"
        f"[bold]Platform:[/bold] {demo_spec['platform']}\n"
        f"[bold]Screens:[/bold] {', '.join(demo_spec['screens'][:3])}...\n"
        f"[bold]Models:[/bold] {', '.join(demo_spec['data_models'][:3])}...",
        title="Specification (Demo)",
        border_style="magenta"
    ))

    # Step 4: Review
    console.print("\n[bold]Step 4: Review & Update (Demo)[/bold]")
    console.print("[dim]In the real workflow, you could edit the specification here.[/dim]")

    # Step 5: Folder Structure
    console.print("\n[bold]Step 5: Creating Folder Structure (Demo)[/bold]")
    
    folder_tree = """📁 fittracker_pro/
  📁 lib/
    📁 models/
      📄 user.dart
      📄 workout.dart
      📄 exercise.dart
    📁 screens/
      📄 home_screen.dart
      📄 workout_screen.dart
      📄 nutrition_screen.dart
    📁 widgets/
    📁 services/
    📁 constants/
      📄 colors.dart
      📄 strings.dart
      📄 themes.dart
    📄 main.dart
  📁 assets/
    📁 images/
    📁 icons/
  📁 test/
  📄 pubspec.yaml
  📄 README.md"""
    
    console.print(Panel(
        folder_tree,
        title="App Folder Structure (Demo)",
        border_style="yellow"
    ))

    # Step 6: Generation
    console.print("\n[bold]Step 6: Building Application (Demo)[/bold]")
    console.print("[green]✓ Demo complete! In the real workflow, the app would be generated here.[/green]")
    
    console.print("\n[bold cyan]What the real workflow would generate:[/bold cyan]")
    console.print("• Complete Flutter project structure")
    console.print("• main.dart with app initialization")
    console.print("• Screen widgets for each feature")
    console.print("• Data model classes")
    console.print("• Theme and styling constants")
    console.print("• Updated pubspec.yaml with dependencies")
    console.print("• README with setup instructions")
    
    console.print("\n[bold cyan]To run the real workflow:[/bold cyan]")
    console.print("1. Set up your API keys in .env")
    console.print("2. Run: python oneday_app.py")
    console.print("3. Follow the interactive prompts")
    console.print("4. Get your complete Flutter app!")


def main():
    """Main entry point."""
    try:
        demo_workflow()
        console.print("\n[bold green]Demo completed successfully![/bold green]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Demo interrupted.[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {str(e)}[/bold red]")


if __name__ == "__main__":
    main()
