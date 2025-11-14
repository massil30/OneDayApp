# OneDayApp Examples

This document provides examples of apps you can create with OneDayApp and the expected output.

## Example 1: Fitness Tracker App

### Input

```
What kind of app are you interested in?
> fitness tracking app for gym workouts

Theme Selection: Material Design
```

### Generated Structure

```
fittracker_pro/
├── lib/
│   ├── main.dart
│   ├── models/
│   │   ├── user.dart
│   │   ├── workout.dart
│   │   └── exercise.dart
│   ├── screens/
│   │   ├── workout_logging_and_tracking_screen.dart
│   │   ├── nutrition_diary_with_calorie_counter_screen.dart
│   │   ├── progress_photos_and_measurements_screen.dart
│   │   ├── exercise_library_with_instructions_screen.dart
│   │   └── social_features_to_share_achievements_screen.dart
│   ├── widgets/
│   ├── services/
│   ├── utils/
│   ├── constants/
│   │   ├── colors.dart
│   │   ├── strings.dart
│   │   └── themes.dart
│   └── main.dart
├── assets/
│   ├── images/
│   ├── fonts/
│   └── icons/
├── test/
│   ├── widget_test/
│   ├── unit_test/
│   └── integration_test/
├── pubspec.yaml
└── README.md
```

### Key Features Generated

- Workout logging interface
- Nutrition tracking
- Progress visualization
- Exercise database
- Social sharing capabilities

## Example 2: Recipe Management App

### Input

```
What kind of app are you interested in?
> recipe app for home cooks with meal planning

Theme Selection: Appetizing / Food-focused
```

### Generated Structure

```
recipebox/
├── lib/
│   ├── main.dart
│   ├── models/
│   │   ├── recipe.dart
│   │   ├── ingredient.dart
│   │   └── meal_plan.dart
│   ├── screens/
│   │   ├── recipe_browser_screen.dart
│   │   ├── meal_planner_screen.dart
│   │   ├── shopping_list_screen.dart
│   │   └── cooking_mode_screen.dart
│   ├── constants/
│   │   ├── colors.dart      # Warm, appetizing colors
│   │   ├── strings.dart
│   │   └── themes.dart
│   └── ...
├── pubspec.yaml
└── README.md
```

### Theme Colors Applied

```dart
// Appetizing / Food-focused theme
AppColors.primary = Color(0xFFFF6B35);    // Warm orange
AppColors.secondary = Color(0xFFF7931E);  // Golden yellow
AppColors.accent = Color(0xFFC1121F);     // Deep red
AppColors.background = Color(0xFFFFF8F3); // Cream
```

## Example 3: Task Management App

### Input

```
What kind of app are you interested in?
> productivity app for task management and team collaboration

Theme Selection: Modern Minimalist
```

### Generated Structure

```
taskmaster/
├── lib/
│   ├── main.dart
│   ├── models/
│   │   ├── task.dart
│   │   ├── project.dart
│   │   └── team_member.dart
│   ├── screens/
│   │   ├── task_list_screen.dart
│   │   ├── project_overview_screen.dart
│   │   ├── team_collaboration_screen.dart
│   │   └── calendar_view_screen.dart
│   ├── widgets/
│   │   └── (reusable widgets generated here)
│   ├── services/
│   │   └── (API services generated here)
│   └── constants/
│       ├── colors.dart      # Clean, professional colors
│       ├── strings.dart
│       └── themes.dart
└── ...
```

### Theme Colors Applied

```dart
// Modern Minimalist theme
AppColors.primary = Color(0xFF2C3E50);    // Dark blue-gray
AppColors.secondary = Color(0xFF3498DB);  // Bright blue
AppColors.accent = Color(0xFFE74C3C);     // Red accent
AppColors.background = Color(0xFFFFFFFF); // Pure white
```

## Example 4: Food Delivery App

### Input

```
What kind of app are you interested in?
> food delivery app for students on campus

Theme Selection: Appetizing / Food-focused

Specification Updates:
- Add split payment feature
- Include real-time order tracking
- Add campus location integration
```

### Generated Features

1. **Restaurant Browser**
   - Campus restaurants listing
   - Menu with images
   - Ratings and reviews

2. **Order Management**
   - Cart with real-time updates
   - Split payment interface
   - Order tracking map

3. **User Profile**
   - Saved addresses
   - Payment methods
   - Order history

4. **Campus Integration**
   - Building/dorm selection
   - Delivery zones
   - Campus-specific offers

## Example 5: Budget Tracking App

### Input

```
What kind of app are you interested in?
> personal finance app for budget tracking and expense management

Theme Selection: Modern Minimalist
```

### Generated Components

#### Models
```dart
// Generated in lib/models/

class Transaction {
  final String id;
  final double amount;
  final String category;
  final DateTime date;
  final String description;
  // ... with toJson() and fromJson()
}

class Budget {
  final String id;
  final String category;
  final double limit;
  final double spent;
  // ...
}
```

#### Screens
```dart
// Generated in lib/screens/

// expense_tracking_screen.dart
class ExpenseTrackingScreen extends StatefulWidget { ... }

// budget_overview_screen.dart
class BudgetOverviewScreen extends StatefulWidget { ... }

// reports_and_analytics_screen.dart
class ReportsAndAnalyticsScreen extends StatefulWidget { ... }
```

#### Constants
```dart
// Generated in lib/constants/colors.dart

class AppColors {
  static const Color primary = Color(0xFF2C3E50);
  static const Color secondary = Color(0xFF3498DB);
  static const Color success = Color(0xFF27AE60);
  static const Color error = Color(0xFFE74C3C);
  // ... more colors
}
```

## Generated File Examples

### main.dart Structure

```dart
import 'package:flutter/material.dart';
import 'constants/themes.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Your App Name',
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      home: const HomeScreen(),
    );
  }
}
```

### pubspec.yaml Structure

```yaml
name: your_app_name
description: A Flutter application built with OneDayApp.
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2
  http: ^1.1.0              # Added by OneDayApp
  provider: ^6.1.0          # Added by OneDayApp

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
```

## Customization Examples

### Adding a New Screen Manually

After generation, you can add screens:

```dart
// lib/screens/new_feature_screen.dart

import 'package:flutter/material.dart';
import '../constants/colors.dart';

class NewFeatureScreen extends StatelessWidget {
  const NewFeatureScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('New Feature'),
        backgroundColor: AppColors.primary,
      ),
      body: Center(
        child: Text(
          'Your new feature here',
          style: TextStyle(color: AppColors.text),
        ),
      ),
    );
  }
}
```

### Extending Generated Models

```dart
// Add methods to generated models

class User {
  final String id;
  final String name;
  final String email;
  
  // Generated constructor and JSON methods
  
  // Add your custom methods
  bool get isVerified => email.isNotEmpty;
  
  String get displayName => name.isEmpty ? 'Guest' : name;
}
```

## Tips for Best Results

### 1. Specific App Ideas Lead to Better Code

❌ Poor: "Make a shopping app"
✅ Good: "Create a grocery shopping app with recipe suggestions and shared lists"

### 2. Choose Appropriate Themes

- **Modern Minimalist**: Professional, B2B, productivity apps
- **Material Design**: Social, communication, general-purpose apps
- **Appetizing/Food-focused**: Food, hospitality, lifestyle apps

### 3. Review and Refine Specifications

The generated spec can be refined:
- Add specific features
- Clarify data models
- Define user flows
- Specify API requirements

### 4. Start with Core Features

For best results, start with 3-5 core features:
```
Good First App:
- User registration
- Main feed/dashboard
- Create/edit items
- View details
- Settings
```

## Real-World Usage Scenarios

### Scenario 1: MVP for Startup

```
Goal: Build MVP in one day to show investors
Strategy:
  1. Focus on 2-3 core features
  2. Use Material Design for familiarity
  3. Keep data models simple
  4. Generate quickly, refine later
```

### Scenario 2: Learning Flutter

```
Goal: Learn Flutter by building real apps
Strategy:
  1. Generate multiple small apps
  2. Study the generated code
  3. Modify and experiment
  4. Try all three themes
```

### Scenario 3: Hackathon Project

```
Goal: Create functional prototype in hours
Strategy:
  1. Clear idea from the start
  2. Request specific features in spec
  3. Let AI handle boilerplate
  4. Focus on custom logic
```

### Scenario 4: Client Prototype

```
Goal: Show client a working prototype
Strategy:
  1. Gather requirements clearly
  2. Match theme to client brand
  3. Use spec refinement for feedback
  4. Polish generated UI
```

## Generated vs Manual Code

### What OneDayApp Generates Well

✅ Project structure
✅ Boilerplate code
✅ Basic screens
✅ Theme configuration
✅ Model classes
✅ File organization

### What You Should Add

🔧 Business logic
🔧 API integration
🔧 Complex state management
🔧 Custom animations
🔧 Error handling
🔧 Testing

## Next Steps After Generation

1. **Immediate (Day 1)**
   - Run the app
   - Test basic navigation
   - Review generated code

2. **Short-term (Week 1)**
   - Add business logic
   - Implement API calls
   - Add error handling
   - Write tests

3. **Medium-term (Month 1)**
   - Polish UI/UX
   - Add advanced features
   - Performance optimization
   - Prepare for release

## Conclusion

OneDayApp provides a solid foundation for your Flutter apps. The examples above show what's possible. Your creativity and requirements will shape the final product.

For more examples and inspiration, check out the demo:
```bash
python example_demo.py
```

Happy building! 🚀
