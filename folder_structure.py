"""
Folder Structure Generator for OneDayApp.
Creates Flutter app folder structure based on specifications.
"""

import os
from pathlib import Path
from typing import Dict, List


class FolderStructureGenerator:
    """Generates Flutter app folder structure."""

    def generate(self, spec: Dict) -> Dict:
        """Generate folder structure based on specification."""
        app_name = spec.get('app_name', 'my_flutter_app').lower().replace(' ', '_')
        
        structure = {
            app_name: {
                "lib": {
                    "models": [],
                    "screens": [],
                    "widgets": [],
                    "services": [],
                    "utils": [],
                    "constants": ["colors.dart", "strings.dart", "themes.dart"],
                    "files": ["main.dart"]
                },
                "assets": {
                    "images": [],
                    "fonts": [],
                    "icons": []
                },
                "test": {
                    "widget_test": [],
                    "unit_test": [],
                    "integration_test": []
                },
                "android": {
                    "app": {
                        "src": {
                            "main": ["AndroidManifest.xml"]
                        }
                    }
                },
                "ios": {
                    "Runner": ["Info.plist"]
                },
                "files": [
                    "pubspec.yaml",
                    "README.md",
                    ".gitignore",
                    "analysis_options.yaml"
                ]
            }
        }
        
        # Add screen files based on features
        if 'features' in spec:
            features = spec.get('features', [])
            for i, feature in enumerate(features[:5]):  # Limit to 5 main features
                screen_name = self._feature_to_screen_name(feature)
                structure[app_name]["lib"]["screens"].append(f"{screen_name}_screen.dart")
        
        # Add model files if data models are specified
        if 'data_models' in spec:
            models = spec.get('data_models', [])
            for model in models[:5]:  # Limit to 5 main models
                model_name = self._clean_name(model)
                structure[app_name]["lib"]["models"].append(f"{model_name}.dart")
        
        return structure

    def create_folders(self, structure: Dict, base_path: Path):
        """Create actual folders and files on disk."""
        base_path.mkdir(parents=True, exist_ok=True)
        self._create_recursive(structure, base_path)

    def _create_recursive(self, structure: Dict, current_path: Path):
        """Recursively create folders and files."""
        for key, value in structure.items():
            if key == "files":
                # Create files in current directory
                for filename in value:
                    filepath = current_path / filename
                    if not filepath.exists():
                        self._create_initial_file(filepath)
            else:
                # Create directory
                dir_path = current_path / key
                dir_path.mkdir(exist_ok=True)
                
                if isinstance(value, dict):
                    # Recursively create subdirectories
                    self._create_recursive(value, dir_path)
                elif isinstance(value, list):
                    # Create files in this directory
                    for filename in value:
                        filepath = dir_path / filename
                        if not filepath.exists():
                            self._create_initial_file(filepath)

    def _create_initial_file(self, filepath: Path):
        """Create initial file with basic content."""
        filename = filepath.name
        
        if filename == "main.dart":
            content = self._get_main_dart_template()
        elif filename == "pubspec.yaml":
            content = self._get_pubspec_template(filepath.parent.name)
        elif filename == "README.md":
            content = self._get_readme_template(filepath.parent.name)
        elif filename == ".gitignore":
            content = self._get_gitignore_template()
        elif filename == "analysis_options.yaml":
            content = self._get_analysis_options_template()
        elif filename.endswith('.dart'):
            content = self._get_dart_file_template(filename)
        else:
            content = f"// {filename}\n"
        
        filepath.write_text(content)

    def _feature_to_screen_name(self, feature: str) -> str:
        """Convert feature name to screen file name."""
        # Remove special characters and convert to snake_case
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

    def _get_main_dart_template(self) -> str:
        """Get main.dart template."""
        return '''import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
'''

    def _get_pubspec_template(self, app_name: str) -> str:
        """Get pubspec.yaml template."""
        return f'''name: {app_name}
description: A Flutter application built with OneDayApp.
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
  
  # assets:
  #   - assets/images/
  
  # fonts:
  #   - family: Roboto
  #     fonts:
  #       - asset: assets/fonts/Roboto-Regular.ttf
'''

    def _get_readme_template(self, app_name: str) -> str:
        """Get README.md template."""
        return f'''# {app_name.replace('_', ' ').title()}

A Flutter application built with OneDayApp.

## Getting Started

1. Install dependencies:
```bash
flutter pub get
```

2. Run the app:
```bash
flutter run
```

## Project Structure

- `lib/`: Main application code
  - `models/`: Data models
  - `screens/`: Screen widgets
  - `widgets/`: Reusable widgets
  - `services/`: Business logic and API services
  - `utils/`: Utility functions
  - `constants/`: App constants
- `assets/`: Images, fonts, and other assets
- `test/`: Test files

## Requirements

- Flutter SDK: >=3.0.0
- Dart SDK: >=3.0.0

## License

This project is licensed under the MIT License.
'''

    def _get_gitignore_template(self) -> str:
        """Get .gitignore template."""
        return '''# Miscellaneous
*.class
*.log
*.pyc
*.swp
.DS_Store
.atom/
.buildlog/
.history
.svn/
migrate_working_dir/

# IntelliJ related
*.iml
*.ipr
*.iws
.idea/

# Flutter/Dart/Pub related
**/doc/api/
**/ios/Flutter/.last_build_id
.dart_tool/
.flutter-plugins
.flutter-plugins-dependencies
.packages
.pub-cache/
.pub/
/build/

# Symbolication related
app.*.symbols

# Obfuscation related
app.*.map.json

# Android Studio
.gradle
/local.properties
/.idea/workspace.xml
/.idea/libraries
.DS_Store
/build
/captures
.cxx

# iOS
**/ios/**/*.mode1v3
**/ios/**/*.mode2v3
**/ios/**/*.moved-aside
**/ios/**/*.pbxuser
**/ios/**/*.perspectivev3
**/ios/**/*sync/
**/ios/**/.sconsign.dblite
**/ios/**/.tags*
**/ios/**/.vagrant/
**/ios/**/DerivedData/
**/ios/**/Icon?
**/ios/**/Pods/
**/ios/**/.symlinks/
**/ios/**/profile
**/ios/**/xcuserdata
**/ios/.generated/
**/ios/Flutter/.last_build_id
**/ios/Flutter/App.framework
**/ios/Flutter/Flutter.framework
**/ios/Flutter/Flutter.podspec
**/ios/Flutter/Generated.xcconfig
**/ios/Flutter/ephemeral/
**/ios/Flutter/app.flx
**/ios/Flutter/app.zip
**/ios/Flutter/flutter_assets/
**/ios/Flutter/flutter_export_environment.sh
**/ios/ServiceDefinitions.json
**/ios/Runner/GeneratedPluginRegistrant.*

# Web
lib/generated_plugin_registrant.dart

# Coverage
coverage/

# Exceptions to above rules.
!**/ios/**/default.mode1v3
!**/ios/**/default.mode2v3
!**/ios/**/default.pbxuser
!**/ios/**/default.perspectivev3
'''

    def _get_analysis_options_template(self) -> str:
        """Get analysis_options.yaml template."""
        return '''include: package:flutter_lints/flutter.yaml

linter:
  rules:
    prefer_const_constructors: true
    prefer_const_literals_to_create_immutables: true
    prefer_final_fields: true
    unnecessary_const: true
    unnecessary_new: true
'''

    def _get_dart_file_template(self, filename: str) -> str:
        """Get template for Dart files."""
        class_name = self._filename_to_classname(filename)
        return f'''// {filename}

/// TODO: Implement {class_name}
class {class_name} {{
  // Add your code here
}}
'''

    def _filename_to_classname(self, filename: str) -> str:
        """Convert filename to class name."""
        name = filename.replace('.dart', '')
        parts = name.split('_')
        return ''.join(part.capitalize() for part in parts)
