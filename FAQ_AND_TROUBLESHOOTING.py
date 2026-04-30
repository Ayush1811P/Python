"""
FREQUENTLY ASKED QUESTIONS & TROUBLESHOOTING GUIDE
"""

FAQs = {
    "installation": {
        "title": "Installation & Setup",
        "questions": [
            {
                "q": "Do I need Python 3.8+?",
                "a": "Yes. Older Python versions won't work. Check with: python --version"
            },
            {
                "q": "How do I install dependencies?",
                "a": "Run: pip install -r requirements_agent.txt"
            },
            {
                "q": "What if pip doesn't work?",
                "a": "Try: pip3 install -r requirements_agent.txt (or python -m pip install)"
            },
            {
                "q": "Do I need all the demo files?",
                "a": "No, only ai_agent.py is required. Others are optional helpers."
            }
        ]
    },
    
    "openai_setup": {
        "title": "OpenAI API Setup",
        "questions": [
            {
                "q": "How do I get an OpenAI API key?",
                "a": "Visit https://platform.openai.com/api-keys and create a new key. Add it to .env"
            },
            {
                "q": "What's the cost?",
                "a": "GPT-4 costs ~$0.03 per 1K input tokens, $0.06 per 1K output. Start with free credits."
            },
            {
                "q": "Can I use GPT-3.5 instead of GPT-4?",
                "a": "Yes! Edit ai_agent.py line 135: self.model = 'gpt-3.5-turbo' (cheaper, faster)"
            },
            {
                "q": "Do I need an OpenAI account?",
                "a": "Yes. Sign up at https://platform.openai.com"
            },
            {
                "q": "What if my API key is invalid?",
                "a": "Check: 1) Key is from API keys page (not dashboard), 2) Key hasn't expired, 3) Key in .env has no spaces"
            }
        ]
    },
    
    "gmail_setup": {
        "title": "Gmail Configuration",
        "questions": [
            {
                "q": "How do I setup Gmail for sending emails?",
                "a": """
                1. Enable 2-factor authentication: https://support.google.com/accounts/answer/185839
                2. Visit: https://myaccount.google.com/apppasswords
                3. Select 'Mail' and 'Windows Computer'
                4. Generate and copy the 16-character password
                5. Add to .env as SENDER_PASSWORD
                """
            },
            {
                "q": "What if 'App Passwords' option doesn't appear?",
                "a": "Your account needs 2-factor authentication enabled. Enable it first."
            },
            {
                "q": "Can I use non-Gmail addresses?",
                "a": "Yes, but configure SMTP_SERVER, IMAP_SERVER, and SMTP_PORT accordingly."
            },
            {
                "q": "Is my password secure?",
                "a": "Yes. The app password is different from your Gmail password and can be revoked anytime."
            },
            {
                "q": "Why does email sending fail?",
                "a": "Check: 1) SENDER_EMAIL is correct, 2) SENDER_PASSWORD is app password (not Gmail password), 3) 2FA is enabled"
            }
        ]
    },
    
    "usage": {
        "title": "Using the Agent",
        "questions": [
            {
                "q": "How do I start the agent?",
                "a": "Run: python ai_agent.py"
            },
            {
                "q": "What commands can I use?",
                "a": "Any natural language! Examples: 'Create a task', 'Send an email', 'List my tasks'"
            },
            {
                "q": "Do I need to give exact details?",
                "a": "No. You can say 'Send an email about the project' and agent fills in details if needed."
            },
            {
                "q": "How do I exit the agent?",
                "a": "Type 'quit' or 'exit' or press Ctrl+C"
            },
            {
                "q": "Can I run multiple agents?",
                "a": "Yes, each AIAgent() instance is independent. Create multiple in separate processes."
            },
            {
                "q": "How do I see my conversation history?",
                "a": "The agent maintains history in conversation_history. Modify the code to print or save it."
            }
        ]
    },
    
    "tasks": {
        "title": "Task Management",
        "questions": [
            {
                "q": "Where are my tasks stored?",
                "a": "Currently in-memory (RAM). They're lost when the agent stops. To persist, add database integration."
            },
            {
                "q": "Can I use tasks across multiple agent instances?",
                "a": "No, each agent has its own task list. Share via database for multi-instance support."
            },
            {
                "q": "How do I format task IDs?",
                "a": "Any string works: 'task_001', 'review_budget', 'meeting_john', etc."
            },
            {
                "q": "What task statuses exist?",
                "a": "'pending', 'in_progress', 'completed' (you can add more if needed)"
            },
            {
                "q": "Can I bulk delete tasks?",
                "a": "Not directly, but you can modify the code to add a bulk delete function."
            }
        ]
    },
    
    "troubleshooting": {
        "title": "Common Issues",
        "questions": [
            {
                "q": "Agent doesn't respond?",
                "a": "Check: 1) Internet connection, 2) OPENAI_API_KEY is valid, 3) No firewall blocking"
            },
            {
                "q": "Error: 'ModuleNotFoundError: No module named openai'",
                "a": "Run: pip install openai"
            },
            {
                "q": "Error: 'OPENAI_API_KEY not found'",
                "a": "Create .env file with: OPENAI_API_KEY=sk-... (copy from platform.openai.com)"
            },
            {
                "q": "Email sending fails silently",
                "a": "Check SENDER_EMAIL and SENDER_PASSWORD in .env. Review .env is in correct directory."
            },
            {
                "q": "Agent ignores my requests",
                "a": "Try: 1) Rephrase naturally, 2) Be more specific, 3) Check system prompt in chat() method"
            },
            {
                "q": "Too many API calls = high costs?",
                "a": "Use gpt-3.5-turbo instead of gpt-4, or set token limits in OpenAI API call"
            }
        ]
    },
    
    "advanced": {
        "title": "Advanced Usage",
        "questions": [
            {
                "q": "How do I add a new tool?",
                "a": """
                1. Add tool definition to AIAgent.__init__() in tools list
                2. Implement the function in appropriate Manager class
                3. Add handler in process_tool_call() method
                4. Test with agent.chat('Your command')
                """
            },
            {
                "q": "How do I persist tasks to a database?",
                "a": """
                Replace TaskManager's dict with database queries:
                - Replace self.tasks dict with self.db connection
                - Update create_task(), list_tasks(), etc to use SQL
                - Add database initialization code
                """
            },
            {
                "q": "Can I deploy as a web API?",
                "a": """
                Yes! Use Flask:
                from flask import Flask, request
                @app.post('/chat')
                def chat():
                    msg = request.json['message']
                    return {'response': agent.chat(msg)}
                """
            },
            {
                "q": "How do I integrate with Slack/Discord?",
                "a": """
                1. Create webhook endpoint
                2. Receive messages from Slack/Discord
                3. Pass to agent.chat()
                4. Send response back via webhook
                See deployment options in ARCHITECTURE.txt
                """
            },
            {
                "q": "Can I run this on a server?",
                "a": "Yes! Deploy to: AWS Lambda, Google Cloud, Azure, Heroku, VPS, Docker, etc."
            }
        ]
    },
    
    "performance": {
        "title": "Performance & Optimization",
        "questions": [
            {
                "q": "Why is the agent slow?",
                "a": "Slowness = network latency to OpenAI. Use gpt-3.5-turbo for faster responses."
            },
            {
                "q": "How can I reduce costs?",
                "a": """
                1. Use gpt-3.5-turbo (3x cheaper than gpt-4)
                2. Reduce conversation history length
                3. Cache frequently used templates
                4. Batch requests instead of one-by-one
                """
            },
            {
                "q": "Can I run this offline?",
                "a": "No, needs OpenAI API. Use Ollama for local models (slower, free, privacy)"
            },
            {
                "q": "How many concurrent users can it handle?",
                "a": "As many as your OpenAI API quota allows. Each chat() call uses one API request."
            }
        ]
    },
    
    "data_privacy": {
        "title": "Security & Privacy",
        "questions": [
            {
                "q": "Is my data sent to OpenAI?",
                "a": "Yes, your messages are sent to OpenAI for processing. Review their privacy policy."
            },
            {
                "q": "Should I commit .env to git?",
                "a": "NO! .env contains secrets. Add to .gitignore. Use environment variables in production."
            },
            {
                "q": "Is my Gmail password safe?",
                "a": "Yes. Use app password (not Gmail password). Can be revoked anytime."
            },
            {
                "q": "Can I run this without internet?",
                "a": "No, needs OpenAI API. You can switch to local LLMs if needed."
            }
        ]
    }
}


QUICK FIXES:
════════════════════════════════════════════════════════════════════════════════

| Problem | Quick Fix |
|---------|-----------|
| No response | `pip install openai` |
| API error | Check OPENAI_API_KEY in .env |
| Email fails | Verify SENDER_EMAIL/PASSWORD, enable Gmail 2FA |
| Slow agent | Use gpt-3.5-turbo instead of gpt-4 |
| ImportError | Run `pip install -r requirements_agent.txt` |
| FileNotFoundError | Ensure .env exists, run from correct directory |


GETTING HELP:
════════════════════════════════════════════════════════════════════════════════

1. Run diagnostics: python quick_start.py
2. Run tests: python test_agent.py
3. Check logs: Review error messages carefully
4. Read docs: README_AGENT.md has detailed info
5. Try demos: python demo_agent.py to see working examples
6. Check code: ai_agent.py is well-commented


═════════════════════════════════════════════════════════════════════════════════
"""

def display_faq():
    """Interactive FAQ viewer"""
    print("\n" + "="*80)
    print("AI AGENT - FREQUENTLY ASKED QUESTIONS")
    print("="*80)
    
    categories = list(FAQs.keys())
    
    print("\n📚 Available Topics:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {FAQs[cat]['title']}")
    print("  0. Show All")
    print("  q. Quit\n")
    
    while True:
        try:
            choice = input("Select topic (0-8 or q): ").strip().lower()
            
            if choice == "q":
                print("\nGoodbye!\n")
                break
            
            if choice == "0":
                for cat in categories:
                    print_category(cat)
                break
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(categories):
                    print_category(categories[idx])
                else:
                    print("Invalid selection")
            except ValueError:
                print("Invalid input")
        
        except KeyboardInterrupt:
            print("\n\nExiting...\n")
            break


def print_category(category):
    """Print a category of FAQs"""
    data = FAQs[category]
    print("\n" + "="*80)
    print(f"  {data['title'].upper()}")
    print("="*80)
    
    for i, item in enumerate(data['questions'], 1):
        q = item['q']
        a = item['a']
        
        # Format answer
        if isinstance(a, str) and '\n' in a:
            a_lines = [line.strip() for line in a.split('\n') if line.strip()]
            a = '\n       '.join(a_lines)
        
        print(f"\n  Q{i}: {q}")
        print(f"  A:  {a}\n")


if __name__ == "__main__":
    display_faq()
