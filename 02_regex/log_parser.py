import re
import csv

pattern = re.compile(
    r'\[(.*?)\]\s+'                     
    r'(ERROR|INFO|WARNING)\s+'          
    r'User:\s(\w+)\s+'                  
    r'IP:\s(\d{1,3}(?:\.\d{1,3}){3})\s+' 
    r'Action:\s(\w+)'                   
)


clean_rows = []

with open("sample_logs.txt", "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            timestamp = match.group(1)
            level = match.group(2)
            user = match.group(3).lower()
            ip = match.group(4)
            action = match.group(5)

            clean_rows.append([timestamp, level, user, ip, action])

with open("clean_logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "level", "user", "ip", "action"])
    writer.writerows(clean_rows)

print("Log parsing complete. Output saved to clean_logs.csv")
