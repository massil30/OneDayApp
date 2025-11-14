"""
App Generator module for OneDayApp.
Generates complete Flutter application code using LLM.
"""

from pathlib import Path
from typing import Dict
from llm_provider import LLMProvider


class AppGenerator:
    """Generates Flutter application code."""

    def __init__(self, llm: LLMProvider):
        self.llm = llm

    def generate_app(self, spec: Dict, folder_structure: Dict, app_dir: Path):
        """Generate complete application code."""
        # Generate main.dart with proper app structure
        self._generate_main_file(spec, app_dir)
        
        # Generate screens based on features
        self._generate_screens(spec, app_dir)
        
        # Generate models if specified
        self._generate_models(spec, app_dir)
        
        # Generate constants
        self._generate_constants(spec, app_dir)
        
        # Update pubspec.yaml with dependencies
        self._update_pubspec(spec, app_dir)

    def _generate_main_file(self, spec: Dict, app_dir: Path):
        """Generate main.dart file."""
        app_name = spec.get('app_name', 'My Flutter App')
        theme_info = spec.get('theme', {})
        
        prompt = f"""Generate a Flutter main.dart file for an app with the following specifications:

App Name: {app_name}
Specification: {spec}

The main.dart should:
1. Initialize the app with proper MaterialApp setup
2. Include basic routing if multiple screens are needed
3. Apply the theme configuration
4. Follow Flutter best practices
5. Include proper imports

Provide only the Dart code without any explanations."""

        code = self.llm.generate(prompt, max_tokens=2000)
        
        # Clean up the code
        code = self._extract_code(code)
        
        main_file = app_dir / "lib" / "main.dart"
        main_file.write_text(code)

    def _generate_screens(self, spec: Dict, app_dir: Path):
        """Generate screen files based on features."""
        features = spec.get('features', [])
        screens_dir = app_dir / "lib" / "screens"
        screens_dir.mkdir(parents=True, exist_ok=True)
        
        for i, feature in enumerate(features[:5]):  # Limit to 5 screens
            screen_name = self._feature_to_screen_name(feature)
            
            prompt = f"""Generate a Flutter screen widget for the following feature:

Feature: {feature}
App Context: {spec.get('description', '')}

The screen should:
1. Be a StatefulWidget or StatelessWidget as appropriate
2. Include basic UI elements for the feature
3. Follow Material Design guidelines
4. Include proper error handling
5. Be ready to use with minimal modifications

Provide only the Dart code without explanations."""

            code = self.llm.generate(prompt, max_tokens=2000)
            code = self._extract_code(code)
            
            screen_file = screens_dir / f"{screen_name}_screen.dart"
            screen_file.write_text(code)

    def _generate_models(self, spec: Dict, app_dir: Path):
        """Generate model files."""
        models = spec.get('data_models', [])
        if not models:
            return
        
        models_dir = app_dir / "lib" / "models"
        models_dir.mkdir(parents=True, exist_ok=True)
        
        for model in models[:5]:  # Limit to 5 models
            model_name = self._clean_name(model)
            
            prompt = f"""Generate a Flutter/Dart model class for:

Model: {model}
Context: {spec.get('description', '')}

The model should:
1. Include appropriate fields
2. Have a constructor
3. Include toJson() and fromJson() methods
4. Follow Dart naming conventions
5. Include proper documentation

Provide only the Dart code without explanations."""

            code = self.llm.generate(prompt, max_tokens=1500)
            code = self._extract_code(code)
            
            model_file = models_dir / f"{model_name}.dart"
            model_file.write_text(code)

    def _generate_constants(self, spec: Dict, app_dir: Path):
        """Generate constants files."""
        constants_dir = app_dir / "lib" / "constants"
        constants_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate colors.dart
        theme_info = spec.get('theme', {})
        colors_content = self._generate_colors_file(theme_info)
        (constants_dir / "colors.dart").write_text(colors_content)
        
        # Generate strings.dart
        strings_content = self._generate_strings_file(spec)
        (constants_dir / "strings.dart").write_text(strings_content)
        
        # Generate themes.dart
        themes_content = self._generate_themes_file(theme_info)
        (constants_dir / "themes.dart").write_text(themes_content)

    def _generate_colors_file(self, theme_info: Dict) -> str:
        """Generate colors.dart content."""
        colors = theme_info.get('colors', {})
        
        return f"""import 'package:flutter/material.dart';

/// App color constants
class AppColors {{
  static const Color primary = Color(0xFF{colors.get('primary', '#2C3E50').replace('#', '')});
  static const Color secondary = Color(0xFF{colors.get('secondary', '#3498DB').replace('#', '')});
  static const Color accent = Color(0xFF{colors.get('accent', '#E74C3C').replace('#', '')});
  static const Color background = Color(0xFF{colors.get('background', '#FFFFFF').replace('#', '')});
  static const Color text = Color(0xFF{colors.get('text', '#2C3E50').replace('#', '')});
  
  static const Color success = Color(0xFF27AE60);
  static const Color error = Color(0xFFE74C3C);
  static const Color warning = Color(0xFFF39C12);
  static const Color info = Color(0xFF3498DB);
}}
"""

    def _generate_strings_file(self, spec: Dict) -> str:
        """Generate strings.dart content."""
        app_name = spec.get('app_name', 'My Flutter App')
        
        return f"""/// App string constants
class AppStrings {{
  static const String appName = '{app_name}';
  static const String appDescription = '{spec.get('description', '')}';
  
  // Common strings
  static const String ok = 'OK';
  static const String cancel = 'Cancel';
  static const String save = 'Save';
  static const String delete = 'Delete';
  static const String edit = 'Edit';
  static const String loading = 'Loading...';
  static const String error = 'An error occurred';
  static const String retry = 'Retry';
  
  // Add more app-specific strings here
}}
"""

    def _generate_themes_file(self, theme_info: Dict) -> str:
        """Generate themes.dart content."""
        return """import 'package:flutter/material.dart';
import 'colors.dart';

/// App theme configuration
class AppTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      primaryColor: AppColors.primary,
      colorScheme: ColorScheme.light(
        primary: AppColors.primary,
        secondary: AppColors.secondary,
      ),
      scaffoldBackgroundColor: AppColors.background,
      appBarTheme: const AppBarTheme(
        backgroundColor: AppColors.primary,
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      textTheme: const TextTheme(
        bodyLarge: TextStyle(color: AppColors.text),
        bodyMedium: TextStyle(color: AppColors.text),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: AppColors.primary,
          foregroundColor: Colors.white,
        ),
      ),
      useMaterial3: true,
    );
  }
  
  static ThemeData get darkTheme {
    return ThemeData.dark().copyWith(
      primaryColor: AppColors.primary,
      colorScheme: ColorScheme.dark(
        primary: AppColors.primary,
        secondary: AppColors.secondary,
      ),
    );
  }
}
"""

    def _update_pubspec(self, spec: Dict, app_dir: Path):
        """Update pubspec.yaml with necessary dependencies."""
        pubspec_file = app_dir / "pubspec.yaml"
        if not pubspec_file.exists():
            return
        
        # Read current content
        content = pubspec_file.read_text()
        
        # Add common dependencies if not present
        common_deps = [
            "  http: ^1.1.0",
            "  provider: ^6.1.0",
        ]
        
        # Check if dependencies section exists and add if needed
        if "dependencies:" in content:
            lines = content.split('\n')
            dep_index = next(i for i, line in enumerate(lines) if "dependencies:" in line)
            
            # Add after flutter dependency
            insert_index = dep_index + 2
            for dep in common_deps:
                if dep.strip().split(':')[0] not in content:
                    lines.insert(insert_index, dep)
                    insert_index += 1
            
            content = '\n'.join(lines)
            pubspec_file.write_text(content)

    def _extract_code(self, response: str) -> str:
        """Extract code from LLM response."""
        # Remove markdown code blocks if present
        if "```dart" in response:
            start = response.find("```dart") + 7
            end = response.rfind("```")
            if end > start:
                response = response[start:end]
        elif "```" in response:
            start = response.find("```") + 3
            end = response.rfind("```")
            if end > start:
                response = response[start:end]
        
        return response.strip()

    def _feature_to_screen_name(self, feature: str) -> str:
        """Convert feature name to screen file name."""
        name = feature.lower()
        name = ''.join(c if c.isalnum() or c.isspace() else '' for c in name)
        name = '_'.join(name.split())
        return name

    def _clean_name(self, name: str) -> str:
        """Clean name for file naming."""
        name = name.lower()
        name = ''.join(c if c.isalnum() or c.isspace() else '' for c in name)
        name = '_'.join(name.split())
        return name
