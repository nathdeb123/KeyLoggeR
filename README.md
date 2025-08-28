# 🖥️ Keylogger with Web Dashboard  


This project is a **Python-based keylogger** that captures keystrokes and automatically hosts them on a **Flask-powered local web server**.  
It logs keystrokes into a `log.txt` file and displays them in a clean, auto-refreshing web interface.  

⚠️ **Disclaimer:** This project is for **educational and research purposes only**. Unauthorized use of keyloggers is illegal. Please use responsibly.  

---

## 📌 Features  

- ✅ Captures both **alphanumeric** and **special keys** (`Enter`, `Space`, `Tab`, etc.).  
- ✅ Automatically saves logs into `log.txt`.  
- ✅ Hosts a **Flask web server** to view captured keystrokes.  
- ✅ Web dashboard **auto-refreshes every 3 seconds**.  
- ✅ Runs **keylogger & server simultaneously** using multithreading.  

---

## 📂 Project Structure  

```
keylogger-web/
│── main.py          # Main script (keylogger + Flask web server)
│── log.txt          # Log file (auto-created on first run)
│── README.md        # Documentation
```

---

## ⚙️ Requirements  

Install the required dependencies using **pip**:  

```bash
pip install pynput flask
```

---

## ▶️ Usage  

1. Clone or download the repository.  
2. Run the script:  

```bash
python main.py
```

3. Open a browser and visit:  

```
http://127.0.0.1:5000
```

4. The webpage will show **captured keystrokes**, refreshing every 3 seconds.  

---

## 📝 Example Log File (`log.txt`)  

```
=== Keylogger Started ===
h
e
l
l
o
(space)
w
o
r
l
d
```

---

## 🚀 Customization  

- Change the **server port** inside `run_flask()` if needed:  

```python
app.run(host="127.0.0.1", port=5000, debug=False)
```

- Modify log file name:  

```python
log_file = "log.txt"
```

---

## ⚠️ Legal & Ethical Notice  

This tool is created for:  
- Cybersecurity research  
- Educational purposes  
- Building **anti-keylogger defense systems**  

🚨 **Do not use this tool to monitor others without consent**. Unauthorized surveillance is against the law.  
