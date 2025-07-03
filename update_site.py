from datetime import datetime

# Read current count
with open("count.txt", "r") as f:
    count = int(f.read().strip())

# Increment count
count += 1

# Save new count
with open("count.txt", "w") as f:
    f.write(str(count))

# Get current time (UTC, formatted)
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Generate HTML
html = f"""
<!DOCTYPE html>
<html>
  <head>
    <title>Auto-Updating Site</title>
  </head>
  <body>
    <h1>🚀 This site has been updated {count} times!</h1>
    <p>⏰ Current UTC time: {now}</p>
    <p>📅 Last update count: {count}</p>
  </body>
</html>
"""

# Write HTML
with open("index.html", "w") as f:
    f.write(html)
