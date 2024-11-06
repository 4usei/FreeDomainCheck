import requests
from concurrent.futures import ThreadPoolExecutor

def check_domain_availability(subdomain, domain):
    # 构造请求 URL
    url = f"http://freedomain.one/tools/pub.jsp?class=FreeDomainSrvBean&actioncode=2&subdomain={subdomain}&domains={domain}"

    try:
        # 发送 GET 请求
        response = requests.get(url)

        # 检查响应状态
        if response.status_code == 200:
            # 获取返回内容
            content = response.text

            # 判断域名是否可用
            if "Not Available" in content:
                return f"{subdomain}.{domain} X"  # 不可用
            elif "Available" in content:
                return f"{subdomain}.{domain} √"  # 可用
            else:
                return f"{subdomain}.{domain}: Unexpected response content."
        else:
            return f"Failed to retrieve data for {domain}: {response.status_code}"

    except requests.RequestException as e:
        return f"An error occurred for {domain}: {e}"

if __name__ == "__main__":
    # 域名列表
    domains = [
        "work.gd",
        "publicvm.com",
        "run.place",
        "linkpc.net",
        "line.pm"
    ]

    while True:
        # 在控制台手动输入 subdomain
        subdomain = input("请输入子域名（或输入 '!' 退出）：")
        if subdomain.lower() == '!':
            break  # 退出循环

        # 使用 ThreadPoolExecutor 并发检查域名
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(check_domain_availability, subdomain, domain): domain for domain in domains}

        # 输出结果并对齐
        for future in futures:
            result = future.result()
            print(result.ljust(30))  # 使用 ljust 进行格式化对齐

            # 如果域名可用，保存到文件中
            if "√" in result:
                with open("available_domains.txt", "a") as f:  # 以追加模式打开文件
                    f.write(f"{subdomain}.{futures[future]}\n")


    print("所有可用域名已保存到 available_domains.txt")