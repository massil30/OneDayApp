# Contributing to OneDayApp

Thank you for your interest in contributing to OneDayApp! This document provides guidelines and information for contributors.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. Check if the issue already exists in the [Issues](https://github.com/massil30/OneDayApp/issues) section
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Submitting Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/massil30/OneDayApp.git
   cd OneDayApp
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guidelines
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   python example_demo.py  # Test the demo
   # If you have API keys:
   python oneday_app.py    # Test the full workflow
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- (Optional) Flutter SDK for testing generated apps

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/massil30/OneDayApp.git
   cd OneDayApp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys (for full testing)
   ```

## Code Style Guidelines

### Python

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and modular

Example:
```python
def generate_specification(self, idea: Dict, theme: Dict) -> Dict:
    """Generate specification document.
    
    Args:
        idea: Dictionary containing app idea details
        theme: Dictionary containing theme information
        
    Returns:
        Dictionary containing the specification
    """
    # Implementation here
```

### Documentation

- Update README.md for major features
- Update USAGE.md for user-facing changes
- Add inline comments for complex logic
- Keep documentation clear and concise

## Project Structure

```
OneDayApp/
├── oneday_app.py          # Main workflow orchestrator
├── llm_provider.py         # LLM provider abstraction
├── theme_selector.py       # Theme selection module
├── folder_structure.py     # Folder structure generator
├── app_generator.py        # Application code generator
├── example_demo.py         # Demo script
├── requirements.txt        # Python dependencies
├── README.md              # Project overview
├── USAGE.md               # User guide
└── CONTRIBUTING.md        # This file
```

## Areas for Contribution

### High Priority

1. **Additional LLM Providers**
   - Add support for more LLM providers (Google Gemini, Cohere, etc.)
   - Implement fallback mechanisms

2. **Enhanced Generation**
   - Improve code generation quality
   - Add more template options
   - Better error handling

3. **Testing**
   - Add unit tests
   - Add integration tests
   - Test coverage for edge cases

### Medium Priority

1. **Additional Themes**
   - More design theme options
   - Custom theme creation
   - Theme preview functionality

2. **Platform Support**
   - React Native support
   - Native Android/iOS support
   - Web app support

3. **UI Improvements**
   - GUI interface option
   - Web dashboard
   - Better progress visualization

### Low Priority

1. **Documentation**
   - Video tutorials
   - More examples
   - Translations

2. **Optimization**
   - Performance improvements
   - Caching mechanisms
   - Reduced API calls

## Testing Guidelines

### Manual Testing

Before submitting a PR:

1. Run the demo script:
   ```bash
   python example_demo.py
   ```

2. Test import statements:
   ```bash
   python -c "from oneday_app import OneDayAppWorkflow"
   ```

3. Check for syntax errors:
   ```bash
   python -m py_compile *.py
   ```

### Automated Testing (Future)

We plan to add:
- Unit tests with pytest
- Integration tests
- CI/CD pipeline

## Commit Message Guidelines

Use clear, descriptive commit messages:

- `Add: new feature or functionality`
- `Fix: bug fix`
- `Update: changes to existing feature`
- `Docs: documentation changes`
- `Refactor: code restructuring`
- `Test: adding or updating tests`

Examples:
```
Add: support for Google Gemini LLM provider
Fix: folder structure creation on Windows
Update: improve specification generation prompts
Docs: add installation troubleshooting section
```

## Code Review Process

All contributions will be reviewed for:

1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it clean and maintainable?
3. **Documentation**: Are changes documented?
4. **Testing**: Has it been tested?
5. **Style**: Does it follow guidelines?

## Community Guidelines

- Be respectful and constructive
- Help others when possible
- Share your knowledge
- Give credit where due
- Focus on the best outcome for the project

## Questions?

If you have questions:

1. Check existing documentation
2. Search through issues
3. Ask in a new issue
4. Reach out to maintainers

## License

By contributing to OneDayApp, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to OneDayApp! 🚀
