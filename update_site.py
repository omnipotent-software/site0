from datetime import datetime

# Generate updated HTML content with current UTC timestamp
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

html_content = f"""
<!DOCTYPE html>
<html>
  <head>
    <title>Auto-Updating Site</title>
  </head>
  <body>
    <h1>Last updated: {timestamp}</h1>
  </body>
</html>
"""

# Overwrite index.html with new content
with open("index.html", "w") as f:
    f.write(html_content)
