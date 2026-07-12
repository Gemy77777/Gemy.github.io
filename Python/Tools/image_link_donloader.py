import requests
r = requests.get("https://www.nvisia.com/insights/agile-methodology/images/agile-methodology.jpg")

with open("images/image.jpg", "wb") as f:
    f.write(r.content)

if r.status_code == 200:
    print("Image downloaded successfully.")
else:
    print("Failed to download image.")