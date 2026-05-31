


# 🛡️ AI-Driven Security Analysis Lab

An interactive desktop application for **log monitoring, network diagnostics, and AI-powered analysis**.  
Built with **Python, CustomTkinter, Ollama, and MongoDB**, this project demonstrates how conversational AI can assist in real-time security analysis.

---

## 📖 Overview
This project integrates:
- **Log Monitoring** – Categorizes logs into INFO, WARNING, and CRITICAL.  
- **Network Diagnostics** – Runs system-level scans using `netstat`.  
- **Conversational AI** – Powered by Ollama (`huihui_ai/qwen3.5-abliterated:2b`) for natural language queries.  
- **Persistent History** – Saves chat interactions for accountability and reproducibility.  
- **Modern UI** – Built with CustomTkinter for a sleek, Copilot-like interface.

---

## ✨ Features
- 🟩 **AI Query Interpretation** – Ask natural questions about logs and network traffic.  
- 📊 **System Architecture & Flowcharts** – Includes diagrams for architecture, data flow, use cases, activity, ER, and database design.  
- 💾 **Persistent Chat History** – Export and save all interactions.  
- 🔐 **Authentication & Security Context** – Designed with compliance and monitoring in mind.  
- 🎨 **Minimalist UI** – Dark theme, modern font, and intuitive layout.

---

## 📂 Project Structure
```
AI-Security-Analysis-Lab/
│── mega_chatbot_ui.py        # Main application
│── system_logs.txt           # Sample logs
│── requirements.txt          # Dependencies
│── README.md                 # Project showcase
│── diagrams/                 # Architecture & flowcharts
│── screenshots/              # UI screenshots
│── chat_history.txt          # Example saved output
```

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/AI-Security-Analysis-Lab.git
cd AI-Security-Analysis-Lab
pip install -r requirements.txt
python mega_chatbot_ui.py
```

---

## 🚀 Usage
1. Run the application.  
2. Enter queries like:  
   - *“Show me today’s critical errors.”*  
   - *“Analyze open ports in the network.”*  
3. View categorized logs and AI responses in the chat window.  
4. Save chat history for later review.

---


## 📊 Diagrams
- **System Architecture**  
- **Data Flow Diagram**  
- **Use Case Diagram**  
- **Activity Diagram**  
- **Entity Relationship Diagram**  
- **Database Design**  

*(See `/diagrams` folder for visuals.)*

---

## 🛠 Tech Stack
- **Python 3.10+**  
- **CustomTkinter** – Modern UI framework  
- **Ollama** – AI model serving (`huihui_ai/qwen3.5-abliterated:2b`)  
- **MongoDB** – Persistent storage  
- **Netstat** – Network diagnostics  

---

## 📌 Future Scope
- 🔍 Advanced visualization of logs and network traffic  
- 📈 Integration with SIEM tools  
- ☁️ Cloud deployment for scalability  
- 🤖 Automated remediation workflows  

---

## 📜 License
This project is licensed under the **Apache License 2.0** – free to use and modify.

---

## 🌟 Showcase
This repository demonstrates how **AI can be integrated into security analysis workflows** with a professional UI and structured documentation.  
Perfect for academic projects, portfolio showcases, and proof-of-concept implementations.
```

---

This README is structured to **impress recruiters and collaborators**: clear overview, features, installation, usage, test cases, diagrams, and future scope.  

Would you like me to also generate a **requirements.txt** file for you, listing all the Python dependencies (CustomTkinter, Ollama, etc.) so your repo is fully plug‑and‑play?
