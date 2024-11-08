### 无需使用cookie等身份认证，即可检查域名是否可使用
    构造 url = f"http://freedomain.one/tools/pub.jsp?class=FreeDomainSrvBean&actioncode=2&subdomain={subdomain}&domains={domain}"
    subdomain用的终端输入，domain为网站所有的几个后缀。
    将可用的域名保存到txt中(追加,利用remove_duplicates.py去重)
    
