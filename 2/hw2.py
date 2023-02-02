class Film:
    def __init__(self, name, year, director, collecting, long, rating):
        self.name = name
        self.year = year
        self.director = director
        self.collecting = collecting
        self.long = long
        self.rating = rating

    def get_name(self):
        print(self.name)

    def change_name(self):
        a = input()
        self.name = a
        print(f'Название фильма стало: {a}')

    def get_director(self):
        print(self.director)

    def show_info(self):
        print(f'{self.name} ;\n{self.year} ;\n{self.collecting}')

class Anime(Film):
    def __init__(self, name, year, director, collecting, long, rating, manga, opening_title, ending_title):
        super().__init__(name, year, director, collecting, long, rating)
        self.manga = manga
        self.opening_title = opening_title
        self.ending_title = ending_title

    def get_manga(self):
        print(self.manga)

    def show_info(self):
        print(f'{self.name} ;\n{self.year} ;\n{self.collecting} ;\n{self.manga} ;\n{self.opening_title}')


film = Film('Star wars 3', '2005', 'George Lucas', '380270577 $', '140 min', '10/10')
film.get_director()
film.show_info()
film.change_name()
print('')

anime = Anime('Naruto', '2005', 'Kisimoto', '2949185 $', 'too many', '10/10', 'Naruto', 'Rocks', 'Wind')
anime.get_manga()
print('')
anime.show_info()