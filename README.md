# 📚 Library Management System

[![Streamlit App](https://img.shields.io/badge/🔗%20Live-Streamlit-blue?style=for-the-badge)](https://pruthviraj-library.streamlit.app)
> ⏳ Note: The live demo may take few seconds to load because Streamlit free hosting puts the app to sleep when inactive.

This project contains two interfaces:

- **Terminal UI** → run `main.py`
- **Web UI using Streamlit** → run `stream.py`
- **JSON database** → data stored in `library.json`
- **Dev Container Support** → run instantly in GitHub Codespaces

---

## 🚀 Features

- Add and manage books
- View book list
- Issue & Return books
- JSON based storage
- Command-Line UI
- Streamlit Web UI
- Runs in cloud using GitHub Codespaces (`.devcontainer`)

---

## 📂 Project Structure

```
library-management-system/
├── .devcontainer/     # Development container configuration (VS Code)
├── main.py            # Terminal UI
├── stream.py          # Streamlit Web UI
├── library.json       # JSON Book Database
└── README.md          # Documentation
```

---

## ▶ Run Terminal Version

```bash
python main.py
```

---

## 🌐 Run Streamlit Version

### Install Streamlit first
```bash
pip install streamlit
```

### Run:
```bash
streamlit run stream.py
```

---

## 📁 Files

### main.py  
Contains code for Terminal-based UI.

### stream.py  
Contains Streamlit UI code and interacts with JSON.

### library.json  
Acts as JSON database (book records).

---

## 🧩 What is `.devcontainer`?

`.devcontainer` allows this repository to run automatically inside a **pre-configured development environment**, especially inside **VS Code & GitHub Codespaces**.

It provides:

- Python version
- Required dependencies
- VS Code settings
- Extensions
- Ready-to-run workspace

Meaning:
👉 No need to manually install anything  
👉 Just open in GitHub Codespaces  
👉 Code runs instantly  

---

### 🔥 One line meaning

> `.devcontainer` makes setup automatic using VS Code + Docker + Codespaces.

---

### Why it’s useful

- Work from browser
- Avoid installing Python locally
- Same environment for all users
- Perfect for cloud development

---

## 💡 About this project

- `main.py` → menu-based terminal interface  
- `stream.py` → web dashboard using Streamlit  
- Both read/write the same `library.json`  
- Designed for beginners learning CRUD & JSON  
- Cloud-ready via `.devcontainer`  

---

## ⭐ Future Enhancements  

- Member system  
- Return deadline  
- Fine calculation  
- Categories  
- Search system  
- Authentication  

---

## 🧑‍💻 Author

**Pruthviraj Chavan**  
🔗 Live Project: https://pruthviraj-library.streamlit.app
