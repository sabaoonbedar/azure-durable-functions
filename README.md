# 🚀 Azure Durable Functions (Python) with v2 Decorators

This project demonstrates how to use **Azure Durable Functions in Python** with the **version 2 decorator model** introduced in the `azure.durable_functions` SDK. It consists of:

- Two activity functions (`Activity1`, `Activity2`)
- One orchestrator function
- A `DFApp` function app setup using Blueprints

---

## 📦 Project Structure

📁 your_project/
│
├── activity1.py
├── activity2.py
├── orchestrator.py
├── main.py # Registers all blueprints to DFApp
├── requirements.txt
└── host.json # Azure Functions host configuration