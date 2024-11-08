import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_domain_availability(subdomain, domain):
    url = f"http://freedomain.one/tools/pub.jsp?class=FreeDomainSrvBean&actioncode=2&subdomain={subdomain}&domains={domain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.text
            if "Not Available" in content:
                return f"{subdomain}.{domain} X"
            elif "Available" in content:
                return f"{subdomain}.{domain} √"
            else:
                return f"{subdomain}.{domain}: Unexpected response content."
        else:
            return f"Failed to retrieve data for {domain}: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred for {domain}: {e}"

def main():
    domains = ["work.gd", "publicvm.com", "run.place", "linkpc.net", "line.pm"]

    while True:
        subdomain = input("请输入子域名（或输入 '!' 退出）：")
        if subdomain.lower() == '!':
            break

        results = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_domain = {executor.submit(check_domain_availability, subdomain, domain): domain for domain in domains}
            for future in as_completed(future_to_domain):
                result = future.result()
                results.append(result)
                print(result.ljust(30))
                if "√" in result:
                    with open("available_domains.txt", "a") as f:
                        f.write(f"{result.split()[0]}\n")

    print("所有可用域名已保存到 available_domains.txt")

if __name__ == "__main__":
    main()