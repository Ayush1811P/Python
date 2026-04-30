# 🚀 AI Agent - Local Model Edition (Ollama + TinyLlama)

A fully working AI agent that runs **completely locally** using Ollama and TinyLlama. No API keys needed, no cloud costs!

## ✨ Key Benefits

✅ **100% Local** - Everything runs on your machine
✅ **Free** - No API costs or subscriptions
✅ **Private** - Your data never leaves your computer
✅ **Fast** - Instant response times once running
✅ **No Internet Required** - Works offline after setup

## 📋 System Requirements

- **CPU**: Modern processor (Intel/AMD/Apple Silicon)
- **RAM**: 4GB minimum (8GB recommended for smooth operation)
- **Disk**: 2GB free space (for model + agent)
- **OS**: Windows, macOS, Linux

## 🔧 Installation

### Step 1: Install Ollama

**Windows/Mac/Linux:**
Visit https://ollama.ai and download the installer for your OS.

After installation, verify:
```bash
ollama --version
```

### Step 2: Pull TinyLlama Model

```bash
ollama pull tinyllama
```

This downloads the 1.1B parameter model (~600MB). First pull takes a few minutes.

### Step 3: Start Ollama Server

In a new terminal, run:
```bash
ollama serve
```

You should see:
```
Listening on [::1]:11434
```

Keep this terminal open while using the agent.

### Step 4: Install Agent Dependencies

```bash
pip install -r requirements_agent.txt
```

### Step 5: Create .env File

```bash
cp .env.example .env
```

The .env file should have:
```env
OLLAMA_BASE_URL=http://localhost:11434
LOCAL_MODEL=tinyllama

# Optional: Gmail for email sending
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
```

### Step 6: Run the Agent

```bash
python ai_agent.py
```

You should see:
```
🤖 AI Task Automation Agent - Local Model Edition
   Using Ollama + TinyLlama

Initializing agent...

✓ Connected to Ollama at http://localhost:11434
✓ Model 'tinyllama' is available
✓ Agent initialized successfully!
```

## 💬 Using the Agent

Same commands as the cloud version:

```
You: Create a task to review the budget
Agent: I'll create that task for you...

You: List my pending tasks
Agent: You have 1 pending task...

You: Send an email to john@company.com about the meeting
Agent: I'll draft an email for you...

You: quit
Agent: Shutting down. Goodbye!
```

## ⚙️ Configuration

### Using Different Models

Edit `.env`:
```env
LOCAL_MODEL=neural-chat  # faster, smaller
LOCAL_MODEL=mistral     # better quality
LOCAL_MODEL=llama2      # larger, slower
```

Pull the model first:
```bash
ollama pull mistral
```

### Adjusting Ollama Settings

Edit Ollama temperature/parameters in `.env`:
```env
OLLAMA_BASE_URL=http://localhost:11434
LOCAL_MODEL=tinyllama
OLLAMA_TEMPERATURE=0.5  # Lower = more deterministic
```

(Note: Modify `ai_agent.py` line to use if needed)

### Remote Ollama Server

If Ollama is on another machine:
```env
OLLAMA_BASE_URL=http://192.168.1.100:11434
```

## 🎯 Capabilities

### Email Management
- Send emails (requires Gmail config)
- Draft emails for review
- Email templates

### Task Management
- Create tasks with due dates
- List & filter tasks by status
- Update task progress
- Delete tasks

### Limitations vs Cloud Version

- **Smaller context**: TinyLlama has smaller context window
- **Simpler reasoning**: Less capable than GPT-4
- **Slower**: 2-5 seconds per response vs instant
- **First response slower**: Initial run takes longer to load model
- **Limited tool calling**: Simpler tool invocation than OpenAI

## 🚀 Performance Tips

### Speed Up Responses

1. **Use quantized model** (already using Q4_K_M):
   ```bash
   ollama pull neural-chat  # Smaller, faster
   ```

2. **Reduce context history**: Fewer messages = faster response
   (Modify ai_agent.py to limit conversation history)

3. **Increase Ollama timeout**:
   Edit `ai_agent.py` line with timeout value

### Reduce Memory Usage

Use a smaller model:
```bash
ollama pull phi        # Smaller than tinyllama
ollama pull orca-mini  # Lightweight
```

### Improve Quality

Use a larger model:
```bash
ollama pull mistral    # 7B parameters
ollama pull neural-chat # 7B, good for chat
```

## 🔍 Troubleshooting

### "Cannot connect to Ollama"
**Issue**: `ConnectionError: Cannot connect to Ollama at http://localhost:11434`

**Solution**:
1. Start Ollama server: `ollama serve`
2. Check if running: `curl http://localhost:11434/api/tags`
3. Check .env has correct OLLAMA_BASE_URL

### "Model not found"
**Issue**: `Model 'tinyllama' not found locally`

**Solution**:
1. Pull model: `ollama pull tinyllama`
2. Verify: `ollama list`
3. Wait for download to complete

### "Response timeout"
**Issue**: Agent takes too long to respond

**Solution**:
1. Try simpler queries first
2. Use faster model: `ollama pull neural-chat`
3. Check system resources (CPU/RAM usage)
4. Close other applications

### Agent hangs on startup
**Issue**: Takes forever to initialize

**Solution**:
1. First load takes longer as model is loaded into memory
2. Subsequent requests are faster
3. Check system has enough RAM

### Poor response quality
**Issue**: Agent responses don't match expectations

**Solution**:
1. TinyLlama is a 1.1B model - not as capable as GPT-4
2. Use a larger model: `ollama pull mistral`
3. Rephrase questions more clearly
4. Use simpler, more direct commands

## 📊 Model Comparison

| Model | Size | Speed | Quality | RAM Needed |
|-------|------|-------|---------|-----------|
| **tinyllama** | 600MB | Fast | Fair | 2GB |
| neural-chat | 4.7GB | Medium | Good | 6GB |
| mistral | 4.2GB | Medium | Good | 6GB |
| llama2 | 3.8GB | Medium | Very Good | 6GB |
| orca-mini | 1.3GB | Fast | Fair | 3GB |

## 🎓 Common Use Cases

### Quick Queries (Use TinyLlama)
```
"Create a task"
"List tasks"
"Draft an email"
```

### Complex Tasks (Use Mistral/Neural-Chat)
```
"Create a task and email the team about it"
"Show pending tasks and write a status summary"
```

### High Quality (Use Llama2)
```
"Write a professional follow-up email"
"Complex task organization"
```

## 🔄 Switching Models

1. Stop the agent
2. Edit `.env`: `LOCAL_MODEL=mistral`
3. Pull model (first time only): `ollama pull mistral`
4. Restart agent: `python ai_agent.py`

## 📚 Additional Resources

- **Ollama Docs**: https://github.com/ollama/ollama
- **Available Models**: https://ollama.ai/library
- **TinyLlama**: https://github.com/jzhang38/TinyLlama
- **Model Benchmarks**: Compare model performance online

## 💾 Storage & Cleanup

### Check Model Size
```bash
ollama list
```

### Delete Model (if needed)
```bash
ollama rm tinyllama
```

### Ollama Storage Location
- **Linux/Mac**: `~/.ollama/models`
- **Windows**: `C:\Users\{user}\.ollama\models`

## 🔐 Privacy & Security

✅ All processing happens locally
✅ No data sent to servers
✅ No API keys exposed
✅ Works completely offline
✅ Full control over your data

## 📈 Upgrading

### Switch to Faster Setup
When ready to use cloud API:
```bash
pip install openai
# Create new ai_agent_cloud.py with OpenAI code
```

### Hybrid Approach
Keep local running for private tasks, use cloud for complex tasks.

## 🎉 Performance Profile

**First Start**: ~30 seconds (loading model into memory)
**Subsequent Starts**: <1 second
**Typical Response**: 2-5 seconds
**Email Send**: <1 second
**Task Operations**: <1 second

## 🚨 Known Limitations

1. **Context window**: Limited conversation history
2. **Tool calling**: Simpler than GPT-4
3. **Long responses**: May be cut off
4. **Math/Logic**: Less accurate than larger models
5. **Complex reasoning**: Limited capability

## 🎯 Best Practices

1. Keep Ollama server running in background
2. Use `.env` for configuration
3. Start with simple queries
4. Monitor system resources
5. Upgrade model if needed for complex tasks

## 📞 Support

If issues occur:
1. Check Ollama is running: `curl http://localhost:11434/api/tags`
2. Verify model exists: `ollama list`
3. Check `.env` configuration
4. Try simpler queries
5. Check system RAM availability

## 🎁 Next Steps

1. ✅ Install Ollama
2. ✅ Pull tinyllama: `ollama pull tinyllama`
3. ✅ Start Ollama: `ollama serve`
4. ✅ Run agent: `python ai_agent.py`
5. ✅ Try commands!

---

**Happy automating with local AI!** 🚀

No API keys. No cloud costs. 100% local. 100% private.
