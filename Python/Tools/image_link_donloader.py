import requests
r = requests.get("https://images.unsplash.com/photo-1511300636408-a63a89df3482?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjJ8fGRlc2t0b3AlMjB3YWxscGFwZXJ8ZW58MHx8MHx8fDA%3D")

with open("images/image.jpg", "wb") as f:
    f.write(r.content)

if r.status_code == 200:
    print("Image downloaded successfully.")
else:
    print("Failed to download image.")