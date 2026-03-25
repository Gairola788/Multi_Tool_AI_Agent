# Multi Tool AI Agent 🤖

A simple **Python-based AI agent** that can perform multiple tasks such as:

* 🌦 Checking weather for any city
* 🧮 Performing mathematical calculations
* 🔎 Searching the web for information

The agent analyzes the user query and routes it to the appropriate tool.

---

# Project Features

✔ Weather information using OpenWeather API
✔ Mathematical calculations using a calculator tool
✔ Web search using DuckDuckGo API
✔ Modular tool-based architecture
✔ Simple command-line interface

---

# Project Structure

```
Multi_tool_Agent/
│
├── main.py                # Main AI agent logic
├── weather_tool.py        # Weather API integration
├── calculator_tool.py     # Calculator tool
├── search_tool.py         # Web search tool
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (API keys)
├── .gitignore             # Ignored files
└── README.md              # Project documentation
```

---

# How It Works

The AI agent reads the user query and determines which tool to use.

Example flow:

```
User Query
   ↓
Query Classification
   ↓
Tool Selection
   ↓
Execute Tool
   ↓
Return Result
```

---

# Installation

Clone the repository

```
git clone https://github.com/your-username/Multi_tool_Agent.git
```

Move into the project directory

```
cd Multi_tool_Agent
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```
OPENWEATHER_API_KEY=your_api_key_here
```

You can get a free API key from
OpenWeatherMap.

---

# Running the Project

Run the agent using:

```
python main.py
```

Example interaction:

```
Ask any query regarding calculations, weather or web search

> weather in Delhi
Temperature in Delhi is 30°C

> calculate 25 * 4
Result: 100

> search python programming
Python is a high-level programming language...
```

---

# Dependencies

This project uses the following Python libraries:

* requests
* python-dotenv

Install them with:

```
pip install -r requirements.txt
```

---

# Future Improvements

Possible upgrades for this project:

* LLM-based tool selection
* Natural language understanding
* More tools (news, currency, stocks)
* GUI interface
* Voice assistant support

---

# Learning Outcome

This project demonstrates the basics of:

* AI agent architecture
* Tool-based system design
* API integration
* Python project structuring

---

# Author

Created by **Akshat**

---

# License

This project is open-source and free to use for learning purposes.
