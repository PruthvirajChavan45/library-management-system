# 📚 Library Management System

This project contains two interfaces:

- **Terminal UI** → run `main.py`
- **Web UI using Streamlit** → run `stream.py`
- **JSON database** → data stored in `library.json`

---

## Features

- Add books
- View books
- Issue / Return books
- JSON based storage
- Terminal UI
- Streamlit UI

---

## Project Structure

```
library-management-system/
├── main.py
├── stream.py
├── library.json
└── README.md
```

---

## Run Terminal Version

```bash
python main.py
```

---

## Run Streamlit Version

### Install Streamlit first
```bash
pip install streamlit
```

### Run:
```bash
streamlit run stream.py
```

---

## Files

### main.py  
Contains code for Terminal-based UI.

### stream.py  
Contains Streamlit UI code and interacts with JSON.

### library.json  
Acts as database (book records).

---

## About this project

- main.py shows terminal-based menu interface.
- stream.py launches Streamlit based UI (browser).
- Both read/write same library.json file.
