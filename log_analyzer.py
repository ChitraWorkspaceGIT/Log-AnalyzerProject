# LogAnalyzerProject

from collections import Counter

# Open the log file
with open("nginx_access.log", "r") as f:
    logs = f.readlines()


# 1. Count 404 errors
errors_404 = [line for line in logs if " 404 " in line]
print(f"Total 404 errors: {len(errors_404)}")

# 2. Most requested pages
pages = [line.split('"')[1].split()[1] for line in logs if '"' in line]
top_pages = Counter(pages).most_common(5)
print("\nTop requested pages:")
for page, count in top_pages:
    print(f"{page} - {count} times")

# 3. Most active IP addresses
ips = [line.split()[0] for line in logs]
top_ips = Counter(ips).most_common(5)
print("\nTop IP addresses:")
for ip, count in top_ips:
    print(f"{ip} - {count} times")
