# Log File Analyzer 

It takes a web server log file (like from Nginx or Apache) and finds useful patterns.
Instead of manually reading thousands of log lines, this script gives you a simple summary of what’s happening on your server.

How log files work

How to read and process files in Python

How to find patterns like errors or frequent visitors

**When you run the script, it will show like this:**

- Count the total number of requests

- Tell you how many 404 errors happened (broken links)

- Show the most requested pages

- Show the top IP addresses making requests

---

```Project Files
LogAnalyzerProject/
│── log_analyzer.py   # The Python script to read and analyze the log file
│── nginx_access.log        # log file is used to analyze the data
│── README.md         # This file (documentation)
```

---

Open the project in VS Code.

Make sure you have Python 3 installed.

In LogAnalyzerProject folder, Create files called nginx_access.log and log_analyzer.py

Run the script in the terminal:

```python log_analyzer.py```






