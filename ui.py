# User gi
"""
AI Design Theme Generation Agent using LangChain & LangGraph
Analyzes similar apps and creates design themes with layout, colors, typography, etc.
"""

from typing import TypedDict, Annotated, List, Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json
import operator

# Define the state structure
class AgentState(TypedDict):
    user_input: str
    similar_apps: List[Dict[str, Any]]
    design_themes: List[Dict[str, Any]]
    selected_theme: Dict[str, Any]
    user_preferences: str
    final_prompt: Dict[str, Any]
    messages: Annotated[List, operator.add]

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7,api_key="")

# Node 1: Search for similar apps
def search_similar_apps(state: AgentState) -> AgentState:
    """Search for similar mobile apps based on user input"""
    user_input = state['user_input']
    
    prompt = f"""
    Based on this app request: "{user_input}"
    
    Research and list 5 similar successful mobile apps. For each app, provide:
    - App name
    - Key design characteristics
    - Color scheme
    - Layout approach
    - Typography style
    - Unique design elements
    
    Format as JSON array with these fields for each app.
    """
    
    messages = [
        SystemMessage(content="You are a UX/UI research expert specializing in mobile app design analysis."),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    # Parse the response to extract similar apps
    try:
        similar_apps = json.loads(response.content)
    except:
        # Fallback if JSON parsing fails
        similar_apps = [
            {
                "app_name": "Example App 1",
                "design_characteristics": "Modern, minimalist",
                "color_scheme": ["#FF6B6B", "#4ECDC4"],
                "layout": "Card-based",
                "typography": "Sans-serif, clean"
            }
        ]
    
    state['similar_apps'] = similar_apps
    state['messages'].append(f"✅ Found {len(similar_apps)} similar apps")
    
    return state

# Node 2: Analyze and create design themes
def create_design_themes(state: AgentState) -> AgentState:
    """Analyze similar apps and generate 2 distinct design themes"""
    similar_apps = state['similar_apps']
    user_input = state['user_input']
    
    prompt = f"""
    Based on the user's request for: "{user_input}"
    
    And analysis of these similar apps:
    {json.dumps(similar_apps, indent=2)}
    
    Create 2 DISTINCT design themes. For each theme provide:
    
    1. **Layout Types**: 
       - Primary layout structure (e.g., Card-based, List-based, Grid, Tab-based)
       - Navigation pattern (e.g., Bottom nav, Side drawer, Top tabs)
       - Screen hierarchy approach
    
    2. **Identity Color Palettes**:
       - Primary color (hex code)
       - Secondary color (hex code)
       - Accent color (hex code)
       - Background colors (2-3 variations)
       - Text colors (primary, secondary)
       - Color psychology reasoning
    
    3. **Identity Typography**:
       - Heading font family
       - Body font family
       - Font size scale (h1, h2, h3, body, caption)
       - Font weights used
       - Line height recommendations
    
    4. **Spacing Scales**:
       - Base unit (e.g., 4px, 8px)
       - Spacing scale (xs, sm, md, lg, xl, 2xl)
       - Padding system
       - Margin system
    
    5. **Component Styles**:
       - Button styles (primary, secondary, tertiary)
       - Input field styles
       - Card styles
       - Icon style approach
       - Border radius system
       - Shadow/elevation system
    
    6. **Imagery Style**:
       - Photography style (if applicable)
       - Illustration style
       - Icon style (outlined, filled, etc.)
       - Image treatment (filters, overlays)
    
    Make Theme 1 more modern/bold and Theme 2 more classic/elegant.
    Return as JSON with structure: {{"themes": [theme1, theme2]}}
    """
    
    messages = [
        SystemMessage(content="You are an expert UI/UX designer who creates comprehensive design systems."),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    # Parse themes
    try:
        themes_data = json.loads(response.content)
        design_themes = themes_data.get('themes', [])
    except:
        # Fallback themes
        design_themes = [
            {
                "theme_name": "Modern Bold",
                "layout_types": {
                    "primary_structure": "Card-based with prominent imagery",
                    "navigation": "Bottom navigation with floating action button",
                    "hierarchy": "Clear visual hierarchy with generous whitespace"
                },
                "color_palette": {
                    "primary": "#FF6B6B",
                    "secondary": "#4ECDC4",
                    "accent": "#FFE66D",
                    "background": ["#FFFFFF", "#F7F7F7"],
                    "text": ["#2D3436", "#636E72"]
                }
            },
            {
                "theme_name": "Classic Elegant",
                "layout_types": {
                    "primary_structure": "List-based with subtle cards",
                    "navigation": "Side drawer with top app bar",
                    "hierarchy": "Traditional hierarchy with clear sections"
                },
                "color_palette": {
                    "primary": "#2C3E50",
                    "secondary": "#E8B4B8",
                    "accent": "#95A5A6",
                    "background": ["#FFFFFF", "#FAFAFA"],
                    "text": ["#2C3E50", "#7F8C8D"]
                }
            }
        ]
    
    state['design_themes'] = design_themes
    state['messages'].append(f"✅ Created {len(design_themes)} design themes")
    
    return state

# Node 3: Present themes to user
def present_themes(state: AgentState) -> AgentState:
    """Format and present the two themes to the user"""
    themes = state['design_themes']
    
    presentation = "\n\n" + "="*60 + "\n"
    presentation += "🎨 DESIGN THEME OPTIONS\n"
    presentation += "="*60 + "\n\n"
    
    for idx, theme in enumerate(themes, 1):
        presentation += f"{'#'*60}\n"
        presentation += f"# THEME {idx}: {theme.get('theme_name', f'Theme {idx}')}\n"
        presentation += f"{'#'*60}\n\n"
        
        # Layout
        presentation += f"## 📐 Layout Types\n"
        layout = theme.get('layout_types', {})
        for key, value in layout.items():
            presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        # Colors
        presentation += f"\n## 🎨 Color Palette\n"
        colors = theme.get('color_palette', {})
        for key, value in colors.items():
            if isinstance(value, list):
                presentation += f"| {key.replace('_', ' ').title():<25} | {', '.join(value)}\n"
            else:
                presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        # Typography
        presentation += f"\n## 🔤 Typography\n"
        typo = theme.get('typography', {})
        for key, value in typo.items():
            presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        # Spacing
        presentation += f"\n## 📏 Spacing Scale\n"
        spacing = theme.get('spacing', {})
        for key, value in spacing.items():
            presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        # Components
        presentation += f"\n## 🧩 Component Styles\n"
        components = theme.get('components', {})
        for key, value in components.items():
            presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        # Imagery
        presentation += f"\n## 🖼️ Imagery Style\n"
        imagery = theme.get('imagery', {})
        for key, value in imagery.items():
            presentation += f"| {key.replace('_', ' ').title():<25} | {value}\n"
        
        presentation += f"\n{'='*60}\n\n"
    
    state['messages'].append(presentation)
    return state

# Node 4: Get user selection and preferences
def get_user_selection(state: AgentState) -> AgentState:
    """
    This function would normally wait for user input.
    In production, this would be interactive.
    For demo purposes, we'll simulate a selection.
    """
    # In a real implementation, you'd pause here and wait for user input
    # For now, we'll simulate selecting theme 1 with some preferences
    
    state['selected_theme'] = state['design_themes'][0]
    state['user_preferences'] = "Make it more vibrant with playful animations"
    state['messages'].append("✅ User selected Theme 1 with preferences")
    
    return state

# Node 5: Generate final prompt
def generate_final_prompt(state: AgentState) -> AgentState:
    """Generate the final design prompt incorporating user preferences"""
    selected_theme = state['selected_theme']
    preferences = state['user_preferences']
    user_input = state['user_input']
    
    prompt = f"""
    Create a comprehensive final design specification for: "{user_input}"
    
    Based on the selected theme:
    {json.dumps(selected_theme, indent=2)}
    
    And user preferences: "{preferences}"
    
    Generate a complete, implementation-ready design specification in JSON format with ALL details.
    Include specific measurements, exact hex codes, font sizes, spacing values, etc.
    """
    
    messages = [
        SystemMessage(content="You are a design system architect creating production-ready specifications."),
        HumanMessage(content=prompt)
    ]
    
    response = llm.invoke(messages)
    
    try:
        final_prompt = json.loads(response.content)
    except:
        final_prompt = {
            "app_name": user_input,
            "theme": selected_theme,
            "preferences": preferences,
            "status": "Design specification ready"
        }
    
    state['final_prompt'] = final_prompt
    state['messages'].append("✅ Final design specification generated")
    
    return state

# Node 6: Present final JSON
def present_final_json(state: AgentState) -> AgentState:
    """Present the final JSON in a formatted way using | and #"""
    final = state['final_prompt']
    
    output = "\n\n" + "#"*80 + "\n"
    output += "# 🎯 FINAL DESIGN SPECIFICATION\n"
    output += "#"*80 + "\n\n"
    
    def format_dict(d, indent=0):
        result = ""
        for key, value in d.items():
            prefix = "|   " * indent
            if isinstance(value, dict):
                result += f"{prefix}| {key}:\n"
                result += format_dict(value, indent + 1)
            elif isinstance(value, list):
                result += f"{prefix}| {key}:\n"
                for item in value:
                    if isinstance(item, dict):
                        result += format_dict(item, indent + 1)
                    else:
                        result += f"{prefix}|   | • {item}\n"
            else:
                result += f"{prefix}| {key:<30} | {value}\n"
        return result
    
    output += format_dict(final)
    output += "\n" + "#"*80 + "\n"
    
    # Also add raw JSON
    output += "\n## Raw JSON:\n"
    output += "```json\n"
    output += json.dumps(final, indent=2)
    output += "\n```\n"
    
    state['messages'].append(output)
    return state

# Build the graph
def create_design_agent():
    """Create and compile the LangGraph agent"""
    
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("search_apps", search_similar_apps)
    workflow.add_node("create_themes", create_design_themes)
    workflow.add_node("present_themes", present_themes)
    workflow.add_node("get_selection", get_user_selection)
    workflow.add_node("generate_final", generate_final_prompt)
    workflow.add_node("present_json", present_final_json)
    
    # Add edges
    workflow.set_entry_point("search_apps")
    workflow.add_edge("search_apps", "create_themes")
    workflow.add_edge("create_themes", "present_themes")
    workflow.add_edge("present_themes", "get_selection")
    workflow.add_edge("get_selection", "generate_final")
    workflow.add_edge("generate_final", "present_json")
    workflow.add_edge("present_json", END)
    
    return workflow.compile()

# Main execution
if __name__ == "__main__":
    # Create the agent
    agent = create_design_agent()
    
    # Initial state
    initial_state = {
        "user_input": "Build a food delivery app",
        "similar_apps": [],
        "design_themes": [],
        "selected_theme": {},
        "user_preferences": "",
        "final_prompt": {},
        "messages": []
    }
    
    # Run the agent
    print("🚀 Starting Design Theme Generation Agent...")
    print("="*60)
    
    final_state = agent.invoke(initial_state)
    
    # Print all messages
    for message in final_state['messages']:
        print(message)
    
    print("\n✅ Agent workflow completed!")
    print("="*60)