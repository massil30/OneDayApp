"""
Theme Selector module for OneDayApp.
Manages design theme selection and configuration.
"""

from typing import Dict
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()


class ThemeSelector:
    """Handles theme selection and design configuration."""

    THEMES = {
        "1": {
            "name": "Modern Minimalist",
            "description": "Clean, simple design with lots of whitespace",
            "colors": {
                "primary": "#2C3E50",
                "secondary": "#3498DB",
                "accent": "#E74C3C",
                "background": "#FFFFFF",
                "text": "#2C3E50"
            },
            "typography": {
                "heading_font": "Montserrat",
                "body_font": "Roboto"
            },
            "characteristics": [
                "Flat design",
                "Generous whitespace",
                "Simple color palette",
                "Clear typography",
                "Minimal decorative elements"
            ]
        },
        "2": {
            "name": "Material Design",
            "description": "Google's Material Design principles",
            "colors": {
                "primary": "#6200EE",
                "secondary": "#03DAC6",
                "accent": "#FF0266",
                "background": "#FFFFFF",
                "text": "#000000"
            },
            "typography": {
                "heading_font": "Roboto",
                "body_font": "Roboto"
            },
            "characteristics": [
                "Elevation and shadows",
                "Bold colors",
                "Responsive animations",
                "Card-based layouts",
                "FAB (Floating Action Button)"
            ]
        },
        "3": {
            "name": "Appetizing / Food-focused (Warm, colorful)",
            "description": "Warm, inviting colors perfect for food apps",
            "colors": {
                "primary": "#FF6B35",
                "secondary": "#F7931E",
                "accent": "#C1121F",
                "background": "#FFF8F3",
                "text": "#333333"
            },
            "typography": {
                "heading_font": "Poppins",
                "body_font": "Open Sans"
            },
            "characteristics": [
                "Warm color palette",
                "High-quality imagery",
                "Appetizing visuals",
                "Rounded corners",
                "Friendly, inviting UI"
            ]
        }
    }

    def select_theme(self) -> Dict:
        """Display theme options and get user selection."""
        console.print("\n[bold cyan]Available Design Themes:[/bold cyan]\n")

        for key, theme in self.THEMES.items():
            console.print(Panel(
                f"[bold]{theme['name']}[/bold]\n\n"
                f"{theme['description']}\n\n"
                f"[dim]Characteristics:[/dim]\n" +
                "\n".join(f"  • {char}" for char in theme['characteristics']),
                title=f"Option {key}",
                border_style="blue"
            ))

        choice = Prompt.ask(
            "\nSelect a theme",
            choices=["1", "2", "3"],
            default="1"
        )

        selected_theme = self.THEMES[choice]
        
        console.print(f"\n[green]✓ Selected: {selected_theme['name']}[/green]")
        
        return selected_theme

    def get_theme_css(self, theme: Dict) -> str:
        """Generate CSS/styling configuration for the selected theme."""
        colors = theme['colors']
        typography = theme['typography']
        
        return f"""
/* Theme: {theme['name']} */

:root {{
    --primary-color: {colors['primary']};
    --secondary-color: {colors['secondary']};
    --accent-color: {colors['accent']};
    --background-color: {colors['background']};
    --text-color: {colors['text']};
    
    --heading-font: '{typography['heading_font']}', sans-serif;
    --body-font: '{typography['body_font']}', sans-serif;
}}
"""

    def get_flutter_theme(self, theme: Dict) -> str:
        """Generate Flutter theme configuration."""
        colors = theme['colors']
        
        return f"""
// Theme: {theme['name']}

ThemeData(
  primaryColor: Color(0xFF{colors['primary'].replace('#', '')}),
  colorScheme: ColorScheme.light(
    primary: Color(0xFF{colors['primary'].replace('#', '')}),
    secondary: Color(0xFF{colors['secondary'].replace('#', '')}),
  ),
  scaffoldBackgroundColor: Color(0xFF{colors['background'].replace('#', '')}),
  textTheme: TextTheme(
    bodyLarge: TextStyle(color: Color(0xFF{colors['text'].replace('#', '')})),
    bodyMedium: TextStyle(color: Color(0xFF{colors['text'].replace('#', '')})),
  ),
)
"""
