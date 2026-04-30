# AI Task Automation Agent

A fully working AI agent built with OpenAI GPT-4 that automates email and communication tasks.

## Features

✅ **Email Management**
- Send emails programmatically
- Draft emails without sending
- Pre-built email templates (meeting requests, follow-ups, thank-yous)

✅ **Task Management**
- Create tasks with due dates
- List and filter tasks by status
- Update task status (pending, in_progress, completed)
- Delete tasks

✅ **AI-Powered Automation**
- Natural language conversation
- Autonomous tool usage via GPT-4 function calling
- Intelligent task execution

## Prerequisites

- Python 3.8+
- OpenAI API key (for GPT-4 access)
- Gmail account with app password (for email sending)

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements_agent.txt
```

Or manually:
```bash
pip install openai>=1.3.0 python-dotenv>=1.0.0 requests>=2.31.0
```

### 2. Setup Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
# Get from https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-...

# Gmail credentials for sending emails
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password

# Email servers (default to Gmail)
IMAP_SERVER=imap.gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Gmail App Password Setup:**
1. Enable 2-factor authentication on your Gmail account
2. Go to https://myaccount.google.com/apppasswords
3. Select "Mail" and "Windows Computer" (or your device)
4. Generate and copy the 16-character password
5. Paste it as `SENDER_PASSWORD` in `.env`

## Usage

### Run the Agent

```bash
python ai_agent.py
```

The agent will start an interactive conversation. Try commands like:

**Email Examples:**
```
"Send an email to john@example.com about the project meeting tomorrow"
"Create a meeting request email for alice@company.com"
"Draft a thank you email to my manager"
```

**Task Examples:**
```
"Create a task to review the budget report"
"Show me all my pending tasks"
"Mark task-123 as completed"
"What tasks do I have due this week?"
```

**Mixed Examples:**
```
"Create a task for following up with Bob, then send him an email about the proposal"
"List my tasks and send a status update email to the team"
```

## Architecture

### Components

1. **AIAgent** - Main orchestrator
   - Manages conversation history
   - Coordinates tool calls
   - Interfaces with OpenAI API

2. **EmailManager** - Email operations
   - Send emails via SMTP
   - Draft emails
   - Email templates

3. **TaskManager** - Task operations
   - Create, read, update, delete tasks
   - Filter by status
   - In-memory storage

### Tool Calling Flow

```
User Input
    ↓
OpenAI GPT-4 (analyzes intent, decides which tools to use)
    ↓
Process Tool Calls (send_email, create_task, etc.)
    ↓
Return Results to Model
    ↓
Generate Natural Response
    ↓
Output to User
```

## API Tools Available

The agent can autonomously use these tools:

- `send_email(recipient, subject, body)` - Send an email
- `draft_email(recipient, subject, body)` - Create a draft
- `get_email_template(template_type)` - Get email templates
- `create_task(task_id, title, description, due_date)` - Create task
- `list_tasks(status)` - List tasks
- `update_task_status(task_id, new_status)` - Update status
- `delete_task(task_id)` - Delete task

## Examples

### Example 1: Send Email via Conversation

```
You: Send an email to alice@company.com reminding her about the meeting tomorrow

Agent: I'll send that email for you right away.
[Sends email]

Agent: ✓ Email sent to alice@company.com about the meeting reminder.
```

### Example 2: Create Task & Send Notification

```
You: Create a task to review the quarterly report and email me a summary

Agent: I'll create the task and send you a summary email.
[Creates task, sends email]

Agent: Done! I've created task #1 and sent you a summary email.
```

### Example 3: Manage Tasks

```
You: What tasks do I have pending?

Agent: You have 3 pending tasks:
1. Review quarterly report
2. Schedule team meeting
3. Prepare presentation

You: Mark the first one as completed

Agent: Task updated! The review task is now marked as completed.
```

## Customization

### Add Custom Tools

Edit `AIAgent.__init__()` to add more tools:

```python
{
    "type": "function",
    "function": {
        "name": "custom_tool",
        "description": "What this tool does",
        "parameters": {...}
    }
}
```

Then implement in `process_tool_call()`:

```python
elif tool_name == "custom_tool":
    return self.my_function(**tool_input)
```

### Modify System Prompt

Edit the `system_prompt` in the `chat()` method to change agent behavior.

### Use Different Models

Change `self.model = "gpt-4"` to:
- `"gpt-4-turbo-preview"` (faster, cheaper)
- `"gpt-3.5-turbo"` (faster, cheapest)

## Troubleshooting

**"Invalid API key"**
- Verify `OPENAI_API_KEY` is set correctly in `.env`
- Check key is from https://platform.openai.com/api-keys

**"Failed to send email"**
- Verify Gmail credentials
- Ensure 2FA is enabled and app password is generated
- Check SMTP settings are correct

**"Module not found"**
- Run `pip install -r requirements_agent.txt`
- Verify Python 3.8+

## License

MIT License - Use freely in your projects

## Next Steps

- Integrate with calendar API for scheduling
- Add Slack/Teams notifications
- Store tasks in database instead of memory
- Add multi-user support
- Implement task persistence with SQLite
