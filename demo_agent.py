"""
Demo script showing how to use the AI Agent programmatically
Run this to see the agent in action without manual input
"""

import os
from dotenv import load_dotenv
from ai_agent import AIAgent

load_dotenv()


def demo_basic_tasks():
    """Demo: Create and manage tasks"""
    print("\n" + "="*60)
    print("DEMO 1: Task Management")
    print("="*60)
    
    agent = AIAgent()
    
    # Create a task
    print("\n📋 User: Create a task to review the Q1 budget report")
    response = agent.chat("Create a task called 'task_001' titled 'Review Q1 Budget Report' with description 'Analyze spending and prepare summary for management'")
    print(f"Agent: {response}\n")
    
    # Create another task
    print("📋 User: Create another task for following up with the client")
    response = agent.chat("Create a task 'task_002' to 'Follow Up with Client ABC' - 'Send status update and get feedback on proposal'")
    print(f"Agent: {response}\n")
    
    # List all tasks
    print("📋 User: Show me all my pending tasks")
    response = agent.chat("List all my pending tasks")
    print(f"Agent: {response}\n")


def demo_email_templates():
    """Demo: Use email templates"""
    print("\n" + "="*60)
    print("DEMO 2: Email Templates")
    print("="*60)
    
    agent = AIAgent()
    
    print("\n📧 User: What email templates are available?")
    response = agent.chat("Get me email templates for a meeting request")
    print(f"Agent: {response}\n")
    
    print("📧 User: Get a follow-up email template")
    response = agent.chat("Show me a follow-up email template")
    print(f"Agent: {response}\n")


def demo_draft_email():
    """Demo: Draft emails without sending"""
    print("\n" + "="*60)
    print("DEMO 3: Draft Emails")
    print("="*60)
    
    agent = AIAgent()
    
    print("\n📧 User: Draft an email to john@example.com about the project")
    response = agent.chat("Draft an email to john@example.com with subject 'Project Update' and body 'Hi John, I wanted to update you on the project status...'")
    print(f"Agent: {response}\n")


def demo_combined_workflow():
    """Demo: Combined task + email workflow"""
    print("\n" + "="*60)
    print("DEMO 4: Combined Workflow")
    print("="*60)
    
    agent = AIAgent()
    
    print("\n🔄 User: Create a task and draft an update email")
    response = agent.chat("Create a task 'send_report' titled 'Send Monthly Report' and draft an email to reports@company.com about sending the monthly metrics")
    print(f"Agent: {response}\n")
    
    print("🔄 User: Show all my tasks")
    response = agent.chat("List all my tasks")
    print(f"Agent: {response}\n")


def demo_task_updates():
    """Demo: Update task statuses"""
    print("\n" + "="*60)
    print("DEMO 5: Task Status Updates")
    print("="*60)
    
    agent = AIAgent()
    
    # Create initial tasks
    print("\n📝 Creating sample tasks...")
    agent.chat("Create task 'demo_task_1' titled 'Review Documentation' with description 'Go through API docs'")
    agent.chat("Create task 'demo_task_2' titled 'Code Review' with description 'Review PR from team'")
    
    # List pending tasks
    print("\n✓ Current pending tasks:")
    response = agent.chat("Show all pending tasks")
    print(f"Agent: {response}\n")
    
    # Mark one as completed
    print("📝 Marking first task as completed...")
    response = agent.chat("Mark demo_task_1 as completed")
    print(f"Agent: {response}\n")
    
    # List remaining
    print("✓ Updated tasks:")
    response = agent.chat("List all my tasks")
    print(f"Agent: {response}\n")


def demo_conversation_flow():
    """Demo: Multi-turn conversation"""
    print("\n" + "="*60)
    print("DEMO 6: Multi-Turn Conversation")
    print("="*60)
    
    agent = AIAgent()
    
    exchanges = [
        "What can you do for me?",
        "Create a task to prepare a presentation",
        "What tasks do I have?",
        "Can you draft a professional email to my manager?",
        "Great! What other email templates do you have?"
    ]
    
    for i, user_msg in enumerate(exchanges, 1):
        print(f"\n({i}) 👤 You: {user_msg}")
        response = agent.chat(user_msg)
        print(f"   🤖 Agent: {response}")


def main():
    """Run all demos"""
    print("\n" + "█"*60)
    print("█ AI AGENT - TASK AUTOMATION DEMO")
    print("█"*60)
    
    print("\n⚠️  Note: This demo uses conversation to control the agent.")
    print("For email sending to work, ensure credentials are set in .env")
    
    demos = {
        "1": ("Task Management", demo_basic_tasks),
        "2": ("Email Templates", demo_email_templates),
        "3": ("Draft Emails", demo_draft_email),
        "4": ("Combined Workflow", demo_combined_workflow),
        "5": ("Task Status Updates", demo_task_updates),
        "6": ("Multi-Turn Conversation", demo_conversation_flow),
        "0": ("Run All Demos", None)
    }
    
    print("\nAvailable Demos:")
    for key, (name, _) in demos.items():
        if key != "0":
            print(f"  {key}. {name}")
    print("  0. Run All Demos")
    print("  q. Quit")
    
    while True:
        try:
            choice = input("\nSelect demo (0-6, or q to quit): ").strip()
            
            if choice == "q":
                print("\nExiting. Goodbye!")
                break
            
            if choice == "0":
                demo_basic_tasks()
                demo_email_templates()
                demo_draft_email()
                demo_combined_workflow()
                demo_task_updates()
                demo_conversation_flow()
                print("\n✅ All demos completed!")
                break
            
            if choice in demos and choice != "0":
                name, func = demos[choice]
                if func:
                    print(f"\n▶️  Running: {name}")
                    func()
                    print(f"\n✅ Demo completed!")
                else:
                    print("Invalid selection")
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nDemo interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Make sure OPENAI_API_KEY is set in .env file")


if __name__ == "__main__":
    main()
