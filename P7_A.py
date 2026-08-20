import requests
from bs4 import BeautifulSoup

print("Shreyash Kadam S091")

url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

print("\n1. First 3 Paragraphs:")

for p in paragraphs[:3]:
    print(p.get_text(strip=True))

images = soup.find_all("img")

print("\n2. Image Source URLs:")

for img in images:
    print(img.get("src"))


links = soup.find_all("a")

print("\n3. Total Number of Links:")
print(len(links))


headings = soup.find_all(["h1", "h2", "h3"])

print("\n4. Headings:")

for heading in headings:
    print(heading.get_text(strip=True))


print("\n5. Languages:")

languages = soup.select(".central-featured-lang strong")

for language in languages:
    print(language.get_text(strip=True))
