# Log Parsing Project

This project contains a Python script that parses log files and computes metrics.

## 0-stats.py

A script that reads stdin line by line and computes the following metrics:
- Total file size
- Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)

### Input format
The expected input format is:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
Lines that don't match this format are skipped.

### Output
After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints:
- Total file size: `File size: <total size>`
- Number of lines by status code in ascending order (only for codes that appear in the input)

### Usage
```
cat logfile.txt | ./0-stats.py
```
Or pipe in data:
```
tail -f logfile.txt | ./0-stats.py
```

### Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)
