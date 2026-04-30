#!/usr/bin/env python3
"""
LOCAL MODEL QUICK START - Ollama + TinyLlama Setup Guide
"""

import subprocess
import sys
import os

def check_ollama_installed():
    """Check if Ollama is installed"""
    try:
        subprocess.run(["ollama", "--version"], capture_output=True, check=True)
        print("✅ Ollama is installed")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("❌ Ollama is not installed")
        print("\n📥 Download from: https://ollama.ai")
        print("   Then run: ollama serve (in a separate terminal)")
        return False

def check_ollama_running():
    """Check if Ollama server is running"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            print("✅ Ollama server is running")
            return True
    except:
        pass
    
    print("❌ Ollama server is not running")
    print("\n🚀 Start Ollama in a new terminal:")
    print("   ollama serve")
    return False

def check_model_installed():
    """Check if tinyllama is installed"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        models = response.json().get("models", [])
        model_names = [m["name"].split(":")[0] for m in models]
        
        if "tinyllama" in model_names:
            print("✅ tinyllama model is installed")
            return True
    except:
        pass
    
    print("❌ tinyllama model is not installed")
    print("\n📥 Download tinyllama:")
    print("   ollama pull tinyllama")
    print("   (This takes a few minutes, ~600MB)")
    return False

def check_python_packages():
    """Check required Python packages"""
    try:
        import dotenv
        import requests
        print("✅ All Python packages installed")
        return True
    except ImportError as e:
        print(f"❌ Missing Python package: {e}")
        print("\n📦 Install requirements:")
        print("   pip install -r requirements_agent.txt")
        return False

def check_env_file():
    """Check .env file"""
    if not os.path.exists(".env"):
        print("❌ .env file not found")
        print("\n📝 Create .env file:")
        print("   cp .env.example .env")
        return False
    
    print("✅ .env file exists")
    return True

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("🚀 LOCAL MODEL AI AGENT - QUICK START")
    print("="*60 + "\n")
    
    checks = [
        ("Ollama Installed", check_ollama_installed),
        ("Ollama Running", check_ollama_running),
        ("TinyLlama Model", check_model_installed),
        ("Python Packages", check_python_packages),
        (".env File", check_env_file),
    ]
    
    passed = 0
    for name, check in checks:
        print(f"\n🔍 Checking {name}...")
        try:
            if check():
                passed += 1
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "="*60)
    
    if passed == len(checks):
        print("\n✅ All checks passed! Ready to run.\n")
        print("Start the agent with:")
        print("  python ai_agent.py\n")
    else:
        print(f"\n⚠️  {len(checks) - passed} setup step(s) needed.\n")
        print("Follow the instructions above, then run:")
        print("  python local_model_setup.py\n")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
