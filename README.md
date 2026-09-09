<div align="center">

# **Botix-S**
### Simple, customizable, and easy-to-use Discord chatbot.

![Progress](https://img.shields.io/badge/Progress-Working-brightgreen)
![Documentation Status](https://img.shields.io/badge/Docs-Maintained-blue)
![Version](https://img.shields.io/badge/Version-0.1.0-orange)
![Python](https://img.shields.io/badge/Language-Python-blue)
![Discord](https://img.shields.io/badge/Platform-Discord-5865F2)
</div>


**Botix-S** is a simple, response-based Discord chatbot built with
**Python** and **discord.py**.

It allows a Discord server to have automated question-and-answer
responses using a predefined collection of questions and answers stored
in a JSON file.

Instead of writing a new piece of chatbot logic for every response,
Botix-S reads the available questions from `responses.json`, matches
the user's message, and sends the corresponding answer automatically.

The project is designed as a clean and beginner-friendly foundation for
learning **Discord bot development, message handling, JSON data
management, environment variables, and automation**.

<div align="center">

## 🚀 **Current Progress**
</div>

The current stage of Botix-S focuses on building and testing the
**core Discord chatbot system** before moving toward more advanced
features.

**Implemented so far :**

- 🤖 Discord bot successfully connected using `discord.py`.
- 💬 Automatic message receiving and response handling.
- 📄 JSON-based question and answer storage.
- 🔎 Automatic matching between user messages and stored questions.
- 🧩 Simple and modular Python project structure.
- 🔐 Secure bot token handling using environment variables.
- 📦 Dependency management using `requirements.txt`.
- 🌐 Successful integration with a Discord server.
- 🛠️ Basic Git and GitHub project workflow.

<div align="center">

## ⚙️ **How Botix-S Works**
</div>

Botix-S follows a simple response-based architecture:

```text
Discord User
      ↓
 User Message
      ↓
   Botix-S
      ↓
responses.json
      ↓
Question Matching
      ↓
   Bot Reply
```

When a user sends a message, Botix-S receives the message and compares
it with the questions stored inside `data/responses.json`.

If a matching question is found, the corresponding answer is sent back
to the Discord channel.

### Example

```text
User:
hello

Botix-S:
hello! 👋 I'm Botix-S.
```

Another example:

```text
User:
what is discord

Botix-S:
Discord is a platform for chatting and communities.
```


## 📂 **Project Structure**

```text
Botix-S/
│
├── data/
│   └── responses.json
│
├── src/
│   └── bot.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── CONTRIBUTORS.md
```

### `src/bot.py`

The main Python file responsible for:

- Connecting the bot to Discord.
- Receiving user messages.
- Reading response data.
- Matching questions.
- Sending automated replies.

### `data/responses.json`

Contains the predefined questions and answers used by Botix-S.

Example:

```json
{
    "responses": [
        {
            "question": "hello",
            "answer": "hello! 👋 I'm Botix-S."
        },
        {
            "question": "hi",
            "answer": "Hi! How can I help you?"
        }
    ]
}
```

### `.env`

Used to store sensitive configuration such as the Discord bot token.

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

> Never publish your real Discord bot token on GitHub.

### `requirements.txt`

Contains the dependencies required by the project:

```text
discord.py
python-dotenv
```

<div align="center">

## ✨ **Features**
</div>

- 🤖 **Discord Integration** — Runs as a real Discord bot.
- 💬 **Automated Responses** — Responds to predefined questions.
- 📄 **JSON Response System** — Keeps questions and answers in a simple
  editable format.
- 🔎 **Message Matching** — Checks incoming messages against stored
  questions.
- 🔐 **Environment Variables** — Keeps sensitive credentials outside the
  source code.
- 🧩 **Simple Architecture** — Easy to understand, modify, and extend.
- 🐍 **Python Powered** — Built using Python and `discord.py`.

<div align="center">

## 📝 **Adding Questions & Answers**
</div>

Botix-S can be customized by editing:

```text
data/responses.json
```

Add a new question and answer like this:

```json
{
    "question": "what is python",
    "answer": "Python is a popular programming language."
}
```


## 🔧 **Setup & Installation**


### 1. Clone the Repository

```bash
git clone https://github.com/vaibhsh17/botix-s.git
```

### 2. Open the Project

```bash
cd botix-s
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

Replace the placeholder with your own Discord bot token.

### 7. Run Botix-S

```bash
python src/bot.py
```

When the bot successfully connects to Discord, you should see:

```text
Botix-S is online as Botix-S#7076
```

<div align="center">

## 🔐 **Discord Configuration**
</div>

Botix-S requires the appropriate Discord configuration to receive and
respond to messages.

The bot uses:

- **Message Content Intent**
- **View Channel**
- **Send Messages**
- **Read Message History**

The Message Content Intent allows Botix-S to receive the message content
required for the response-matching system.

<div align="center">

## 🛠️ **Technologies Used**
</div>

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| discord.py | Discord bot development |
| JSON | Question and answer storage |
| python-dotenv | Environment variable management |
| GitHub | Repository hosting |
| Discord API | Bot communication |

<div align="center">

## 📌 **Current Limitations**
</div>

Botix-S is intentionally simple in its current version.

At the moment:

- Responses are predefined.
- Questions and answers are stored manually in JSON.
- The bot does not generate AI-based answers.
- Unknown questions do not yet have a dedicated fallback system.
- The current matching system depends on the stored question text.
- The bot needs to remain running on the host machine to stay online.

These limitations are part of the current development stage and provide
a foundation for future improvements.

<div align="center">

## 🌱 **Vision & Next Steps**
</div>

Botix-S aims to evolve from a basic response-based Discord bot into a
more flexible and user-friendly chatbot system.

**Upcoming goals :**

- 💬 **Fallback Responses** — Provide a response for unknown questions.
- 🧠 **Smarter Matching** — Improve how similar questions are recognized.
- 🌐 **Web Dashboard** — Manage chatbot settings through a visual interface.
- ➕ **No-Code Q&A Management** — Add and edit responses without manually
  modifying JSON files.
- 👥 **Multi-Bot Support** — Allow users to manage multiple chatbot
  configurations.
- 💾 **Automatic Configuration** — Manage response data automatically.
- 🤖 **AI Integration** — Add optional AI-powered responses in the future.
- ☁️ **Cloud Deployment** — Keep bots running without requiring a local
  computer.
- 📊 **Bot Analytics** — Track interactions and usage statistics.

<div align="center">

## 📘 **About This Version**
</div>

> **v0.1.0 - Working Discord Bot**

This version establishes the core Botix-S architecture and demonstrates
a working Discord chatbot.

The current release can connect to Discord, receive user messages,
match predefined questions from `responses.json`, and send automated
responses.

The next stage will focus on making the response system smarter and
easier to manage.

<div align="center">

## 🧭 **Why Botix-S**
</div>

Botix-S is built around a simple idea:

> **A chatbot should be easy to understand, customize, and extend.**

The project focuses on keeping the core architecture simple while
providing a foundation that can grow into a more advanced chatbot
platform.

Instead of starting with complex AI systems, Botix-S begins with the
fundamentals:

```text
Python
   ↓
Discord API
   ↓
Message Handling
   ↓
JSON Data
   ↓
Automated Responses
```


<div align=""center>

## 👨‍💻 **The Developer**
</div>

**Vaibhav**

Botix-S is developed as a learning and development project focused on
exploring:

- Python programming
- Discord bot development
- JSON data handling
- API-based applications
- Environment variable management
- Chatbot architecture

<div align="center">

## 📈 **Project Status**
</div>

🟢 **Working — v0.1.0**

The current version of Botix-S is successfully connected to Discord and
can receive and respond to predefined user messages.

The project is actively being improved with the goal of adding smarter
responses, easier configuration, and more advanced chatbot features.

<div align="center">

### **Botix-S — Simple logic. Automated responses. Built to grow.**
</div>
