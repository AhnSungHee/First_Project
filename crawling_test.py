# requests
# BeautifulSoup

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com/")
bs = BeautifulSoup(r.content, "html.parser")

h3 = bs.select("h3")
# 리스트형으로 반환
h3_1 = bs.select_one("h3")

print(h3)
print(h3_1)
print(h3_1.text)