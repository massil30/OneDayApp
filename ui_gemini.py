"""
AI Design Theme Generation Agent - V1 with Google Gemini
Complete implementation using Gemini API instead of OpenAI
"""

# ============================================================================
# PROJECT STRUCTURE (Updated for Gemini)
# ============================================================================

"""
design-theme-agent/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── src/
│   ├── __init__.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   └── state.py
│   │
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── search_apps.py
│   │   ├── create_themes.py
│   │   ├── present_themes.py
│   │   ├── user_selection.py
│   │   ├── generate_final.py
│   │   └── present_json.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── theme.py
│   │   ├── app.py
│   │   └── design_spec.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── llm.py
│   │   ├── formatters.py
│   │   ├── validators.py
│   │   └── json_parser.py
│   │
│   └── prompts/
│       ├── __init__.py
│       ├── search_prompts.py
│       ├── theme_prompts.py
│       └── final_prompts.py
│
├── tests/
│   ├── __init__.py
│   ├── test_nodes.py
│   └── test_integration.py
│
├── examples/
│   ├── basic_example.py
│   └── interactive_example.py
│
└── main.py
"""

# ============================================================================
# FILE: requirements.txt
# ============================================================================

REQUIREMENTS = """
# Core Dependencies - Gemini
langchain==0.1.0
langchain-google-genai==0.0.11
langgraph==0.0.25
google-generativeai==0.3.2

# Data Processing
pydantic==2.5.0
python-dotenv==1.0.0

# Utilities
colorama==0.4.6
rich==13.7.0

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
"""

# ============================================================================
# FILE: .env.example
# ============================================================================

ENV_EXAMPLE = """
# Google Gemini API Configuration
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-pro
GEMINI_TEMPERATURE=0.7

# Application Settings
LOG_LEVEL=INFO
DEBUG_MODE=false
"""

# ============================================================================
# FILE: .gitignore
# ============================================================================

GITIGNORE = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# Environment
.env
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log
logs/

# Cache
.cache/
"""

# ============================================================================
# FILE: config/__init__.py
# ============================================================================

CONFIG_INIT = """
from .settings import settings

__all__ = ['settings']
"""

# ============================================================================
# FILE: config/settings.py
# ============================================================================

SETTINGS_PY = """
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    \"\"\"Application settings and configuration\"\"\"
    
    # Google Gemini Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-pro")
    GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
    
    # Application Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
    
    # Agent Settings
    MAX_RETRIES = 3
    TIMEOUT = 60
    
    @classmethod
    def validate(cls):
        \"\"\"Validate required settings\"\"\"
        if not cls.GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY is not set. "
                "Please set it in your .env file or environment variables."
            )
        return True
    
    @classmethod
    def display(cls):
        \"\"\"Display current settings (hide sensitive info)\"\"\"
        return {
            "model": cls.GEMINI_MODEL,
            "temperature": cls.GEMINI_TEMPERATURE,
            "debug_mode": cls.DEBUG_MODE,
            "api_key_set": bool(cls.GOOGLE_API_KEY)
        }

settings = Settings()
"""

# ============================================================================
# FILE: src/__init__.py
# ============================================================================

SRC_INIT = """
__version__ = "1.0.0"
__author__ = "Design Theme Agent"
"""

# ============================================================================
# FILE: src/agents/state.py
# ============================================================================

STATE_PY = """
from typing import TypedDict, Annotated, List, Dict, Any
import operator

class AgentState(TypedDict):
    \"\"\"State definition for the design theme agent workflow\"\"\"
    
    # User Input
    user_input: str
    
    # Step 1: Similar Apps
    similar_apps: List[Dict[str, Any]]
    
    # Step 2: Design Themes
    design_themes: List[Dict[str, Any]]
    
    # Step 3: User Selection
    selected_theme_index: int
    selected_theme: Dict[str, Any]
    user_preferences: str
    
    # Step 4: Final Output
    final_prompt: Dict[str, Any]
    
    # Tracking
    messages: Annotated[List[str], operator.add]
    errors: Annotated[List[str], operator.add]
    
    # Metadata
    current_step: str
    completed_steps: Annotated[List[str], operator.add]
"""

# ============================================================================
# FILE: src/models/theme.py
# ============================================================================

THEME_PY = """
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class LayoutTypes(BaseModel):
    \"\"\"Layout structure definitions\"\"\"
    primary_structure: str = Field(description="Main layout pattern")
    navigation: str = Field(description="Navigation style")
    hierarchy: str = Field(description="Visual hierarchy approach")

class ColorPalette(BaseModel):
    \"\"\"Color palette with reasoning\"\"\"
    primary: str = Field(description="Primary brand color (hex)")
    secondary: str = Field(description="Secondary color (hex)")
    accent: str = Field(description="Accent color (hex)")
    background: List[str] = Field(description="Background colors")
    text: List[str] = Field(description="Text colors")
    reasoning: Optional[str] = Field(default=None, description="Color psychology")

class Typography(BaseModel):
    \"\"\"Typography system\"\"\"
    heading_font: str = Field(description="Font for headings")
    body_font: str = Field(description="Font for body text")
    font_sizes: Dict[str, str] = Field(description="Size scale")
    font_weights: Dict[str, int] = Field(description="Weight scale")
    line_heights: Dict[str, str] = Field(description="Line height values")

class SpacingScale(BaseModel):
    \"\"\"Spacing and rhythm system\"\"\"
    base_unit: str = Field(description="Base spacing unit")
    scale: Dict[str, str] = Field(description="Spacing scale")
    padding_system: Dict[str, str] = Field(description="Padding values")
    margin_system: Dict[str, str] = Field(description="Margin values")

class ComponentStyles(BaseModel):
    \"\"\"Component style definitions\"\"\"
    buttons: Dict[str, str] = Field(description="Button styles")
    inputs: Dict[str, str] = Field(description="Input field styles")
    cards: Dict[str, str] = Field(description="Card styles")
    icons: str = Field(description="Icon style approach")
    border_radius: Dict[str, str] = Field(description="Border radius scale")
    shadows: Dict[str, str] = Field(description="Shadow/elevation system")

class ImageryStyle(BaseModel):
    \"\"\"Imagery and visual style\"\"\"
    photography_style: Optional[str] = Field(default=None)
    illustration_style: str = Field(description="Illustration approach")
    icon_style: str = Field(description="Icon style")
    image_treatment: str = Field(description="Image processing")

class DesignTheme(BaseModel):
    \"\"\"Complete design theme specification\"\"\"
    theme_name: str
    description: str
    layout_types: LayoutTypes
    color_palette: ColorPalette
    typography: Typography
    spacing: SpacingScale
    components: ComponentStyles
    imagery: ImageryStyle

class SimilarApp(BaseModel):
    \"\"\"Similar app analysis\"\"\"
    app_name: str
    design_characteristics: str
    color_scheme: List[str]
    layout_approach: str
    typography_style: str
    unique_elements: str
"""

# ============================================================================
# FILE: src/utils/llm.py
# ============================================================================

LLM_PY = """
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings
import google.generativeai as genai

def initialize_gemini():
    \"\"\"Initialize Google Gemini API\"\"\"
    genai.configure(api_key=settings.GOOGLE_API_KEY)

def get_llm(temperature: float = None) -> ChatGoogleGenerativeAI:
    \"\"\"
    Initialize and return Gemini LLM instance
    
    Args:
        temperature: Override default temperature
        
    Returns:
        ChatGoogleGenerativeAI instance
    \"\"\"
    initialize_gemini()
    
    return ChatGoogleGenerativeAI(
        model=settings.GEMINI_MODEL,
        temperature=temperature or settings.GEMINI_TEMPERATURE,
        google_api_key=settings.GOOGLE_API_KEY,
        convert_system_message_to_human=True  # Gemini-specific
    )
"""

# ============================================================================
# FILE: src/utils/json_parser.py
# ============================================================================

JSON_PARSER_PY = """
import json
import re
from typing import Any, Dict, List, Optional

def extract_json_from_text(text: str) -> Optional[Dict]:
    \"\"\"
    Extract JSON from text that might contain markdown or other formatting
    
    Args:
        text: Text that may contain JSON
        
    Returns:
        Parsed JSON dict or None
    \"\"\"
    # Remove markdown code blocks
    text = re.sub(r'```json\\s*', '', text)
    text = re.sub(r'```\\s*', '', text)
    
    # Try to find JSON object
    json_pattern = r'\\{[^{}]*(?:\\{[^{}]*\\}[^{}]*)*\\}'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue
    
    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None

def safe_json_parse(text: str, default: Any = None) -> Any:
    \"\"\"
    Safely parse JSON with fallback
    
    Args:
        text: JSON string
        default: Default value if parsing fails
        
    Returns:
        Parsed JSON or default value
    \"\"\"
    result = extract_json_from_text(text)
    return result if result is not None else default

def clean_json_string(text: str) -> str:
    \"\"\"
    Clean common JSON formatting issues
    
    Args:
        text: Potentially malformed JSON string
        
    Returns:
        Cleaned JSON string
    \"\"\"
    # Remove common issues
    text = text.strip()
    text = re.sub(r',\\s*}', '}', text)  # Remove trailing commas
    text = re.sub(r',\\s*]', ']', text)  # Remove trailing commas in arrays
    
    return text
"""

# ============================================================================
# FILE: src/utils/formatters.py
# ============================================================================

FORMATTERS_PY = """
import json
from typing import Dict, Any, List

def format_theme_presentation(themes: List[Dict[str, Any]]) -> str:
    \"\"\"
    Format themes using | and # for presentation
    
    Args:
        themes: List of theme dictionaries
        
    Returns:
        Formatted string with themes
    \"\"\"
    presentation = "\\n\\n" + "="*80 + "\\n"
    presentation += "🎨 DESIGN THEME OPTIONS\\n"
    presentation += "="*80 + "\\n\\n"
    
    for idx, theme in enumerate(themes, 1):
        presentation += f"{'#'*80}\\n"
        presentation += f"# THEME {idx}: {theme.get('theme_name', f'Theme {idx}').upper()}\\n"
        presentation += f"# {theme.get('description', '')}\\n"
        presentation += f"{'#'*80}\\n\\n"
        
        # Layout Types
        presentation += "## 📐 LAYOUT TYPES\\n"
        presentation += "-" * 80 + "\\n"
        layout = theme.get('layout_types', {})
        for key, value in layout.items():
            presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        # Color Palette
        presentation += "\\n## 🎨 COLOR PALETTE\\n"
        presentation += "-" * 80 + "\\n"
        colors = theme.get('color_palette', {})
        for key, value in colors.items():
            if isinstance(value, list):
                presentation += f"| {key.replace('_', ' ').title():<30} | {', '.join(value)}\\n"
            else:
                presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        # Typography
        presentation += "\\n## 🔤 TYPOGRAPHY\\n"
        presentation += "-" * 80 + "\\n"
        typo = theme.get('typography', {})
        for key, value in typo.items():
            if isinstance(value, dict):
                presentation += f"| {key.replace('_', ' ').title():<30} | {json.dumps(value)}\\n"
            else:
                presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        # Spacing
        presentation += "\\n## 📏 SPACING SCALE\\n"
        presentation += "-" * 80 + "\\n"
        spacing = theme.get('spacing', {})
        for key, value in spacing.items():
            if isinstance(value, dict):
                vals = ', '.join([f"{k}: {v}" for k, v in value.items()])
                presentation += f"| {key.replace('_', ' ').title():<30} | {vals}\\n"
            else:
                presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        # Components
        presentation += "\\n## 🧩 COMPONENT STYLES\\n"
        presentation += "-" * 80 + "\\n"
        components = theme.get('components', {})
        for key, value in components.items():
            if isinstance(value, dict):
                presentation += f"| {key.replace('_', ' ').title():<30} |\\n"
                for k, v in value.items():
                    presentation += f"|   • {k:<26} | {v}\\n"
            else:
                presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        # Imagery
        presentation += "\\n## 🖼️ IMAGERY STYLE\\n"
        presentation += "-" * 80 + "\\n"
        imagery = theme.get('imagery', {})
        for key, value in imagery.items():
            if value:
                presentation += f"| {key.replace('_', ' ').title():<30} | {value}\\n"
        
        presentation += "\\n" + "="*80 + "\\n\\n"
    
    return presentation

def format_final_json(final: Dict[str, Any]) -> str:
    \"\"\"
    Format final JSON using | and #
    
    Args:
        final: Final design specification dict
        
    Returns:
        Formatted string
    \"\"\"
    output = "\\n\\n" + "#"*80 + "\\n"
    output += "# 🎯 FINAL DESIGN SPECIFICATION\\n"
    output += "#"*80 + "\\n\\n"
    
    def format_dict(d: Dict, indent: int = 0) -> str:
        result = ""
        for key, value in d.items():
            prefix = "|   " * indent
            if isinstance(value, dict):
                result += f"{prefix}| {key.upper()}:\\n"
                result += format_dict(value, indent + 1)
            elif isinstance(value, list):
                result += f"{prefix}| {key.upper()}:\\n"
                for item in value:
                    if isinstance(item, dict):
                        result += format_dict(item, indent + 1)
                    else:
                        result += f"{prefix}|   • {item}\\n"
            else:
                result += f"{prefix}| {key.upper():<35} | {value}\\n"
        return result
    
    output += format_dict(final)
    output += "\\n" + "#"*80 + "\\n"
    
    # Add raw JSON
    output += "\\n## 📄 RAW JSON OUTPUT:\\n"
    output += "=" * 80 + "\\n"
    output += "```json\\n"
    output += json.dumps(final, indent=2)
    output += "\\n```\\n"
    output += "=" * 80 + "\\n"
    
    return output

def format_apps_list(apps: List[Dict[str, Any]]) -> str:
    \"\"\"Format similar apps list\"\"\"
    output = "\\n## 📱 SIMILAR APPS FOUND:\\n"
    output += "=" * 80 + "\\n"
    
    for idx, app in enumerate(apps, 1):
        output += f"\\n### {idx}. {app.get('app_name', 'Unknown App')}\\n"
        output += f"| Design: {app.get('design_characteristics', 'N/A')}\\n"
        output += f"| Layout: {app.get('layout_approach', 'N/A')}\\n"
        output += f"| Colors: {', '.join(app.get('color_scheme', []))}\\n"
        output += "-" * 80 + "\\n"
    
    return output
"""

# ============================================================================
# FILE: src/prompts/search_prompts.py
# ============================================================================

SEARCH_PROMPTS_PY = """
def get_app_search_prompt(user_input: str) -> str:
    \"\"\"
    Generate prompt for searching similar apps
    
    Args:
        user_input: User's app description
        
    Returns:
        Formatted prompt string
    \"\"\"
    return f\"\"\"You are a UX/UI research expert analyzing mobile applications.

Based on this app request: "{user_input}"

Research and identify 5 similar successful mobile apps. For each app, provide detailed analysis.

You MUST respond with ONLY a valid JSON array. No markdown, no explanations, just the JSON.

Structure:
[
  {{
    "app_name": "App Name",
    "design_characteristics": "Brief description of visual design approach",
    "color_scheme": ["#hex1", "#hex2", "#hex3"],
    "layout_approach": "Description of layout structure",
    "typography_style": "Font choices and text styling",
    "unique_elements": "Distinctive design features"
  }}
]

Return exactly 5 apps in this format. Ensure all hex codes are valid.
\"\"\"
"""

# ============================================================================
# FILE: src/prompts/theme_prompts.py
# ============================================================================

THEME_PROMPTS_PY = """
import json

def get_theme_creation_prompt(user_input: str, similar_apps: list) -> str:
    \"\"\"
    Generate prompt for theme creation
    
    Args:
        user_input: User's app description
        similar_apps: List of analyzed similar apps
        
    Returns:
        Formatted prompt string
    \"\"\"
    return f\"\"\"You are an expert UI/UX designer creating comprehensive design systems.

USER REQUEST: "{user_input}"

SIMILAR APPS ANALYSIS:
{json.dumps(similar_apps, indent=2)}

Create 2 DISTINCT design themes. Make Theme 1 modern/bold/vibrant and Theme 2 classic/elegant/refined.

You MUST respond with ONLY valid JSON. No markdown, no code blocks, just the JSON object.

Structure (follow EXACTLY):
{{
  "themes": [
    {{
      "theme_name": "Short memorable name",
      "description": "One sentence describing the theme's essence",
      "layout_types": {{
        "primary_structure": "e.g., Card-based with floating elements",
        "navigation": "e.g., Bottom tab bar with gesture support",
        "hierarchy": "e.g., Bold headings with clear content sections"
      }},
      "color_palette": {{
        "primary": "#hexcode",
        "secondary": "#hexcode",
        "accent": "#hexcode",
        "background": ["#hexcode1", "#hexcode2"],
        "text": ["#hexcode1", "#hexcode2"],
        "reasoning": "Brief color psychology explanation"
      }},
      "typography": {{
        "heading_font": "Font name for headings",
        "body_font": "Font name for body text",
        "font_sizes": {{
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px",
          "caption": "14px"
        }},
        "font_weights": {{
          "bold": 700,
          "semibold": 600,
          "regular": 400
        }},
        "line_heights": {{
          "heading": "1.2",
          "body": "1.6",
          "tight": "1.4"
        }}
      }},
      "spacing": {{
        "base_unit": "8px",
        "scale": {{
          "xs": "4px",
          "sm": "8px",
          "md": "16px",
          "lg": "24px",
          "xl": "32px",
          "2xl": "48px"
        }},
        "padding_system": {{
          "container": "16px",
          "card": "20px",
          "section": "24px"
        }},
        "margin_system": {{
          "element": "8px",
          "section": "32px",
          "page": "16px"
        }}
      }},
      "components": {{
        "buttons": {{
          "primary": "Large, rounded, gradient or solid, prominent shadow",
          "secondary": "Outlined, same size as primary, subtle hover",
          "tertiary": "Text-only, minimal styling, icon optional"
        }},
        "inputs": {{
          "default": "Rounded corners, subtle border, clear focus state",
          "error": "Red border, error icon, helper text below",
          "success": "Green accent, checkmark icon"
        }},
        "cards": {{
          "style": "Elevated with shadow, rounded corners, white background",
          "hover": "Subtle lift effect, increased shadow"
        }},
        "icons": "outlined / filled / rounded",
        "border_radius": {{
          "small": "4px",
          "medium": "8px",
          "large": "16px",
          "full": "9999px"
        }},
        "shadows": {{
          "low": "0 2px 4px rgba(0,0,0,0.1)",
          "medium": "0 4px 8px rgba(0,0,0,0.15)",
          "high": "0 8px 16px rgba(0,0,0,0.2)"
        }}
      }},
      "imagery": {{
        "photography_style": "Bright, natural, lifestyle-focused",
        "illustration_style": "Geometric / organic / minimalist",
        "icon_style": "Outlined with rounded corners",
        "image_treatment": "Slight overlay, rounded corners, lazy load"
      }}
    }}
  ]
}}

Provide exactly 2 themes. Ensure all values are detailed and specific.
\"\"\"

def get_final_spec_prompt(user_input: str, selected_theme: dict, preferences: str) -> str:
    \"\"\"Generate prompt for final specification\"\"\"
    return f\"\"\"You are a design system architect creating production-ready specifications.

APP REQUEST: "{user_input}"

SELECTED THEME:
{json.dumps(selected_theme, indent=2)}

USER PREFERENCES: "{preferences}"

Create a comprehensive, implementation-ready design specification incorporating the user's preferences.

You MUST respond with ONLY valid JSON. Structure:
{{
  "project_name": "App name",
  "theme_selected": "Theme name",
  "user_preferences_applied": "How preferences were incorporated",
  "design_system": {{
    "colors": {{...full color system...}},
    "typography": {{...complete typography system...}},
    "spacing": {{...full spacing system...}},
    "components": {{...all component specifications...}},
    "layouts": {{...layout specifications...}},
    "imagery": {{...imagery guidelines...}}
  }},
  "implementation_notes": ["Note 1", "Note 2"],
  "file_structure": {{
    "components": ["Component1.tsx", "Component2.tsx"],
    "styles": ["colors.ts", "typography.ts"],
    "assets": ["icons/", "images/"]
  }}
}}

Make it comprehensive and ready for development.
\"\"\"
"""

# ============================================================================
# FILE: src/nodes/search_apps.py
# ============================================================================

SEARCH_APPS_PY = """
from langchain_core.messages import HumanMessage, SystemMessage
from src.utils.llm import get_llm
from src.utils.json_parser import safe_json_parse
from src.agents.state import AgentState
from src.prompts.search_prompts import get_app_search_prompt

def search_similar_apps(state: AgentState) -> AgentState:
    \"\"\"
    Node 1: Search for similar mobile apps
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with similar apps
    \"\"\"
    user_input = state['user_input']
    llm = get_llm()
    
    prompt = get_app_search_prompt(user_input)
    
    messages = [
        HumanMessage(content=prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        similar_apps = safe_json_parse(response.content, default=[])
        
        # Validate we got a list
        if not isinstance(similar_apps, list):
            similar_apps = []
        
        state['similar_apps'] = similar_apps
        state['messages'].append(f"✅ Step 1: Found {len(similar_apps)} similar apps")
        state['current_step'] = "search_apps"
        state['completed_steps'].append("search_apps")
        
    except Exception as e:
        error_msg = f"Error in search_apps: {str(e)}"
        state['errors'].append(error_msg)
        state['similar_apps'] = []
        state['messages'].append(f"⚠️ {error_msg}")
    
    return state
"""

# ============================================================================
# FILE: src/nodes/create_themes.py
# ============================================================================

CREATE_THEMES_PY = """
from langchain_core.messages import HumanMessage
from src.utils.llm import get_llm
from src.utils.json_parser import safe_json_parse
from src.agents.state import AgentState
from src.prompts.theme_prompts import get_theme_creation_prompt

def create_design_themes(state: AgentState) -> AgentState:
    \"\"\"
    Node 2: Create design themes
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with design themes
    \"\"\"
    llm = get_llm()
    
    prompt = get_theme_creation_prompt(
        state['user_input'],
        state['similar_apps']
    )
    
    messages = [HumanMessage(content=prompt)]
    
    try:
        response = llm.invoke(messages)
        themes_data = safe_json_parse(response.content, default={"themes": []})
        
        design_themes = themes_data.get('themes', [])
        
        # Validate we have themes
        if not design_themes:
            design_themes = []
        
        state['design_themes'] = design_themes
        state['messages'].append(f"✅ Step 2: Created {len(design_themes)} design themes")
        state['current_step'] = "create_themes"
        state['completed_steps'].append("create_themes")
        
    except Exception as e:
        error_msg = f"Error in create_themes: {str(e)}"
        state['errors'].append(error_msg)
        state['design_themes'] = []
        state['messages'].append(f"⚠️ {error_msg}")
    
    return state
"""

# ============================================================================
# FILE: src/nodes/present_themes.py
# ============================================================================

PRESENT_THEMES_PY = """
from src.agents.state import AgentState
from src.utils.formatters import format_theme_presentation

def present_themes(state: AgentState) -> AgentState:
    \"\"\"
    Node 3: Present themes to user
    
    Args:
        state: Current agent state
        
    Returns:
        Updated state with formatted themes
    \"\"\"
    themes = state['design_themes']
    
    if themes:
        presentation = format_theme_presentation(themes)
        state['messages'].append(presentation)
        state['messages'].append("✅ Step 3: Themes presented to user")
    else:
        state['messages'].append("⚠️ No themes available to present")
    
    state['current_step'] = "present_themes"
    state['completed_steps'].append("present_themes")
    
    return state
"""

# ============================================================================
# FILE: src/nodes/user_selection.py
# ============================================================================

##USER_SELECTION_PY = """
#from src.agents.state import AgentState

#def get_user_selection(state: AgentState) -> AgentState:
 ##  Node 4: Get user theme selection