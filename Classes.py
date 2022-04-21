from faker import Faker
fake = Faker()
import random


class Films:
    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        # Variables
        self.nr_view = 0

    def play(self, step=1):
        self.nr_view += step

    def str(self):
        return f'{self.title} {self.year}'

    def repr(self):
        return f"Films(title={self.title} year={self.year}, type={self.type}, view={self.nr_view})"


class Series(Films):
    def __init__(self, nr_episode, nr_season, args, kwargs):
        super().__init__(args, kwargs)
        self.nr_episode = nr_episode
        self.nr_season = nr_season

    def str(self):
        return f'{self.title} S{self.nr_season:02}E{self.nr_episode:02}'

    def repr(self):
        return f"Series(title={self.title} year={self.year}, type={self.type}, nr_view={self.nr_view}, nr_episode={self.nr_episode}," \
f"nr_season={self.nr_season})"


films_list =[]


for x in range(10):
    film = Films(title=fake.word(), year=fake.year(), type=fake.word())
    films_list.append(film)
    serie = Series(title=fake.word(), year=fake.year(), type=fake.word(),
    nr_season=fake.random_digit(), nr_episode=fake.random_int(0,20))
    films_list.append(serie)

def get_movies():
    films = []
    for element in film_list:
        if isinstance(element, Film):
            films.append(element)
    return films

def get_series():
    series = []
    for element in series_list:
        if isinstance(element, Series):
            series.append(element)

    return series
   
def search(keyword):
    for element in films_list:
        if element.title == keyword:
          print(keyword)

def generate_views():
    random.shuffle(films_list)
    films_list[0].play()


def multiple():
    for a in range(10):
      generate_views()

def top_titles(nr, content_type):
    if content_type == "filmy":
        get_movies()
        sorted(films_list, key=lambda film: film.nr_view)
            for b in range(nr):
                return films_list[b].title
    if content_type == 2:
        get_series()
        sorted(films_list, key=lambda serie: serie.nr_view)
            for b in range(nr):
                return films_list[b].title

multiple()

print(films_list)
top_titles(1,"filmy")
print(films_list)
