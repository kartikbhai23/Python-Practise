# Day 27: HTTP requests
# fetching user details from online APIs using requests module

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    print("HTTP Code Status:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        print("\nPost Title:", data.get("title"))
        print("Post Body:", data.get("body")[:50], "...")
    else:
        print("Fetch failed!")
except requests.exceptions.RequestException as e:
    print("Connection error:", e)

# exercise 1: fetch name list
try:
    users_url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(users_url, timeout=5)
    if res.status_code == 200:
        users = res.json()
        print("First user:", users[0]["name"])
except Exception as e:
    print("Fetch error:", e)

# challenge: website status checker
def is_website_up(test_url):
    try:
        res = requests.head(test_url, timeout=3)
        return res.status_code == 200
    except requests.RequestException:
        return False

print("Is github.com active?", is_website_up("https://github.com"))
print("Is bogus link active?", is_website_up("http://non_existent_site.local"))
