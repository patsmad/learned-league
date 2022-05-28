from util.request import soupifyURL
from util.data_cache import openJson, saveJson

class LLQuestionScraper:
    def __init__(self):
        self.cache = openJson('data/question.json')

    def save(self):
        saveJson(self.cache, 'data/question.json')

    def scrape(self, season, match_day, question):
        s = str(season)
        m = str(match_day)
        q = str(question)
        if s not in self.cache:
            self.cache[s] = {}
        if m not in self.cache[s]:
            self.cache[s][m] = {}
        if q not in self.cache[s][m]:
            print(f'Scraping {s}-{m}-{q}')
            self.cache[s][m][q] = LLQuestion(s, m, q).get_data()
            self.save()
        return self.cache[s][m][q]

    def scrape_season(self, season):
        for match_day in range(1, 26):
            for question in range(1, 7):
                self.scrape(season, match_day, question)

class LLQuestion:
    def __init__(self, season, match_day, question):
        self.season = season
        self.match_day = match_day
        self.question = question
        self.soup = None
        self.data = None

    def get_soup(self):
        if self.soup is None:
            self.soup = soupifyURL(f'https://www.learnedleague.com/question.php?{self.season}&{self.match_day}&{self.question}')
        return self.soup

    def set_data(self):
        soup = self.get_soup()
        self.data = {
            'question': soup.find('div', 'indivqQuestion').text.strip(),
            'answer': soup.find('div', {'id': 'xyz'}).text.strip(),
            'correct': int([a for a in soup.find_all('h3') if a.text == 'Leaguewide Correct %'][0].find_next('div').text.strip().replace('%', '')) / 100
        }

    def get_data(self):
        if self.data is None:
            self.set_data()
        return self.data
