#!/usr/bin/env python3
"""
Setup validation script for OneDayApp.
Tests that all dependencies and configuration are correct.
"""

import sys
import os
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_status(message, status="info"):
    """Print a status message with color."""
    if status == "success":
        print(f"{GREEN}✓{RESET} {message}")
    elif status == "error":
        print(f"{RED}✗{RESET} {message}")
    elif status == "warning":
        print(f"{YELLOW}⚠{RESET} {message}")
    else:
        print(f"{BLUE}ℹ{RESET} {message}")


def check_python_version():
    """Check if Python version is compatible."""
    print_status("Checking Python version...", "info")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - OK", "success")
        return True
    else:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} - Need 3.8+", "error")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    print_status("\nChecking dependencies...", "info")
    
    required = {
        'rich': 'Rich',
        'dotenv': 'python-dotenv',
        'yaml': 'PyYAML',
    }
    
    optional = {
        'openai': 'OpenAI',
        'anthropic': 'Anthropic',
    }
    
    all_ok = True
    
    # Check required packages
    for module, name in required.items():
        try:
            __import__(module)
            print_status(f"{name} - Installed", "success")
        except ImportError:
            print_status(f"{name} - Missing (required)", "error")
            all_ok = False
    
    # Check optional packages
    for module, name in optional.items():
        try:
            __import__(module)
            print_status(f"{name} - Installed", "success")
        except ImportError:
            print_status(f"{name} - Not installed (optional)", "warning")
    
    return all_ok


def check_env_file():
    """Check if .env file exists and has required keys."""
    print_status("\nChecking environment configuration...", "info")
    
    env_file = Path('.env')
    
    if not env_file.exists():
        print_status(".env file not found", "warning")
        print_status("  Run: cp .env.example .env", "info")
        return False
    
    print_status(".env file exists", "success")
    
    # Check for API keys
    content = env_file.read_text()
    
    has_openai = 'OPENAI_API_KEY=' in content
    has_anthropic = 'ANTHROPIC_API_KEY=' in content
    
    if has_openai or has_anthropic:
        if has_openai:
            print_status("OpenAI API key configured", "success")
        if has_anthropic:
            print_status("Anthropic API key configured", "success")
        return True
    else:
        print_status("No API keys configured", "warning")
        print_status("  Add OPENAI_API_KEY or ANTHROPIC_API_KEY to .env", "info")
        return False


def check_project_structure():
    """Check if all required files exist."""
    print_status("\nChecking project structure...", "info")
    
    required_files = [
        'oneday_app.py',
        'llm_provider.py',
        'theme_selector.py',
        'folder_structure.py',
        'app_generator.py',
        'requirements.txt',
        'README.md',
    ]
    
    all_ok = True
    for file in required_files:
        if Path(file).exists():
            print_status(f"{file} - Found", "success")
        else:
            print_status(f"{file} - Missing", "error")
            all_ok = False
    
    return all_ok


def test_imports():
    """Test importing main modules."""
    print_status("\nTesting module imports...", "info")
    
    modules = [
        'llm_provider',
        'theme_selector',
        'folder_structure',
        'app_generator',
    ]
    
    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print_status(f"{module} - OK", "success")
        except Exception as e:
            print_status(f"{module} - Error: {str(e)}", "error")
            all_ok = False
    
    return all_ok


def check_flutter():
    """Check if Flutter is installed (optional)."""
    print_status("\nChecking Flutter installation (optional)...", "info")
    
    try:
        import subprocess
        result = subprocess.run(
            ['flutter', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print_status(f"Flutter installed - {version_line}", "success")
            return True
        else:
            print_status("Flutter not found", "warning")
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print_status("Flutter not installed (needed to run generated apps)", "warning")
        print_status("  Install: https://docs.flutter.dev/get-started/install", "info")
        return False
    except Exception as e:
        print_status(f"Error checking Flutter: {str(e)}", "warning")
        return False


def main():
    """Run all validation checks."""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}OneDayApp Setup Validation{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    results = {
        'Python Version': check_python_version(),
        'Dependencies': check_dependencies(),
        'Environment': check_env_file(),
        'Project Structure': check_project_structure(),
        'Module Imports': test_imports(),
        'Flutter': check_flutter(),
    }
    
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Summary{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    critical_checks = ['Python Version', 'Dependencies', 'Project Structure', 'Module Imports']
    optional_checks = ['Environment', 'Flutter']
    
    critical_passed = all(results[check] for check in critical_checks)
    optional_passed = sum(results[check] for check in optional_checks)
    
    if critical_passed:
        print_status("Core setup: READY", "success")
    else:
        print_status("Core setup: INCOMPLETE", "error")
        print_status("Please fix the errors above", "info")
    
    if results['Environment']:
        print_status("API configuration: READY", "success")
    else:
        print_status("API configuration: NOT CONFIGURED", "warning")
        print_status("You can still run the demo without API keys", "info")
    
    if results['Flutter']:
        print_status("Flutter: READY", "success")
    else:
        print_status("Flutter: NOT INSTALLED", "warning")
        print_status("Install Flutter to run generated apps", "info")
    
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}Next Steps{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    if not results['Environment']:
        print_status("1. Configure API keys: cp .env.example .env", "info")
        print_status("2. Edit .env and add your OpenAI or Anthropic API key", "info")
    
    print_status("• Run demo: python example_demo.py", "info")
    
    if results['Environment']:
        print_status("• Generate an app: python oneday_app.py", "info")
    else:
        print_status("• After configuring API keys: python oneday_app.py", "info")
    
    print_status("• Read documentation: README.md, USAGE.md", "info")
    
    print()
    
    # Return exit code
    sys.exit(0 if critical_passed else 1)


if __name__ == "__main__":
    main()
