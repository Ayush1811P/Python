#!/usr/bin/env python3
"""
QUICK START GUIDE - AI Task Automation Agent

This script guides you through initial setup and testing.
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Verify Python 3.8+"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        print(f"   You have: Python {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required = ["openai", "dotenv"]
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("\n   Install with: pip install -r requirements_agent.txt")
        return False
    
    print("✅ All required packages installed")
    return True

def check_env_file():
    """Check .env file exists and has API key"""
    if not Path(".env").exists():
        print("❌ .env file not found")
        print("   Copy .env.example to .env: cp .env.example .env")
        print("   Then edit .env with your OpenAI API key")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
    
    if "your_openai_api_key_here" in content or "sk-" not in content:
        print("⚠️  .env file exists but OPENAI_API_KEY not set")
        print("   Edit .env and add your API key from https://platform.openai.com/api-keys")
        return False
    
    print("✅ .env file configured")
    return True

def test_openai_connection():
    """Test OpenAI API connection"""
    try:
        from openai import OpenAI
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Quick test call
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Say 'Hello'"}],
            max_tokens=5
        )
        
        print("✅ OpenAI API connection successful")
        return True
    except Exception as e:
        print(f"❌ OpenAI API connection failed: {str(e)}")
        return False

def main():
    """Run setup checks"""
    print("\n" + "="*60)
    print("AI AGENT - QUICK START")
    print("="*60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Environment File", check_env_file),
        ("OpenAI API", test_openai_connection),
    ]
    
    passed = 0
    for name, check in checks:
        print(f"\n🔍 Checking {name}...")
        try:
            if check():
                passed += 1
            else:
                pass
        except Exception as e:
            print(f"❌ Check failed: {str(e)}")
    
    print("\n" + "="*60)
    
    if passed == len(checks):
        print(f"\n✅ All checks passed! Ready to start.\n")
        print("Start the agent with:")
        print("  python ai_agent.py\n")
        print("Or run demos with:")
        print("  python demo_agent.py\n")
    else:
        print(f"\n⚠️  {len(checks) - passed} check(s) failed")
        print("Please fix the issues above and try again.\n")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
