# Kovai.co - Structured API Task (Mocked)

This project contains mock implementations of the Document360 Drive Folder CRUD API tasks (GET, POST, PUT, DELETE), organized as individual Python files.

---

## 📁 File Structure

```
.
├── get_folders.py
├── create_folder.py
├── update_folder.py
├── delete_folder.py
├── utils.py
├── .env         (excluded in Git)
├── .gitignore
└── README.md
```

---

## 🔧 Setup Instructions

1. Create a `.env` file in the root directory with:

```
API_TOKEN=your_api_token_here
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run individual scripts as needed:

```bash
python get_folders.py
python create_folder.py
python update_folder.py
python delete_folder.py
```

---

## 🧠 Note

- This project uses **mock data** (no real API call).
- Designed as per Kovai.co's instructions for modular, token-safe, and clear structure.
