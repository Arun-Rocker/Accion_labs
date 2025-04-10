Problem: Given a log file access.log with entries in the following format:

192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /api/user HTTP/1.1" 200 1234
192.168.1.2 - - [10/Oct/2023:13:55:38 +0000] "POST /api/login HTTP/1.1" 401 567
192.168.1.1 - - [10/Oct/2023:13:55:40 +0000] "GET /api/products HTTP/1.1" 200 8901


grep -E 'HTTP.*"[4-5][0-9]{2}' access.log | \
awk '{print $1}' | \
sort | \
uniq -c | \
sort -nr