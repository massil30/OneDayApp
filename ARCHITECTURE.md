# OneDayApp Architecture

## Overview

OneDayApp is a Python-based workflow orchestration system that uses Large Language Models (LLMs) to automate Flutter app development. This document describes the system architecture and design decisions.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     OneDayApp System                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         oneday_app.py (Main Orchestrator)          │    │
│  │  - Workflow coordination                            │    │
│  │  - User interaction                                 │    │
│  │  - Progress tracking                                │    │
│  └─────┬────────────────────────────────────────┬─────┘    │
│        │                                        │           │
│  ┌─────▼─────────┐                      ┌──────▼──────┐   │
│  │ llm_provider  │                      │theme_selector│   │
│  │  - OpenAI     │                      │  - 3 Themes  │   │
│  │  - Anthropic  │                      │  - Colors    │   │
│  │  - Unified API│                      │  - Typography│   │
│  └─────┬─────────┘                      └──────┬──────┘   │
│        │                                        │           │
│  ┌─────▼──────────────────────────────────────▼──────┐    │
│  │              app_generator.py                     │    │
│  │  - Code generation                                 │    │
│  │  - Screen creation                                 │    │
│  │  - Model generation                                │    │
│  └─────┬──────────────────────────────────────────────┘   │
│        │                                                    │
│  ┌─────▼─────────────────────────┐                        │
│  │    folder_structure.py        │                        │
│  │  - Flutter project structure  │                        │
│  │  - File templates             │                        │
│  │  - Directory creation         │                        │
│  └───────────────────────────────┘                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Generates
                           ▼
                  ┌─────────────────┐
                  │  Flutter App    │
                  │  - lib/         │
                  │  - assets/      │
                  │  - test/        │
                  │  - pubspec.yaml │
                  └─────────────────┘
```

## Component Details

### 1. Main Orchestrator (oneday_app.py)

**Purpose**: Coordinates the entire workflow from idea to app generation.

**Key Responsibilities**:
- User interaction and input collection
- Workflow step sequencing
- Progress tracking and reporting
- File output management

**Main Methods**:
```python
class OneDayAppWorkflow:
    def run()                              # Main workflow entry point
    def generate_idea()                    # Step 1: Idea generation
    def select_theme_and_inspiration()     # Step 2: Theme selection
    def generate_specification()           # Step 3: Spec generation
    def review_and_update_specification()  # Step 4: User review
    def create_folder_structure()          # Step 5: Folder creation
    def build_application()                # Step 6: App building
```

### 2. LLM Provider (llm_provider.py)

**Purpose**: Provides unified interface for different LLM providers.

**Supported Providers**:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude 3.5 Sonnet)

**Architecture Pattern**: Adapter Pattern
```python
class LLMProvider:
    def __init__(provider)        # Initialize provider
    def generate(prompt)          # Unified generation method
    def _generate_openai()        # OpenAI-specific implementation
    def _generate_anthropic()     # Anthropic-specific implementation
```

**Configuration**: Environment variables
```
LLM_PROVIDER=openai|anthropic
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
```

### 3. Theme Selector (theme_selector.py)

**Purpose**: Manages design theme selection and configuration.

**Themes**:
1. **Modern Minimalist**
   - Target: Professional, B2B apps
   - Colors: Cool, sophisticated palette
   - Style: Clean, minimal

2. **Material Design**
   - Target: Consumer apps
   - Colors: Bold, Google-inspired
   - Style: Elevation, shadows, animations

3. **Appetizing / Food-focused**
   - Target: Food, hospitality apps
   - Colors: Warm, inviting
   - Style: Rounded, friendly

**Data Structure**:
```python
theme = {
    "name": str,
    "description": str,
    "colors": {
        "primary": hex,
        "secondary": hex,
        "accent": hex,
        "background": hex,
        "text": hex
    },
    "typography": {
        "heading_font": str,
        "body_font": str
    },
    "characteristics": [str]
}
```

### 4. Folder Structure Generator (folder_structure.py)

**Purpose**: Creates Flutter project structure and initial files.

**Structure Template**:
```
app_name/
├── lib/
│   ├── models/       # Data models
│   ├── screens/      # Screen widgets
│   ├── widgets/      # Reusable widgets
│   ├── services/     # Business logic
│   ├── utils/        # Helper functions
│   ├── constants/    # App constants
│   └── main.dart     # Entry point
├── assets/           # Resources
├── test/             # Tests
└── pubspec.yaml      # Dependencies
```

**Generated Files**:
- `main.dart`: App entry point
- `pubspec.yaml`: Dependencies configuration
- `README.md`: Project documentation
- `.gitignore`: Git ignore rules
- `analysis_options.yaml`: Linting configuration

### 5. App Generator (app_generator.py)

**Purpose**: Generates Flutter application code using LLM.

**Generation Pipeline**:
```
Specification → LLM Prompt → Generated Code → File Creation
```

**Generated Components**:

1. **Main Application**
   - MaterialApp setup
   - Theme configuration
   - Routing setup

2. **Screens**
   - One per feature
   - StatefulWidget or StatelessWidget
   - Basic UI implementation

3. **Models**
   - Data classes
   - JSON serialization
   - Validation logic

4. **Constants**
   - colors.dart: Color definitions
   - strings.dart: Text constants
   - themes.dart: Theme configuration

## Workflow Sequence

```
User Start
    │
    ▼
┌────────────────┐
│ 1. Idea Gen    │ → LLM generates app idea
└────┬───────────┘
     │
     ▼
┌────────────────┐
│ 2. Theme       │ → User selects design theme
└────┬───────────┘   + LLM provides inspiration
     │
     ▼
┌────────────────┐
│ 3. Spec Gen    │ → LLM creates specification
└────┬───────────┘
     │
     ▼
┌────────────────┐
│ 4. Review      │ → User reviews/updates spec
└────┬───────────┘   (optional AI assistance)
     │
     ▼
┌────────────────┐
│ 5. Structure   │ → System creates folders
└────┬───────────┘
     │
     ▼
┌────────────────┐
│ 6. Generate    │ → LLM generates code
└────┬───────────┘   System writes files
     │
     ▼
Flutter App Ready
```

## Data Flow

### Input Flow
```
User Input → Prompt Engineering → LLM API → Response Parsing → Data Storage
```

### Output Flow
```
Specification → Template Application → Code Generation → File Writing → Flutter Project
```

## File Organization

```
OneDayApp/
├── Core Modules
│   ├── oneday_app.py          # Main orchestrator
│   ├── llm_provider.py         # LLM abstraction
│   ├── theme_selector.py       # Theme management
│   ├── folder_structure.py     # Structure generation
│   └── app_generator.py        # Code generation
│
├── Documentation
│   ├── README.md              # Overview
│   ├── USAGE.md               # User guide
│   ├── QUICKSTART.md          # Quick start
│   ├── EXAMPLES.md            # Examples
│   ├── CONTRIBUTING.md        # Contribution guide
│   └── ARCHITECTURE.md        # This file
│
├── Configuration
│   ├── requirements.txt        # Dependencies
│   ├── .env.example           # Environment template
│   └── .gitignore             # Git ignore rules
│
├── Tools
│   ├── example_demo.py        # Demo script
│   └── test_setup.py          # Validation script
│
└── Output
    └── output/                # Generated apps
```

## Design Patterns

### 1. Orchestrator Pattern
- `OneDayAppWorkflow` orchestrates all components
- Centralized workflow control
- Easy to extend with new steps

### 2. Adapter Pattern
- `LLMProvider` adapts different LLM APIs
- Unified interface for providers
- Easy to add new providers

### 3. Template Method Pattern
- Folder structure uses templates
- Consistent project structure
- Customizable templates

### 4. Strategy Pattern
- Theme selection uses strategy pattern
- Different themes = different strategies
- Easy to add new themes

## Extension Points

### Adding a New LLM Provider

1. Implement initialization method:
```python
def _initialize_newprovider(self):
    from newprovider import Client
    self.client = Client(api_key=os.getenv("NEWPROVIDER_API_KEY"))
    self.model = os.getenv("NEWPROVIDER_MODEL")
```

2. Implement generation method:
```python
def _generate_newprovider(self, prompt: str, max_tokens: int) -> str:
    response = self.client.generate(prompt, max_tokens=max_tokens)
    return response.text
```

3. Add to environment template:
```
NEWPROVIDER_API_KEY=your_key_here
NEWPROVIDER_MODEL=model_name
```

### Adding a New Theme

1. Add to `theme_selector.py`:
```python
"4": {
    "name": "New Theme",
    "description": "Description",
    "colors": { ... },
    "typography": { ... },
    "characteristics": [ ... ]
}
```

### Adding a New Workflow Step

1. Add method to `OneDayAppWorkflow`:
```python
def new_step(self):
    console.print("\n[bold]Step X: New Step[/bold]")
    # Implementation
    return result
```

2. Add to workflow in `run()`:
```python
def run(self):
    # ... existing steps
    new_result = self.new_step()
    # ... continue
```

## Security Considerations

### API Key Management
- Keys stored in `.env` file (not in git)
- Environment variable based configuration
- No hardcoded credentials

### Code Generation Safety
- Review generated code before use
- No execution of generated code by system
- User has full control over output

### Data Privacy
- No data sent to third parties except LLM providers
- User controls what information is shared
- Local file storage only

## Performance Considerations

### LLM API Calls
- Minimize number of API calls
- Use appropriate `max_tokens` limits
- Implement retry logic for failures

### File I/O
- Batch file operations where possible
- Use efficient path operations
- Avoid unnecessary file reads/writes

### Memory Usage
- Stream large responses when possible
- Clean up temporary data
- Efficient data structures

## Error Handling

### Strategy
```python
try:
    # Workflow step
except KeyboardInterrupt:
    # User cancellation
except Exception as e:
    # Error handling
    console.print(f"Error: {str(e)}")
    # Graceful degradation
```

### Recovery
- Saved intermediate results
- Can resume from last successful step
- Clear error messages for users

## Testing Strategy

### Current Testing
- Manual testing with demo script
- Syntax validation with py_compile
- Import testing

### Future Testing
- Unit tests for each module
- Integration tests for workflow
- End-to-end tests with mock LLM
- CI/CD pipeline

## Dependencies

### Core Dependencies
```
rich>=13.0.0          # Terminal UI
python-dotenv>=1.0.0  # Environment variables
pyyaml>=6.0           # YAML parsing
```

### Optional Dependencies
```
openai>=1.0.0         # OpenAI API
anthropic>=0.7.0      # Anthropic API
```

## Future Enhancements

### Short-term
- [ ] Add more LLM providers
- [ ] Enhance error handling
- [ ] Add progress saving/resuming
- [ ] Improve code generation quality

### Medium-term
- [ ] GUI interface
- [ ] Web dashboard
- [ ] Template marketplace
- [ ] Plugin system

### Long-term
- [ ] Multi-platform support (React Native, etc.)
- [ ] Collaborative features
- [ ] Cloud deployment
- [ ] App store publishing integration

## Conclusion

OneDayApp follows a modular, extensible architecture that separates concerns and makes it easy to add new features. The system is designed to be user-friendly while maintaining flexibility for advanced users.

For implementation details, see the source code. For usage information, see USAGE.md.
