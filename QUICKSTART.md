# OneDayApp Quick Start Guide

Get started with OneDayApp in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key or Anthropic API key
- (Optional) Flutter SDK for running generated apps

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/massil30/OneDayApp.git
cd OneDayApp
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your favorite editor
nano .env  # or vim, code, etc.
```

Add your API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
LLM_PROVIDER=openai
```

Or for Anthropic:
```
ANTHROPIC_API_KEY=your-anthropic-api-key-here
LLM_PROVIDER=anthropic
```

## Your First App

### Run the Demo (No API Key Required)

Try the demo first to see how it works:

```bash
python example_demo.py
```

This will show you the workflow without making any API calls.

### Generate a Real App

```bash
python oneday_app.py
```

Follow the interactive prompts:

1. **Idea Generation**: 
   ```
   What kind of app are you interested in? 
   > fitness tracking app
   ```

2. **Theme Selection**:
   ```
   Select a theme [1/2/3]: 
   > 2  # Choose Material Design
   ```

3. **Review Specification**:
   ```
   Would you like to make changes to the specification? [y/N]:
   > n  # Or 'y' to customize
   ```

4. **Wait for Generation**: The system will create your Flutter app!

### What You Get

After completion, you'll have:

```
output/
└── your_app_name/
    ├── lib/
    │   ├── main.dart
    │   ├── models/
    │   ├── screens/
    │   └── constants/
    ├── assets/
    ├── test/
    └── pubspec.yaml
```

## Run Your Generated App

### Step 1: Navigate to Your App

```bash
cd output/your_app_name
```

### Step 2: Install Flutter Dependencies

```bash
flutter pub get
```

### Step 3: Run the App

```bash
# On connected device/emulator
flutter run

# Or specify a device
flutter devices  # List available devices
flutter run -d chrome  # Run on Chrome
flutter run -d "iPhone 14"  # Run on iOS simulator
```

## Common First-Time Issues

### Issue: "OPENAI_API_KEY not found"

**Solution**: Make sure you:
1. Created the `.env` file (not `.env.example`)
2. Added your actual API key
3. No spaces around the `=` sign

### Issue: "Module not found"

**Solution**: Install requirements again:
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "Flutter command not found"

**Solution**: Install Flutter SDK:
- Follow: https://docs.flutter.dev/get-started/install
- Run: `flutter doctor`

### Issue: Generated app won't run

**Solution**: 
```bash
cd output/your_app_name
flutter clean
flutter pub get
flutter run
```

## Next Steps

### Customize Your App

1. **Modify Screens**: Edit files in `lib/screens/`
2. **Update Theme**: Modify `lib/constants/colors.dart`
3. **Add Features**: Create new screens and widgets
4. **Connect Backend**: Implement API calls in `lib/services/`

### Learn the Workflow

Read the full documentation:
- [README.md](README.md) - Overview and features
- [USAGE.md](USAGE.md) - Detailed usage guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute

### Generate More Apps

Each run creates a new app. Try different:
- App ideas
- Design themes
- Feature combinations

## Pro Tips

### 1. Be Specific with Ideas

Instead of:
```
What kind of app? > shopping app
```

Try:
```
What kind of app? > grocery shopping app for busy parents 
with meal planning and recipe suggestions
```

### 2. Iterate on Specifications

Don't hesitate to request changes:
```
What changes would you like? > Add user authentication and 
dark mode support
```

### 3. Start Simple

For your first app:
- Choose 3-5 features max
- Keep data models simple
- Use a standard theme

### 4. Save Your Outputs

Keep the `output/` directory organized:
```bash
# Rename generated apps
mv output/my_app output/my_app_v1

# Or organize by date
mkdir output/2025-11-14
mv output/my_app output/2025-11-14/
```

## Example Session

Here's a complete example:

```bash
$ python oneday_app.py

OneDayApp Workflow
Build Flutter Apps in One Day with LLM Assistance

Step 1: Generating App Idea
What kind of app are you interested in? recipe app

Generated App Idea:
  App Name: RecipeBox
  Description: A recipe management app...
  
Do you want to proceed with this idea? [Y/n]: y

Step 2: Theme Selection & Inspiration
Available Design Themes:
  1. Modern Minimalist
  2. Material Design
  3. Appetizing / Food-focused

Select a theme [1/2/3]: 3

Step 3: Generating Specification Document
✓ Specification created

Step 4: Review & Update Specification
Would you like to make changes? [y/N]: n

Step 5: Creating App Folder Structure
✓ Folder structure created at: output/recipebox

Step 6: Building Full Application
✓ Application built successfully!

Next steps:
1. cd output/recipebox
2. flutter pub get
3. flutter run
```

## Troubleshooting

### Getting Help

1. **Check the Logs**: Look in the `output/` directory for error messages
2. **Run Demo**: Test with `python example_demo.py` first
3. **Verify Setup**: Ensure all dependencies are installed
4. **Read Docs**: Check [USAGE.md](USAGE.md) for detailed info
5. **Open Issue**: Report bugs on GitHub

### Debug Mode

Add debug output:
```python
# In oneday_app.py, add at the top:
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Resources

- **Flutter Documentation**: https://docs.flutter.dev/
- **OpenAI API Docs**: https://platform.openai.com/docs
- **Anthropic API Docs**: https://docs.anthropic.com/
- **GitHub Repository**: https://github.com/massil30/OneDayApp

## Support

Need help?
- 📖 Read the [full documentation](README.md)
- 💬 Open an [issue on GitHub](https://github.com/massil30/OneDayApp/issues)
- 🤝 Check [CONTRIBUTING.md](CONTRIBUTING.md) to help improve OneDayApp

Happy app building! 🎉
