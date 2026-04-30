"""
AI Task Automation Agent - Email/Communication Tasks
Handles email operations and communication tasks using Ollama (local model)
Uses tinyllama-1.1b-chat for local inference
"""

import os
import json
import smtplib
import requests
from typing import Optional, Any
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()


class EmailManager:
    """Handles email operations"""
    
    def __init__(self):
        self.sender_email = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
        self.sender_password = os.getenv("SENDER_PASSWORD", "your_app_password")
        self.imap_server = os.getenv("IMAP_SERVER", "imap.gmail.com")
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        
    def send_email(self, recipient: str, subject: str, body: str) -> dict:
        """Send an email"""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            return {
                "status": "success",
                "message": f"Email sent to {recipient}",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to send email: {str(e)}"
            }
    
    def draft_email(self, recipient: str, subject: str, body: str) -> dict:
        """Create a draft email without sending"""
        return {
            "status": "draft",
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "created_at": datetime.now().isoformat()
        }
    
    def get_email_template(self, template_type: str) -> dict:
        """Get a template for common email types"""
        templates = {
            "meeting_request": {
                "subject": "Meeting Request: [TOPIC]",
                "body": "Hi [NAME],\n\nI wanted to schedule a meeting to discuss [TOPIC].\n\nAvailable times: [TIMES]\n\nPlease let me know what works best for you.\n\nBest regards"
            },
            "follow_up": {
                "subject": "Follow Up: [TOPIC]",
                "body": "Hi [NAME],\n\nI wanted to follow up on our discussion about [TOPIC].\n\n[MESSAGE]\n\nLooking forward to hearing from you.\n\nBest regards"
            },
            "thank_you": {
                "subject": "Thank You",
                "body": "Hi [NAME],\n\nThank you for [ACTION/MEETING].\n\n[MESSAGE]\n\nI appreciate your time and effort.\n\nBest regards"
            }
        }
        return templates.get(template_type, {"error": f"Template '{template_type}' not found"})


class TaskManager:
    """Manages tasks and reminders"""
    
    def __init__(self):
        self.tasks = {}
    
    def create_task(self, task_id: str, title: str, description: str, due_date: Optional[str] = None) -> dict:
        """Create a new task"""
        self.tasks[task_id] = {
            "id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "pending",
            "created_at": datetime.now().isoformat()
        }
        return {"status": "success", "message": f"Task '{title}' created", "task": self.tasks[task_id]}
    
    def list_tasks(self, status: Optional[str] = None) -> dict:
        """List all tasks, optionally filtered by status"""
        tasks = list(self.tasks.values())
        if status:
            tasks = [t for t in tasks if t["status"] == status]
        return {"status": "success", "tasks": tasks, "count": len(tasks)}
    
    def update_task_status(self, task_id: str, new_status: str) -> dict:
        """Update task status"""
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = new_status
            return {"status": "success", "message": f"Task status updated to '{new_status}'"}
        return {"status": "error", "message": f"Task '{task_id}' not found"}
    
    def delete_task(self, task_id: str) -> dict:
        """Delete a task"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return {"status": "success", "message": f"Task '{task_id}' deleted"}
        return {"status": "error", "message": f"Task '{task_id}' not found"}


class AIAgent:
    """Main AI Agent for task automation using local Ollama model"""
    
    def __init__(self):
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model_name = os.getenv("LOCAL_MODEL", "tinyllama")
        self.email_manager = EmailManager()
        self.task_manager = TaskManager()
        self.conversation_history = []
        
        # Verify Ollama is running
        self._verify_ollama_connection()
        
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "send_email",
                    "description": "Send an email to a recipient",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient": {"type": "string", "description": "Email address of recipient"},
                            "subject": {"type": "string", "description": "Email subject"},
                            "body": {"type": "string", "description": "Email body content"}
                        },
                        "required": ["recipient", "subject", "body"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "draft_email",
                    "description": "Create a draft email without sending",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient": {"type": "string", "description": "Email address of recipient"},
                            "subject": {"type": "string", "description": "Email subject"},
                            "body": {"type": "string", "description": "Email body content"}
                        },
                        "required": ["recipient", "subject", "body"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_email_template",
                    "description": "Get a template for common email types",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "template_type": {
                                "type": "string",
                                "description": "Type of template: meeting_request, follow_up, thank_you"
                            }
                        },
                        "required": ["template_type"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "create_task",
                    "description": "Create a new task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "Unique task identifier"},
                            "title": {"type": "string", "description": "Task title"},
                            "description": {"type": "string", "description": "Task description"},
                            "due_date": {"type": "string", "description": "Due date (optional, format: YYYY-MM-DD)"}
                        },
                        "required": ["task_id", "title", "description"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "list_tasks",
                    "description": "List all tasks or filter by status",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "status": {"type": "string", "description": "Filter by status: pending, completed, in_progress"}
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "update_task_status",
                    "description": "Update the status of a task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "Task identifier"},
                            "new_status": {"type": "string", "description": "New status: pending, completed, in_progress"}
                        },
                        "required": ["task_id", "new_status"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "delete_task",
                    "description": "Delete a task",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "task_id": {"type": "string", "description": "Task identifier"}
                        },
                        "required": ["task_id"]
                    }
                }
            }
        ]
    
    def _verify_ollama_connection(self):
        """Check if Ollama is running and accessible"""
        try:
            response = requests.get(f"{self.ollama_base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                print(f"✓ Connected to Ollama at {self.ollama_base_url}")
                models = response.json().get("models", [])
                model_names = [m["name"].split(":")[0] for m in models]
                if self.model_name not in model_names:
                    print(f"⚠️  Model '{self.model_name}' not found locally")
                    print(f"   Available models: {', '.join(model_names)}")
                    print(f"   Pull it with: ollama pull {self.model_name}")
                else:
                    print(f"✓ Model '{self.model_name}' is available")
            else:
                raise Exception(f"HTTP {response.status_code}")
        except requests.exceptions.ConnectionError:
            raise Exception(
                f"Cannot connect to Ollama at {self.ollama_base_url}\n"
                "Make sure Ollama is running: ollama serve"
            )
        except Exception as e:
            raise Exception(f"Ollama error: {str(e)}")
    
    def process_tool_call(self, tool_name: str, tool_input: dict) -> Any:
        """Execute tool calls"""
        if tool_name == "send_email":
            return self.email_manager.send_email(**tool_input)
        elif tool_name == "draft_email":
            return self.email_manager.draft_email(**tool_input)
        elif tool_name == "get_email_template":
            return self.email_manager.get_email_template(**tool_input)
        elif tool_name == "create_task":
            return self.task_manager.create_task(**tool_input)
        elif tool_name == "list_tasks":
            return self.task_manager.list_tasks(**tool_input)
        elif tool_name == "update_task_status":
            return self.task_manager.update_task_status(**tool_input)
        elif tool_name == "delete_task":
            return self.task_manager.delete_task(**tool_input)
        else:
            return {"error": f"Unknown tool: {tool_name}"}
    
    def _extract_tool_calls(self, response_text: str) -> list:
        """Extract tool calls from model response (simple parsing)"""
        tool_calls = []
        
        # Look for tool calls in format: [TOOL_NAME](param1, param2...)
        import re
        pattern = r'\[(\w+)\]\s*\((.*?)\)'
        matches = re.finditer(pattern, response_text, re.DOTALL)
        
        for match in matches:
            tool_name = match.group(1)
            params_str = match.group(2)
            
            # Simple parameter parsing
            try:
                params_str = "{" + params_str.replace(", ", ", ") + "}"
                params = json.loads(params_str)
                tool_calls.append({"name": tool_name, "input": params})
            except:
                pass
        
        return tool_calls
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response from the local model"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        system_prompt = """You are a helpful task automation agent that specializes in email and communication tasks.
You can help users:
- Send and draft emails
- Manage tasks and reminders
- Get email templates for common scenarios
- Organize and track tasks by status

Available tools:
- send_email(recipient, subject, body) - Send an email
- draft_email(recipient, subject, body) - Create a draft email
- get_email_template(template_type) - Get email templates
- create_task(task_id, title, description, due_date) - Create a task
- list_tasks(status) - List tasks
- update_task_status(task_id, new_status) - Update task
- delete_task(task_id) - Delete a task

When you need to use tools, format them as: [TOOL_NAME](param1, param2)
Be helpful, professional, and proactive.
Keep responses concise and clear."""
        
        # Prepare messages for Ollama
        messages = [{"role": "system", "content": system_prompt}] + self.conversation_history
        
        try:
            # Call Ollama API
            response = requests.post(
                f"{self.ollama_base_url}/api/chat",
                json={
                    "model": self.model_name,
                    "messages": messages,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=120
            )
            
            if response.status_code != 200:
                return f"Error from Ollama: {response.status_code} - {response.text}"
            
            response_data = response.json()
            assistant_message = response_data.get("message", {}).get("content", "")
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except requests.exceptions.Timeout:
            return "Response timeout. The model is taking too long to respond. Try a simpler query."
        except requests.exceptions.ConnectionError:
            return f"Cannot connect to Ollama at {self.ollama_base_url}. Make sure it's running."
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """Main function to run the agent"""
    print("=" * 60)
    print("🤖 AI Task Automation Agent - Local Model Edition")
    print("   Using Ollama + TinyLlama")
    print("=" * 60)
    print("\nInitializing agent...\n")
    
    try:
        agent = AIAgent()
        print("✓ Agent initialized successfully!")
        print("\nAgent capabilities:")
        print("  • Send and draft emails")
        print("  • Get email templates")
        print("  • Create and manage tasks")
        print("  • Track task status")
        print("\nModel: tinyllama-1.1b (running locally)")
        print("Type 'quit' or 'exit' to stop.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["quit", "exit"]:
                    print("\nAgent shutting down. Goodbye!")
                    break
                
                print("\nAgent: Processing...\n")
                response = agent.chat(user_input)
                print(f"Agent: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nAgent interrupted by user.")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")
    
    except Exception as e:
        print(f"Failed to initialize agent: {str(e)}")
        print("\nMake sure you have:")
        print("1. Ollama installed: https://ollama.ai")
        print("2. Ollama running: ollama serve")
        print("3. TinyLlama model: ollama pull tinyllama")
        print("4. Install requirements: pip install -r requirements_agent.txt")


if __name__ == "__main__":
    main()
