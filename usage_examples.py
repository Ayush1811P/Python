"""
USAGE EXAMPLES & CONVERSATION GUIDE
Complete examples of how to use the AI Agent
"""

EXAMPLES = {
    "email_sending": {
        "title": "Sending Emails",
        "examples": [
            {
                "user": "Send an email to john@company.com with subject 'Meeting Tomorrow' and message about our 2pm meeting",
                "agent_response": "I'll send that email right away. [Email sent]",
                "notes": "Requires SENDER_EMAIL and SENDER_PASSWORD in .env"
            },
            {
                "user": "Email alice@example.com a reminder about the project deadline",
                "agent_response": "[Sends email]",
                "notes": "Agent will compose a professional reminder"
            },
            {
                "user": "Send a follow-up email to bob@client.com about our discussion last week",
                "agent_response": "[Sends email]",
                "notes": "Agent creates contextually appropriate follow-up"
            }
        ]
    },
    
    "email_drafting": {
        "title": "Drafting Emails (without sending)",
        "examples": [
            {
                "user": "Draft an email to my manager about a promotion opportunity",
                "agent_response": "I'll draft a professional email for you to review",
                "notes": "Use drafting to review before sending"
            },
            {
                "user": "Can you draft a thank you email to the interviewers?",
                "agent_response": "[Provides draft]",
                "notes": "Perfect for sensitive communications"
            }
        ]
    },
    
    "email_templates": {
        "title": "Using Email Templates",
        "examples": [
            {
                "user": "Get me a meeting request email template",
                "agent_response": "[Provides template with placeholders]",
                "notes": "Templates: meeting_request, follow_up, thank_you"
            },
            {
                "user": "Show me a follow-up email template",
                "agent_response": "[Template with Hi [NAME], I wanted to follow up...]",
                "notes": "Customize by replacing [PLACEHOLDER] values"
            },
            {
                "user": "Can you create a thank you email template?",
                "agent_response": "[Professional thank you template]",
                "notes": "Great starting point for customization"
            }
        ]
    },
    
    "task_creation": {
        "title": "Creating Tasks",
        "examples": [
            {
                "user": "Create a task to review the budget proposal",
                "agent_response": "[Creates task] Task 'review_budget' created",
                "notes": "Agent auto-generates task IDs"
            },
            {
                "user": "Add a task for preparing the presentation, due next Friday",
                "agent_response": "[Creates task with due date]",
                "notes": "Use natural dates like 'next Friday', '2024-05-15'"
            },
            {
                "user": "Create a task: 'client_meeting' - schedule meeting with ABC Corp",
                "agent_response": "[Task created]",
                "notes": "You can specify task IDs directly"
            }
        ]
    },
    
    "task_management": {
        "title": "Managing Tasks",
        "examples": [
            {
                "user": "List all my tasks",
                "agent_response": "[Shows all tasks with status]",
                "notes": "Shows pending, in_progress, and completed tasks"
            },
            {
                "user": "Show me my pending tasks",
                "agent_response": "[Lists only pending tasks]",
                "notes": "Filter by status: pending, in_progress, completed"
            },
            {
                "user": "What tasks do I have this week?",
                "agent_response": "[Lists tasks with upcoming due dates]",
                "notes": "Agent understands date-based filtering"
            }
        ]
    },
    
    "task_updates": {
        "title": "Updating Task Status",
        "examples": [
            {
                "user": "Mark task_001 as completed",
                "agent_response": "[Task status updated]",
                "notes": "Status: pending → in_progress → completed"
            },
            {
                "user": "Move the budget review to in_progress",
                "agent_response": "[Task status updated]",
                "notes": "Agent finds task by name or ID"
            },
            {
                "user": "Delete the old meeting task",
                "agent_response": "[Task deleted]",
                "notes": "Removes task from list"
            }
        ]
    },
    
    "combined_workflows": {
        "title": "Combined Tasks & Emails",
        "examples": [
            {
                "user": "Create a task to follow up with Sarah and send her an email about the proposal",
                "agent_response": "[Creates task AND sends email]",
                "notes": "Agent handles multi-step workflows"
            },
            {
                "user": "Add a task for the meeting with John and draft an agenda email",
                "agent_response": "[Task created + email drafted]",
                "notes": "Coordinates multiple actions automatically"
            },
            {
                "user": "List my tasks and send a status update email to the team",
                "agent_response": "[Shows tasks + sends summary email]",
                "notes": "Sequential workflow execution"
            }
        ]
    },
    
    "advanced_usage": {
        "title": "Advanced Patterns",
        "examples": [
            {
                "user": "Create tasks for all items on my project roadmap and email stakeholders about them",
                "agent_response": "[Multiple tasks + comprehensive email]",
                "notes": "Agent extracts items and creates tasks automatically"
            },
            {
                "user": "Draft personalized follow-up emails for all my pending tasks",
                "agent_response": "[Generates multiple contextual drafts]",
                "notes": "Perfect for bulk communications"
            },
            {
                "user": "What's my task status? Send a summary to my manager",
                "agent_response": "[Status overview + summary email]",
                "notes": "Automatic reporting workflow"
            }
        ]
    }
}


def print_section(category):
    """Print a category of examples"""
    data = EXAMPLES[category]
    print("\n" + "="*70)
    print(f"  {data['title'].upper()}")
    print("="*70)
    
    for i, example in enumerate(data['examples'], 1):
        print(f"\n  Example {i}:")
        print(f"  👤 User: {example['user']}")
        print(f"  🤖 Agent: {example['agent_response']}")
        if example.get('notes'):
            print(f"  ℹ️  Note: {example['notes']}")


def main():
    """Show all examples"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "AI AGENT - USAGE EXAMPLES GUIDE" + " "*23 + "║")
    print("╚" + "="*68 + "╝")
    
    categories = list(EXAMPLES.keys())
    
    print("\n📚 Available Topics:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {EXAMPLES[cat]['title']}")
    print("  0. Show All")
    print("  q. Quit")
    
    while True:
        try:
            choice = input("\nSelect topic (0-7 or q): ").strip().lower()
            
            if choice == "q":
                print("\nGoodbye!\n")
                break
            
            if choice == "0":
                for cat in categories:
                    print_section(cat)
                print("\n")
                break
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(categories):
                    print_section(categories[idx])
                else:
                    print("Invalid selection")
            except ValueError:
                print("Invalid input")
        
        except KeyboardInterrupt:
            print("\n\nExiting...\n")
            break


if __name__ == "__main__":
    main()
