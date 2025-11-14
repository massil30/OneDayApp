# OneDayApp - Frequently Asked Questions

## General Questions

### What is OneDayApp?

OneDayApp is an automated workflow system that uses AI (specifically Large Language Models) to help you create complete Flutter mobile applications quickly. It guides you through the entire process from idea generation to working code.

### Can I really build an app in one day?

Yes, with OneDayApp you can generate a fully structured Flutter application in minutes to hours. However, the "one day" refers to getting a functional prototype with proper structure. Adding custom business logic, testing, and polishing will take additional time.

### Do I need to know Flutter to use OneDayApp?

No, but it helps! OneDayApp generates all the boilerplate code, but you'll need some Flutter knowledge to:
- Customize the generated code
- Add business logic
- Fix any issues
- Deploy the app

### Is OneDayApp free?

OneDayApp itself is free and open-source (MIT License). However, you'll need an API key from OpenAI or Anthropic, which are paid services (though they offer free trials).

## Setup and Configuration

### What do I need to get started?

- Python 3.8 or higher
- An API key from OpenAI or Anthropic
- (Optional) Flutter SDK to run generated apps

### How do I get an API key?

**For OpenAI:**
1. Sign up at https://platform.openai.com
2. Navigate to API Keys section
3. Create a new API key
4. Add it to your `.env` file

**For Anthropic:**
1. Sign up at https://console.anthropic.com
2. Navigate to API Keys
3. Create a new API key
4. Add it to your `.env` file

### How much do API calls cost?

Costs vary by provider and model:
- **OpenAI GPT-4**: ~$0.03-0.06 per app generation
- **Anthropic Claude**: ~$0.02-0.04 per app generation

These are estimates. Check provider pricing for current rates.

### Can I use OneDayApp without API keys?

Yes! Run the demo script:
```bash
python example_demo.py
```

This shows you the workflow without making any API calls.

### Why isn't my .env file working?

Common issues:
- File is named `.env.example` instead of `.env`
- Spaces around the `=` sign (should be `KEY=value` not `KEY = value`)
- API key has extra quotes or spaces
- File is in wrong directory

## Usage Questions

### What kind of apps can I create?

You can create any type of mobile app, but OneDayApp works best for:
- CRUD applications
- Content display apps
- Simple productivity tools
- Prototypes and MVPs
- Learning projects

Less suitable for:
- Complex games
- Apps requiring native integrations
- Apps with complex animations
- Real-time communication apps (without additional work)

### Can I create iOS and Android apps?

Yes! Flutter is cross-platform, so generated apps work on both iOS and Android. You'll need:
- Mac for iOS development
- Xcode for iOS builds
- Android Studio for Android builds

### Which theme should I choose?

- **Modern Minimalist**: Professional apps, B2B tools, productivity apps
- **Material Design**: Consumer apps, social media, general-purpose apps
- **Appetizing/Food-focused**: Food delivery, recipe apps, hospitality apps

### Can I change the theme after generation?

Yes! The theme configuration is in `lib/constants/`. You can:
- Edit `colors.dart` to change colors
- Modify `themes.dart` for theme settings
- Update styling throughout the app

### How do I add more features?

After generation:
1. Create new screen files in `lib/screens/`
2. Add new models in `lib/models/`
3. Update routing in `main.dart`
4. Add navigation logic

Or regenerate with updated specifications.

### Can I use my own designs?

Yes! The generated code is fully customizable:
1. Replace colors in `lib/constants/colors.dart`
2. Update `themes.dart` with your theme
3. Modify screen layouts
4. Add your custom widgets

## Technical Questions

### What Flutter version does it generate for?

OneDayApp generates code compatible with Flutter 3.0+. The generated `pubspec.yaml` specifies:
```yaml
environment:
  sdk: '>=3.0.0 <4.0.0'
```

### What dependencies are included?

By default:
- `flutter`: Flutter SDK
- `cupertino_icons`: iOS-style icons
- `http`: HTTP requests (added by OneDayApp)
- `provider`: State management (added by OneDayApp)

You can add more in `pubspec.yaml`.

### Does it support state management?

The generated code includes basic `provider` package setup. You can:
- Use the included Provider
- Switch to Bloc, Riverpod, GetX, etc.
- Implement your preferred solution

### Can I generate web or desktop apps?

Currently, OneDayApp is optimized for mobile (iOS/Android). However, Flutter code often works on web/desktop with minimal changes. Try:
```bash
flutter run -d chrome    # Web
flutter run -d macos     # Desktop
```

### What about null safety?

All generated code is null-safe, following Flutter's modern practices.

### Does it generate tests?

OneDayApp creates test directories and structure but doesn't generate actual test code. You should write tests for your specific logic.

## Troubleshooting

### "Module not found" error

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Generated code has compilation errors

**Possible causes:**
1. Missing dependencies - Run `flutter pub get`
2. Flutter version mismatch - Update Flutter
3. Incomplete generation - Check for errors in output

**Fix:**
```bash
cd output/your_app
flutter clean
flutter pub get
flutter run
```

### App won't run on my device

**Check:**
1. Device is connected: `flutter devices`
2. Flutter is set up: `flutter doctor`
3. App is built: `flutter build`

### LLM generates incomplete code

**Solutions:**
- Increase `max_tokens` in the code
- Simplify your requirements
- Run generation again
- Use a more capable model (e.g., GPT-4)

### "Rate limit exceeded" error

**Cause:** Too many API calls

**Solution:**
- Wait a few minutes
- Check your API usage
- Upgrade your API plan

### Generated app is different each time

This is normal! LLMs generate slightly different code each time. For consistency:
- Save specifications
- Use same prompts
- Keep generated code

## Workflow Questions

### Can I skip steps?

No, the workflow is sequential. Each step builds on previous ones. However, you can:
- Accept defaults quickly
- Skip optional customizations
- Use Ctrl+C to exit anytime

### Can I resume if interrupted?

Currently, no. If interrupted, restart from the beginning. Future versions may add resume capability.

### Can I save my specifications?

Yes! All intermediate files are saved in `output/`:
- `idea.json`
- `theme.json`
- `specification.json`
- `specification_final.json`
- `folder_structure.json`

### How do I generate multiple apps?

Run the workflow multiple times:
```bash
python oneday_app.py  # First app
python oneday_app.py  # Second app
python oneday_app.py  # Third app
```

Each generates a separate app in `output/`.

## Advanced Usage

### Can I customize the prompts?

Yes! Edit prompts in:
- `oneday_app.py`: Workflow prompts
- `app_generator.py`: Code generation prompts

### Can I add a new LLM provider?

Yes! See ARCHITECTURE.md for instructions. You'll need to:
1. Implement initialization
2. Implement generation method
3. Add configuration

### Can I create custom themes?

Yes! Edit `theme_selector.py` and add to the `THEMES` dictionary:
```python
"4": {
    "name": "My Custom Theme",
    "colors": { ... },
    # ...
}
```

### Can I modify the folder structure?

Yes! Edit `folder_structure.py` to customize:
- Folder layout
- Generated files
- Templates

### Can I use this in CI/CD?

Possible but not recommended. OneDayApp is interactive. For CI/CD:
- Pre-generate specs
- Use non-interactive mode (custom implementation)
- Or use traditional Flutter CI/CD

## Best Practices

### How can I get better results?

1. **Be specific with ideas**:
   - Bad: "shopping app"
   - Good: "grocery shopping app with barcode scanner and recipe suggestions"

2. **Choose appropriate theme**:
   - Match theme to app purpose
   - Consider target audience

3. **Review specifications carefully**:
   - Specifications guide generation
   - Fix issues early

4. **Start simple**:
   - 3-5 core features
   - Simple data models
   - Expand after generation

### Should I commit generated code to git?

Yes! But first:
1. Review the code
2. Remove unused files
3. Initialize git in the app directory
4. Create `.gitignore` (already generated)

### How should I structure my project after generation?

Keep the generated structure! It follows Flutter best practices:
```
lib/
  models/      - Data
  screens/     - UI
  widgets/     - Reusable UI
  services/    - Logic
  constants/   - Config
```

## Contributing

### How can I contribute?

See CONTRIBUTING.md for details. Areas that need help:
- Adding LLM providers
- Improving code generation
- Adding tests
- Documentation
- Bug fixes

### I found a bug. What should I do?

1. Check if it's already reported
2. Create a GitHub issue with:
   - Description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment

### Can I request features?

Yes! Create a GitHub issue with:
- Feature description
- Use case
- Why it's useful

## Comparison

### OneDayApp vs Manual Development?

**OneDayApp:**
- ✅ Fast initial setup
- ✅ Consistent structure
- ✅ Best practices included
- ⚠️ Requires customization
- ⚠️ Learning curve for workflow

**Manual:**
- ⚠️ Slower initial setup
- ⚠️ Structure varies
- ✅ Full control from start
- ✅ No dependencies on external services

### OneDayApp vs Flutter Templates?

**OneDayApp:**
- ✅ AI-generated based on requirements
- ✅ Customized to your app
- ✅ Multiple themes
- ⚠️ Requires API keys

**Templates:**
- ⚠️ Generic structure
- ⚠️ Not customized
- ✅ No API needed
- ✅ Instant

### OneDayApp vs No-Code Platforms?

**OneDayApp:**
- ✅ Full code control
- ✅ No platform lock-in
- ✅ Free and open-source
- ⚠️ Requires coding knowledge

**No-Code:**
- ⚠️ Limited customization
- ⚠️ Platform lock-in
- ⚠️ Ongoing costs
- ✅ No coding needed

## Support

### Where can I get help?

1. **Documentation**: Start here
   - README.md
   - USAGE.md
   - QUICKSTART.md
   - This FAQ

2. **Demo**: Run without API keys
   ```bash
   python example_demo.py
   ```

3. **GitHub Issues**: For bugs and features

4. **Community**: (Coming soon)
   - Discord server
   - Discussions

### Is there commercial support?

Currently, no. OneDayApp is community-supported. Consider:
- Hiring Flutter developers
- Using professional services
- Contributing improvements

## License and Legal

### What's the license?

MIT License - very permissive:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

### Can I use generated apps commercially?

Yes! The generated code is yours. You can:
- Sell the apps
- Use in commercial products
- Modify as needed
- Keep proprietary

### What about the AI-generated code?

Based on LLM provider policies:
- **OpenAI**: You own the output
- **Anthropic**: You own the output

Check current provider terms for confirmation.

## Still Have Questions?

- 📖 Check the [documentation](README.md)
- 🐛 Open a [GitHub Issue](https://github.com/massil30/OneDayApp/issues)
- 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md)
- 💡 Read [EXAMPLES.md](EXAMPLES.md)

Happy app building! 🚀
