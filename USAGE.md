# OneDayApp Usage Guide

## Quick Start

### 1. First Time Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### 2. Run the Workflow

```bash
python oneday_app.py
```

## Detailed Workflow Steps

### Step 1: Idea Generation

The LLM will generate an app idea. You can:
- Provide context about what kind of app you want
- Let the LLM decide completely (press Enter with no input)
- Regenerate if you don't like the first idea

**Example Input:**
```
What kind of app are you interested in? food delivery for students
```

**Example Output:**
```
App Name: CampusEats
Description: A food delivery app specifically designed for college students...
Target Users: College students, university faculty
Key Features:
  • Quick order from campus restaurants
  • Split bills with roommates
  • Meal plan integration
  • Campus location tracking
```

### Step 2: Theme Selection & Inspiration

Choose from three carefully crafted design themes:

#### Modern Minimalist
Best for: Professional apps, productivity tools, business applications
- Clean lines and generous whitespace
- Sophisticated color palette
- Focus on content over decoration

#### Material Design
Best for: Android-first apps, social media, communication tools
- Google's proven design system
- Bold colors and clear hierarchy
- Rich interactions and animations

#### Appetizing / Food-focused
Best for: Food delivery, recipe apps, restaurant apps
- Warm, inviting colors
- Emphasis on imagery
- Friendly, approachable interface

The LLM will also provide design inspiration including:
- Current design trends
- Color palette suggestions
- UI/UX best practices
- Reference apps

### Step 3: Specification Generation

The LLM creates a comprehensive specification document including:

1. **App Overview**
   - Purpose and goals
   - Target audience
   - Key value propositions

2. **Technical Requirements**
   - Flutter version
   - Required packages
   - Platform support (iOS/Android)

3. **Feature Specifications**
   - Detailed feature descriptions
   - User stories
   - Acceptance criteria

4. **Screen Layouts**
   - Screen hierarchy
   - Navigation flow
   - UI components per screen

5. **Data Models**
   - Entity definitions
   - Relationships
   - Data validation rules

6. **API Requirements**
   - Endpoints needed (if applicable)
   - Data formats
   - Authentication

7. **Design Guidelines**
   - Color usage
   - Typography
   - Spacing and layout rules

8. **Testing Requirements**
   - Unit tests
   - Widget tests
   - Integration tests

### Step 4: Review & Update Specification

You have three options:

#### Option 1: Keep Current Specification
If you're satisfied, proceed to the next step.

#### Option 2: Edit Specification Manually
The specification is saved to `output/specification.md`. You can:
1. Edit the file in your preferred text editor
2. Save your changes
3. Press Enter to continue

#### Option 3: Request AI Updates
Provide specific feedback like:
- "Add a dark mode feature"
- "Include user authentication"
- "Remove the payment feature"
- "Add offline support"

The LLM will update the specification based on your feedback.

### Step 5: Folder Structure Creation

The system generates a complete Flutter project structure:

```
my_app/
├── lib/
│   ├── models/          # Data models
│   ├── screens/         # Screen widgets
│   ├── widgets/         # Reusable widgets
│   ├── services/        # Business logic
│   ├── utils/           # Helper functions
│   ├── constants/       # App constants
│   └── main.dart        # Entry point
├── assets/
│   ├── images/          # Image assets
│   ├── fonts/           # Custom fonts
│   └── icons/           # Icon files
├── test/
│   ├── widget_test/     # Widget tests
│   ├── unit_test/       # Unit tests
│   └── integration_test/# Integration tests
├── pubspec.yaml         # Dependencies
└── README.md            # Project documentation
```

### Step 6: Full App Generation

The system generates:

1. **main.dart**: Complete app entry point with:
   - MaterialApp configuration
   - Theme setup
   - Initial routing

2. **Screen Files**: One file per feature:
   - StatefulWidget or StatelessWidget
   - Basic UI implementation
   - Proper imports and structure

3. **Model Files**: Data model classes with:
   - Properties
   - Constructors
   - JSON serialization
   - Documentation

4. **Constants**: Theme-specific values:
   - colors.dart: Color constants
   - strings.dart: Text constants
   - themes.dart: Theme configuration

5. **Updated pubspec.yaml**: With common dependencies:
   - http: For API calls
   - provider: For state management

## Advanced Usage

### Custom Idea Input

Provide detailed context for better results:

```
What kind of app are you interested in?
A fitness tracking app for elderly users that focuses on simple exercises
and medication reminders. Should have large fonts and voice guidance.
```

### Specification Modifications

Be specific when requesting changes:

```
What changes would you like to make?
Add a feature for caregivers to remotely monitor the user's activities.
Include emergency contact quick dial button on the home screen.
Make the UI support multiple languages (English, Spanish, Chinese).
```

### Multiple Iterations

You can run the workflow multiple times:
- Generate different ideas
- Try different themes
- Iterate on specifications

Each run creates a new project in the `output/` directory.

## Testing Generated Apps

### 1. Initial Setup

```bash
cd output/your_app_name
flutter pub get
```

### 2. Run on Emulator/Device

```bash
flutter run
```

### 3. Run Tests

```bash
flutter test
```

### 4. Build for Production

```bash
# Android
flutter build apk

# iOS
flutter build ios
```

## Tips for Best Results

### 1. Be Specific with Context
Instead of "a shopping app", try:
"A grocery shopping app for busy parents that suggests recipes based on items in their cart and dietary restrictions"

### 2. Choose the Right Theme
- B2B/Professional → Modern Minimalist
- Consumer/Social → Material Design
- Food/Hospitality → Appetizing/Food-focused

### 3. Review Specifications Carefully
The specification is the blueprint. A detailed spec = better generated code.

### 4. Iterate on the Specification
Don't hesitate to request changes. It's easier to fix the spec than the code.

### 5. Start Simple
For your first project, keep it simple:
- 3-5 main features
- 2-4 screens
- Minimal external dependencies

## Common Issues and Solutions

### Issue: LLM generates incomplete code
**Solution**: Increase `max_tokens` in the LLM calls (edit `app_generator.py`)

### Issue: Generated app has compilation errors
**Solution**: 
- Run `flutter pub get`
- Check for missing imports
- Verify Flutter SDK version compatibility

### Issue: Theme colors not applied correctly
**Solution**: The theme is in `lib/constants/`. Review and adjust color values.

### Issue: Want to add more features later
**Solution**: 
- Update the specification
- Re-run just the generation steps
- Or manually add features following the existing structure

## Next Steps After Generation

1. **Review the Code**: Understand what was generated
2. **Run the App**: Test basic functionality
3. **Customize**: Add your specific business logic
4. **Add Assets**: Replace placeholder images with real ones
5. **Implement APIs**: Connect to your backend services
6. **Test Thoroughly**: Write additional tests
7. **Polish UI**: Fine-tune the user interface
8. **Deploy**: Build and release your app

## Getting Help

- Check the main README.md for setup issues
- Review generated code comments for guidance
- Open an issue on GitHub for bugs
- Consult Flutter documentation for Flutter-specific questions

## Best Practices

1. **Version Control**: Initialize git in your generated project
2. **Documentation**: Update the generated README with your specifics
3. **Code Review**: Review all generated code before using in production
4. **Security**: Add proper authentication and data validation
5. **Testing**: Expand the generated tests with your own
6. **Performance**: Profile and optimize as needed

Happy app building! 🚀
