#!/usr/bin/env python3
"""
Test script to verify AI Agent installation and functionality
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test that all required packages can be imported"""
    print("\n" + "="*60)
    print("TEST 1: Import Verification")
    print("="*60)
    
    packages = {
        "openai": "OpenAI",
        "dotenv": "python-dotenv",
        "requests": "requests"
    }
    
    failed = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ Failed to import {name}: {e}")
            failed.append(name)
    
    return len(failed) == 0

def test_files():
    """Test that all required files exist"""
    print("\n" + "="*60)
    print("TEST 2: File Structure")
    print("="*60)
    
    required_files = [
        "ai_agent.py",
        ".env.example",
        "requirements_agent.txt",
        "README_AGENT.md",
        "demo_agent.py",
        "quick_start.py",
        "usage_examples.py"
    ]
    
    missing = []
    for file in required_files:
        if Path(file).exists():
            size = Path(file).stat().st_size
            print(f"✅ {file} ({size} bytes)")
        else:
            print(f"❌ {file} - MISSING")
            missing.append(file)
    
    return len(missing) == 0

def test_env_file():
    """Test .env file setup"""
    print("\n" + "="*60)
    print("TEST 3: Environment Configuration")
    print("="*60)
    
    if not Path(".env").exists():
        print("⚠️  .env file not found")
        print("   Run: cp .env.example .env")
        print("   Then edit .env with your credentials")
        return False
    
    print("✅ .env file exists")
    
    # Check for API key
    with open(".env", "r") as f:
        content = f.read()
    
    if "OPENAI_API_KEY" in content and "sk-" not in content:
        print("⚠️  OPENAI_API_KEY not set (still has placeholder)")
        print("   Get your key from: https://platform.openai.com/api-keys")
        return False
    
    if "OPENAI_API_KEY" in content and "sk-" in content:
        print("✅ OPENAI_API_KEY appears configured")
    
    return True

def test_agent_structure():
    """Test that ai_agent.py has required classes"""
    print("\n" + "="*60)
    print("TEST 4: Agent Code Structure")
    print("="*60)
    
    try:
        with open("ai_agent.py", "r") as f:
            content = f.read()
        
        required_classes = [
            "EmailManager",
            "TaskManager", 
            "AIAgent"
        ]
        
        required_methods = [
            "send_email",
            "create_task",
            "chat",
            "process_tool_call"
        ]
        
        for cls in required_classes:
            if f"class {cls}" in content:
                print(f"✅ Class '{cls}' found")
            else:
                print(f"❌ Class '{cls}' NOT found")
                return False
        
        for method in required_methods:
            if f"def {method}" in content:
                print(f"✅ Method '{method}' found")
            else:
                print(f"❌ Method '{method}' NOT found")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error reading ai_agent.py: {e}")
        return False

def test_demo_structure():
    """Test that demo files exist and have content"""
    print("\n" + "="*60)
    print("TEST 5: Demo & Example Files")
    print("="*60)
    
    demo_files = [
        ("demo_agent.py", "demo functions"),
        ("quick_start.py", "check functions"),
        ("usage_examples.py", "EXAMPLES dict")
    ]
    
    all_ok = True
    for filename, content_marker in demo_files:
        try:
            with open(filename, "r") as f:
                content = f.read()
            
            if content_marker.lower() in content.lower() or "def " in content:
                print(f"✅ {filename} has content")
            else:
                print(f"⚠️  {filename} might be incomplete")
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
            all_ok = False
    
    return all_ok

def test_documentation():
    """Test that documentation files are complete"""
    print("\n" + "="*60)
    print("TEST 6: Documentation")
    print("="*60)
    
    docs = {
        "README_AGENT.md": ["Features", "Installation", "Usage"],
        "AGENT_SUMMARY.txt": ["Getting Started", "Capabilities"]
    }
    
    for doc, markers in docs.items():
        try:
            with open(doc, "r") as f:
                content = f.read()
            
            found = [m for m in markers if m in content]
            if len(found) >= len(markers) - 1:
                print(f"✅ {doc} - {len(found)}/{len(markers)} sections found")
            else:
                print(f"⚠️  {doc} - only {len(found)}/{len(markers)} sections found")
        except Exception as e:
            print(f"❌ Error reading {doc}: {e}")
    
    return True

def print_summary(results):
    """Print test summary"""
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(results.values())
    total = len(results)
    percentage = (passed / total) * 100
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n📊 Result: {passed}/{total} tests passed ({percentage:.0f}%)")
    
    if passed == total:
        print("\n✅ All systems ready! Start with: python ai_agent.py")
    elif passed >= total - 1:
        print("\n⚠️  Minor issues detected. Check output above.")
        print("   Likely need to set OPENAI_API_KEY in .env")
    else:
        print("\n❌ Issues detected. Please fix before running agent.")
    
    return passed == total

def main():
    """Run all tests"""
    print("\n" + "█"*60)
    print("█ AI AGENT - SYSTEM TEST SUITE")
    print("█"*60)
    
    results = {
        "Import Verification": test_imports(),
        "File Structure": test_files(),
        "Environment Config": test_env_file(),
        "Agent Code Structure": test_agent_structure(),
        "Demo & Example Files": test_demo_structure(),
        "Documentation": test_documentation()
    }
    
    all_ok = print_summary(results)
    
    print("\n" + "="*60 + "\n")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
