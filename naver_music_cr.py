import requests
from bs4 import BeautifulSoup

r = requests.get("https://music.bugs.co.kr/chart")
bs = BeautifulSoup(r.content, "html.parser")

# 가수의 목록
# 노래의 목록

song_name = []
artist_name = []

song = bs.select("th > p.title > a")
artist = bs.select("td.left > p.artist > a")

for s in range(len(song)):
    song_name.append(song[s].text)

for a in range(len(song)):
    artist_name.append(artist[a].text)   

for i in range(0, 9):
    print(f"순위 0{i+1}위 - 가수 : {artist_name[i].strip()} - 곡명 : {song_name[i]}")

for i in range(9, 50):
    print(f"순위 {i+1}위 - 가수 : {artist_name[i].strip()} - 곡명 : {song_name[i]}")
