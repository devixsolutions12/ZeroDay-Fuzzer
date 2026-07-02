import requests
import random
import time
import string

def generate_payload():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(random.randint(50, 200)))

def fuzz_endpoint(target_url):
    print(f"[*] Starting aggressive fuzzing on: {target_url}")
    headers = {
        "User-Agent": "ZeroDay-Fuzzer/1.0",
        "X-Custom-Bypass": "True"
    }
    
    for i in range(1, 1001):
        payload = generate_payload()
        try:
            # Test query param injection
            res = requests.get(f"{target_url}?id={payload}", headers=headers, timeout=2)
            
            if res.status_code == 500:
                print(f"[!] Server Error (500) detected with payload length: {len(payload)}")
                with open("crash_logs.txt", "a") as f:
                    f.write(f"Payload: {payload}\n")
            
            # Rate limiting evasion logic
            if i % 50 == 0:
                print("[*] Sleeping to evade WAF rate limits...")
                time.sleep(random.uniform(1.0, 3.5))
                
        except requests.exceptions.RequestException as e:
            print(f"[-] Connection dropped during fuzzing: {e}")
            break

if __name__ == "__main__":
    target = input("Enter target API endpoint: ")
    fuzz_endpoint(target)
