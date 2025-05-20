
# 📂 SnapSort

**SnapSort** is a lightweight Python utility that automatically organizes files in a selected folder by file type. It’s perfect for cleaning up cluttered folders like Downloads or Desktop.

## 📌 Features

- 📁 Organizes files into subfolders (Images, Documents, Videos, etc.)
- 🧠 Automatically recognizes common file types
- 📦 Puts unknown types into an "Others" folder
- ⚙️ Command-line interface with customizable folder path
- 💻 Works on Windows, macOS, and Linux
## 📂 Before & After

### 🔹 Before
```

Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── [script.py](http://script.py/)
├── video.mp4
├── randomfile.xyz
```

### 🔹 After
```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
├── Scripts/
│   └── [script.py](http://script.py/)
├── Videos/
│   └── video.mp4
├── Others/
│   └── randomfile.xyz
```


## ⚙️ Installation

### ✅ Requirements

- Python 3.6 or higher

### 🧪 Setup

```bash
git clone <https://github.com/yourusername/SnapSort.git>
cd SnapSort

```

(Optional: create a virtual environment)

```
python -m venv venv
```

# On Windows

```
venv\Scripts\activate
```

# On macOS/Linux

```
source venv/bin/activate
```

## 🚀 Usage

### 🔧 Run the script

```bash
python snap_sort.py /path/to/folder

```

### 🔹 Examples

- **Windows:**
    
    ```bash
    python snap_sort.py "C:\Users\YourName\Downloads"
    
    ```
    
- **macOS/Linux:**
    
    ```bash
    python3 snap_sort.py ~/Downloads
    
    ```
    

---

## 🗂️ Supported File Categories

| Category | Extensions |
| --- | --- |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Documents | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| Videos | `.mp4`, `.mov`, `.avi` |
| Music | `.mp3`, `.wav` |
| Archives | `.zip`, `.rar`, `.7z` |
| Scripts | `.py`, `.js`, `.html`, `.css` |
| Others | Any unrecognized file type |

---

## 🧩 Customization

Want to support more file types or categories?

Open `snap_sort.py` and modify the `file_types` dictionary:

```
file_types = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx'],
    # Add your own!
}
```
## 🔁 Automation

You can schedule SnapSort to run automatically:

- 🪟 **Windows**: Use Task Scheduler
- 🍎 **macOS/Linux**: Use a cron job

---

## 🗺️ Roadmap

- [ ]  ✅ Add dry-run (preview without moving files)
- [ ]  ✅ Undo / Restore functionality
- [ ]  ⬜ GUI with drag-and-drop support
- [ ]  ⬜ Desktop notifications

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📬 Contact

Made with ❤️ by **[Your Name]**

📧 [adilc0070@gmail.com](mailto:adilc0070@gmail.com)

Give it a ⭐ if you find it useful!