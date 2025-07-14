# 📁 Kovai.co Mock API - Document360 Folder CRUD

This project contains mock implementations of the Document360 Drive Folder CRUD API tasks (GET, POST, PUT, DELETE), organized as individual Python files.This project demonstrates **mock CRUD operations** for Document360's Folder API.  
Each operation is modularized into its own file and callable from `main.py`.

---

## 🚀 Features

- 🧾 List Folders (GET)
- 📂 Create Folder (POST)
- ✏️ Rename Folder (PUT)
- 🗑️ Delete Folder (DELETE)
- ✅ All responses are mocked for safe demo
- 💻 Clean input/output using terminal

---

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

Clone the repo:

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
4.Create .env file
```
env
API_TOKEN=your_mock_token
```
---
---
finally:
```
bash
python main.py
```
sample output:
'''
A "folder_id.txt" file create for log.

<img width="927" height="798" alt="image" src="https://github.com/user-attachments/assets/056cec10-fc12-4e74-8a4d-2d86b2de1d33" />

<img width="754" height="293" alt="image" src="https://github.com/user-attachments/assets/f1ee5c0b-5a69-40f5-9ec2-4a51cd541b37" />

```
---
## 🧠 Note

- This project uses **mock data** (no real API call).
- Designed as per Kovai.co's instructions for modular, token-safe, and clear structure.
