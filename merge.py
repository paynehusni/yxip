import requests

urls = [
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestcf.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt"
]

merged_content = ""

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是200,则抛出异常
        lines = response.text.strip().split("\n")
        
        if "bestcf" in url:
            suffix = ":8433#bestcf"
        elif "bestproxy" in url:
            suffix = ":8433#bestproxy"
        else:
            suffix = ""
        
        for line in lines:
            merged_content += line + suffix + "\n"
    
    except requests.exceptions.RequestException as e:
        print(f"请求 {url} 时出错: {e}")

with open("yxip.txt", "w") as file:
    file.write(merged_content)