import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Fronalpstock_big.jpg/640px-Fronalpstock_big.jpg"
output_path = "sample.png"

response = requests.get(url)
if response.status_code == 200:
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print(f"[+] Image saved as '{output_path}'")
else:
    print("[-] Failed to download image")
