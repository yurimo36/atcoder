import os
import time
import requests
from bs4 import BeautifulSoup

results = requests.get('https://kenkoooo.com/atcoder/atcoder-api/results?user=yurimo36').json()
results_sorted = sorted(results, key=lambda x:x['id'], reverse=True)
i = 0

with open('last_id.txt', 'r') as f:
  last_id = f.read()

for result in results_sorted:
  if result["result"] == "AC":
    id_ = str(result["id"])
    problem_id = result["problem_id"]
    contest_id = result["contest_id"]
    language = result["language"]

    if i == 0:
      with open('last_id.txt', mode='w') as f:
        f.write(id_)
    if id_ == last_id:
      break

    url = "https://atcoder.jp/contests/" + contest_id + "/submissions/" + id_
    print(url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    code = soup.select_one("pre").text#.rstrip("\n")
    url = "https://atcoder.jp/contests/" + contest_id + "/tasks/" + problem_id

    if not os.path.exists(contest_id):
      os.mkdir(contest_id)

    path = contest_id + "/" + problem_id
    if language[0:2] == "Py":
      path += ".py"
      code = "# "+ url + "\n\n" + code #+ "\n"
    else:
      path += ".cpp"
      code = "// "+ url + "\n\n" + code #+ "\n"

    with open(path, mode='w') as f:
      f.write(code)

    i += 1
    time.sleep(1)

print("\nfinish!!\ntotal:", i)
