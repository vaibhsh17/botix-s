<div align="center">

# **Botix-S**
### A simple, customizable, no-code chatbot system.

![Progress](https://img.shields.io/badge/Progress-In%20Development-orange)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Version](https://img.shields.io/badge/Version-0.1.0-green)
</div>

- **Botix-S** is a simple, customizable chatbot project designed to make automated question-and-answer interactions easy to  create and manage.

- Instead of writing seperate chatbot logic for every response, Botix-S stores questions and answers in a structured JSON file and automatically matches user message with the available responses.

- The project is being  developed with a long-term goal of becoming a **no-code chatbot platform**, where users can create and customize their own bots without manually editing code or configuration files.

<div align="center">

## 🚀 **Current Progress**
</div>

The current version of Botix-S focuses on building the **core chatbot foundation** and keeping the project simple, modular and easy to extand.

**implemented so far:**

- Python-based chatbot logic.
- Question-and-answer response system.
- JSON based response storage.
- Automatic message matching.
- Modular project structure.
- Enviourment variable support using `.env`.
- Dependency management through `requirements.txt`.
- Github projrct workflow.

<div align="center">

## ⚙️ **How it works**g
</div>

Botix-S follows a simple response-based architecture.

```text
User Message
     ↓
  Botix-S
     ↓
responses.json
     ↓
Question Matching
     ↓
  Bot Response
```

Question and their corresponding answers are stored in:

```
data/response.json
```
> User sends a message, Botix-S checks the stored questions and returns the corresponding answer when a match is found.

<div align="center">

## **💬 Example**
</div>

```
user:
what is botix-s

Botix-S:
Botix-S is a no-code Discord chatbot project.
```

<div align="center">

##  📁 Project Structure
</div>

```
Botix-S/
|
├── data/
|   └──responses.json
|
├──sre/
|    └──bot.py
|
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└──CONTRIBUTORS.md
```

<div align="center">

## 🛠️ Technologies Used
</div>

- **Python** - Core Programming Language
- **discord.py** - Discord bot functionally.
- **JSON** - Storing chatbot questions and responses.
- **Python-dotenv** - Managing enviourment variables.
- **GitHub** - Version controll collaboration.

<div align = "center">

## 🌱 Vision
</div>

- Botix-S aims to grow from a simple response-based chatbot into an **easy-to-use no-code chatbot builder.

**Upcoming Goals:**

- **Web Dashboard** - Create and manage bots through a simple interface.
- **Visual Q&A Management** - Add, edit and rempve questions manually editing JSON files.
- **Discord Integrarion** - Connected created bots withDiscord servers.
- **Automatic Configuration** - Manage bot responses through the dashboard.
- **Muti-Bot Support** - Allow users to manage multiple bots.
- **Optional AI Integration** - Add AI-based responses as a future fallback system.
- **Live Configuration Updates** - Update chatbot responses without manually changing project files.

<div slign="center">

## 🧭 Why Botix-S
</div>

Botix-S is built around a simple idea:
     ```
     **Chatbot should be easy to create, customize and understand**
     ```

<div align="center">

## 📌 Project Status
</div>

**Botix-S** is currently under development.
The core response based chatbot  structure is in place. Discord deployment and no-code dashboard are part of the next stages of development.

<div align="center">

## 👨‍💻 Developer
</div>

- Developed as a learning and development project focus on:
  - Python
  - Chatbot develpoment
  - JSON data handling
  - Discord bot develpoment
  - No-Code platform structure
