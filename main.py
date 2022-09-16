from bs4 import BeautifulSoup
import requests

web_url = "https://news.ycombinator.com/"
score = []
title = []
link = []

hacker_news = requests.get(url=web_url).text
soup = BeautifulSoup(hacker_news, 'html.parser')

scores = soup.select('.score')
titles = soup.select('.titlelink')
links = soup.find_all(name='a', class_='titlelink')
for i in range(len(scores)):
    score.append(int(scores[i].text[0:2]))
max_score = sorted(score, reverse=True)

for i in range(len(max_score)):
    index = score.index(max_score[i])
    title.append(titles[index].text)
    link.append(links[index].get('href'))

print(max_score)
print(title)
print(link)


# for i in range(len(scores)):
#     max_score[int(scores[i].text[0:2])] = titles[i].text
# max_score = {k: v for k, v in sorted(max_score.items(), key=lambda item: item[0], reverse=True)}
# print(max_score)