# 事前準備
# https://kenkoooo.com/atcoder/#/user/yurimo36?userPageTab=Submissions で
# All表示 & Status選択 をして、開発者ツールを使って tbody のHTMLをコピーして、
# それを scrap.html にペーストする

import os
import time
import requests
from bs4 import BeautifulSoup

with open ('scrap.html', 'r') as f:
  html = f.read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a")

with open('last_url.txt', 'r') as f:
  last_url = f.read()
i = 0

for link in links:
  if "Detail" in link.text.splitlines()[0]:
    url = link["href"]
    if i == 0:
      with open('last_url.txt', mode='w') as f:
        f.write(url)
    if url == last_url:
      break

    print(url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    code = soup.select_one("pre").text#.rstrip("\n")
    contest = url.split("/")[4]

    for tr in soup.select("tr")[:5]:
      if tr.select_one("th").text == "Task":
        difficulty = tr.select_one("td").text[0].lower()
        url = "https://atcoder.jp" + tr.select_one("a")["href"]
      if tr.select_one("th").text == "Language":
        language  = tr.select_one("td").text

    path = contest + "/" + difficulty

    if language[0:2] == "Py":
      path += ".py"
      code = "# "+ url + "\n\n" + code #+ "\n"
    else:
      path += ".cpp"
      code = "// "+ url + "\n\n" + code #+ "\n"

    if not os.path.exists(contest):
      os.mkdir(contest)

    with open(path, mode='w') as f:
      f.write(code)

    i += 1
    time.sleep(1)

print("\nfinish!!\ntotal:", i)
