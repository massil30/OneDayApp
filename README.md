# OneDayApp

Build Flutter Applications in One Day with AI Assistance

## Overview

OneDayApp is an automated workflow system that leverages Large Language Models (LLMs) to help you create complete Flutter applications in a single day. It guides you through the entire app development process, from ideation to implementation.

## Features

The workflow includes the following steps:

1. **Idea Generation**: LLM generates creative app ideas based on your input
2. **Theme Selection & Inspiration**: Choose from three design themes and get design inspiration
   - Modern Minimalist
   - Material Design
   - Appetizing / Food-focused (Warm, colorful)
3. **Specification Generation**: LLM creates detailed specification documents
4. **User Review**: Opportunity to review and update specifications
5. **Folder Structure Creation**: Automatic generation of Flutter project structure
6. **Full App Generation**: LLM builds the complete application code

## Installation

### Prerequisites

- Python 3.8 or higher
- Flutter SDK (for running generated apps)
- An API key for OpenAI or Anthropic

### Setup

1. Clone the repository:
```bash
git clone https://github.com/massil30/OneDayApp.git
cd OneDayApp
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

4. Set your API key in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
# or
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## Usage

Run the OneDayApp workflow:

```bash
python oneday_app.py
```

The workflow will guide you through each step:

1. **Generate App Idea**: Provide context or let the LLM decide
2. **Select Theme**: Choose from three design options
3. **Review Specification**: Review and optionally modify the generated spec
4. **Build App**: The system creates the complete Flutter project

### Output

All generated files are saved in the `output/` directory:

- `idea.json`: Generated app idea
- `theme.json`: Selected theme information
- `specification.json`: Initial specification
- `specification_final.json`: Final approved specification
- `folder_structure.json`: App folder structure
- `{app_name}/`: Complete Flutter project directory

## Design Themes

### 1. Modern Minimalist
- Clean, simple design with lots of whitespace
- Flat design with minimal decorative elements
- Colors: Dark blue-gray primary (#2C3E50), bright blue secondary (#3498DB)

### 2. Material Design
- Google's Material Design principles
- Elevation and shadows, bold colors
- Responsive animations and card-based layouts
- Colors: Purple primary (#6200EE), teal secondary (#03DAC6)

### 3. Appetizing / Food-focused
- Warm, inviting colors perfect for food apps
- High-quality imagery with appetizing visuals
- Rounded corners and friendly UI
- Colors: Orange primary (#FF6B35), warm yellow secondary (#F7931E)

## Project Structure

```
OneDayApp/
├── oneday_app.py           # Main workflow orchestrator
├── llm_provider.py          # LLM provider abstraction (OpenAI/Anthropic)
├── theme_selector.py        # Theme selection and configuration
├── folder_structure.py      # Flutter folder structure generator
├── app_generator.py         # Application code generator
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── output/                 # Generated projects directory
```

## Configuration

### LLM Provider

You can use either OpenAI or Anthropic as your LLM provider. Configure in `.env`:

```
LLM_PROVIDER=openai  # or anthropic
OPENAI_MODEL=gpt-4
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

## Running Generated Apps

After the workflow completes:

1. Navigate to the generated app directory:
```bash
cd output/{your_app_name}
```

2. Install Flutter dependencies:
```bash
flutter pub get
```

3. Run the app:
```bash
flutter run
```

## Example Workflow

```bash
$ python oneday_app.py

┌─────────────────────────────────────────┐
│   OneDayApp Workflow                    │
│   Build Flutter Apps in One Day with    │
│   LLM Assistance                        │
└─────────────────────────────────────────┘

Step 1: Generating App Idea
What kind of app are you interested in? [food delivery]

Generated App Idea:
  Name: FoodQuick
  Description: Fast food delivery app...
  
Do you want to proceed with this idea? [Y/n]: y

Step 2: Theme Selection & Inspiration
Available Design Themes:
  1. Modern Minimalist
  2. Material Design
  3. Appetizing / Food-focused

Select a theme [1/2/3]: 3

Step 3: Generating Specification Document
...
```

## Customization

### Adding Custom Themes

Edit `theme_selector.py` to add new themes to the `THEMES` dictionary.

### Modifying Templates

Edit `folder_structure.py` to customize the Flutter project templates.

### Adjusting LLM Prompts

Modify prompts in `oneday_app.py` and `app_generator.py` to change how the LLM generates content.

## Troubleshooting

### API Key Issues
- Ensure your API key is correctly set in `.env`
- Check that you have sufficient API credits

### Flutter Issues
- Make sure Flutter SDK is properly installed: `flutter doctor`
- Check Flutter version compatibility: `flutter --version`

### Generation Issues
- If generation fails, check your internet connection
- Try increasing `max_tokens` in LLM calls for longer responses

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- Built with Flutter
- Powered by OpenAI GPT-4 and Anthropic Claude
- Uses Rich library for beautiful terminal output 
