from util.request import soupifyURL

url = 'https://www.learnedleague.com/match.php?67&1&Valley'
soup = soupifyURL(url)

qs = soup.find_all('div', 'ind-Q20')
for q in qs:
    answer = q.find_next('div', 'a-red')
    print(q.text.strip())
    print(answer.text.strip())
