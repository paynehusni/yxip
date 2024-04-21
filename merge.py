import requests

urls = [
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestcf.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt"
]

merged_content = ""

for url in urls:
    response = requests.get(url)
    merged_content += response.text + "\n"

with open("yxip.txt", "w") as file:
    file.write(merged_content)
