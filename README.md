# AI Blog Writer - Agentic AI System

An intelligent blog writing system built with CrewAI that automates the entire blog creation process from research to SEO optimization.

## 🎯 Project Overview

This project demonstrates the fundamentals of CrewAI and agentic AI applications. It uses multiple AI agents working together to create high-quality, SEO-optimized blog content.

## 🤖 AI Agents

The system employs three specialized agents:

1. **Research Agent** - Collects 10-15 interesting and latest facts about the given topic
2. **Writer Agent** - Creates engaging 300-500 word blog content based on research
3. **SEO Agent** - Optimizes content with keywords, meta titles, and descriptions

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **AI Framework**: CrewAI
- **LLM**: Google Gemini 2.0 Flash

## 📋 Prerequisites

- Python 3.8+
- pip or uv package manager

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-blog-writer.git
cd ai-blog-writer
```

2. Install dependencies
```bash
uv sync
```

3. Create a `.env` file and add your API keys
```env
GEMINI_API_KEY=your_api_key_here
```

## ▶️ Running the Application

Start the FastAPI server:
```bash
uvicorn backend:app --reload
```

The application will be available at `http://127.0.0.1:8000`

## 💻 Usage

1. Open your browser and navigate to `http://127.0.0.1:8000`
2. Enter your blog topic in the input field
3. Click "Generate Blog"
4. Wait 30-60 seconds for the AI agents to complete their work
5. View your generated, SEO-optimized blog!



## 🎓 Learning Outcomes

- Understanding agentic AI systems
- Working with multiple AI agents
- Building REST APIs with FastAPI
- Integrating AI with web applications
- Asynchronous task processing


## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!
