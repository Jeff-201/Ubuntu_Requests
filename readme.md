# Fetched Images Downloader 🖼️

A simple Python script that downloads one or more images from the web and saves them into a local **Fetched_Images/** directory.  

The script is built around **Ubuntu principles**:  
- 🌍 **Community** → Connects to the wider web community to fetch images.  
- 🙏 **Respect** → Handles errors gracefully without crashing.  
- 📂 **Sharing** → Organizes downloaded images in a dedicated folder.  
- 🛠️ **Practicality** → Provides a real, useful tool for everyday needs.  

---

## Features
- Accepts **multiple URLs** (comma-separated or line-by-line).  
- Creates a **Fetched_Images/** folder automatically.  
- Saves images with **unique, timestamped filenames** to prevent overwriting.  
- Handles network errors, invalid URLs, and HTTP errors gracefully.  
- Provides a **download summary** (successful vs. failed).  

---

## Requirements
- Python 3.7+  
- [Requests](https://docs.python-requests.org/en/latest/) library  

Install dependencies with:
```bash
pip install requests
