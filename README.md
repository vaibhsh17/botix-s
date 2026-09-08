<div align="center">

# **Botix-S**
### A Simple and Customizable Discord Chatbot.

![Progress](https://img.shields.io/badge/Progress-Working-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Discord.py](https://img.shields.io/badge/discord.py-Library-purple)
![Version](https://img.shields.io/badge/Version-0.1.0-orange)

</div>

**Botix-S** is a simple, response-based **Discord chatbot** built with
Python and `discord.py`.

The bot automatically reads user messages, checks them against a
predefined collection of questions stored in a JSON file, and sends the
corresponding answer when a matching question is found.

The main purpose of Botix-S is to provide a clean and beginner-friendly
foundation for understanding **Discord bots, message handling, JSON
data storage, environment variables, and Python-based automation**.

---

<div align="center">

# 🚀 **What is Botix-S?**
</div>

Botix-S is a basic Discord Chatbot that works using a **question-and-answer response system**.

Instead of using AI or Machine Learning, the bot uses predefined questions and answers stored in:
```text
data/responses.json
```

When the user sends a message in a Discord channel, Botix-S checks the message against the stored questions.
If a matching question is found the bot sends the associated answer.

Basic Flow
```
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

<div align="center">

# ✨ **Features**
</div>

- Discord bot integration using discord.py
- Automated question-and-answer responses
- JSON-based response storage
- Message matching system
- Python-based implementation
- Secure token management using .env
- Simple and modular project structure
- Easy to customize and extend

<div align="center">

# 🧠**How Does It Work?**
</div>

Botix-S listens for message sent in Discord.

For every recieved message:

- The message content is converted to lowercase.
- The bot checks the stored question in responses.json.
- If a matching question is found, its answer is sent to the discord channel.
- If no-matching questions exist, the bot currently does not return a predefined response.

**For Example**
```
user:
hello

Botix-S:
hello! 👋 I'm Botix-S.
```
```
user:
what is discord

Botix-S:
Discord is a platform for chatting and communities.
```

<div align="center">

# 📂**Project Structure**
</div>

```
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

<div align="center">

# ⚙️ **Setup & Installation**
</div>

Clone the Repository:
```
git clone https://github.com/vaibhsh17/botix-s.git
```

Move into the project directory:
```
cd botix-s
```

Create virtual Enviourment:
```
python -m venv .venv
```

Install Dependencies:
```
pip install -r requirements.txt
```

<div align="center">

# 🔐**Discord Configuration**
</div>

For Botix-S to recieve message content, the **Message Content Intent** must be enabled in the Discord Developer Portal.

The bot also needs permissions to:

- View Channels
- Send Messges
- Read Message History

These permissions allows Botix-S to recieve and respond to message in the configured Discord server.

<div align="center">

# 📌**Crrent Limitations**
</div>

- Current Version of Botix-S is simple:
    - Responses are predefined.
    - Questions are manually stored in JSON.
    - The bot does not generate AI-based answers.
    - New responses require editing responses.json.
    - The current matching system depends on the stored question text.

- These limitations are part of the project's current stage and provide
a foundation for future improvements.

<div align="center">

# 📈**Project Status**
</div>

🟢 Working — v0.1.0

The current version successfully connects to Discord, recieves user messages, matches predefined questions, and sends the curresponding responses.
