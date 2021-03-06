from actors import Actor


class Cast:
    def __init__(self):
        self.cast = {}

    def set_director(self, director):
        self.cast[director] = director.get_name()

    def add_to_cast(self, actor, role):
        self.cast[actor] = role

    def remove_from_cast(self, actor):
        del self.cast[actor]

    def print_cast(self):
        for actor, role in self.cast.items():
            print('%20s as %s' % (actor.get_name(), role))


class Movie:
    MOVIE_TYPES = [
        "comedy",
        "adventure",
        "horror",
        "science fiction",
        "romance",
        "drama",
        "crime",
        "romantic comedy",
        "action",
        "fantasy",
        "melodrama",
        "historic",
        'animated',
        "thriller",
        "musical",
        "western"
    ]

    def __init__(self, title, type_of_movie, year_of_production=None, rate=None):
        self.title = title
        self.year_of_production = year_of_production
        self.description = None
        self.cast = Cast()
        self.rate = rate

        while self.MOVIE_TYPES.count(type_of_movie) == 0:
            print(f'{type_of_movie} is not on the list!')
            print(f"\nWhat kind of movie is {self.title}?")
            print(self.MOVIE_TYPES)
            type_of_movie = (input("Please enter a movie type from above list: "))
        self.type = type_of_movie

    def get_rate(self):
        while not 0 <= self.rate <= 10:
            try:
                self.rate = int(input("This movie has no rate yet. Please rate it. 0 to 10 "))
            except ValueError:
                print("Please input correct value!")
        print(f'My rate: {self.rate}/10')
        return self.rate

    def add_description(self, description: str):
        self.description = description

    def get_year_of_production(self):
        return self.year_of_production

    def get_title(self):
        return self.title

    def add_cast(self, actor, role):
        if isinstance(actor, Actor):
            self.cast.add_to_cast(actor, role)
            actor.filmography.add_movie(self, role)

    def show_cast(self):
        self.cast.print_cast()
        pass

    def introduce_myself(self):
        return f'"{self.get_title()}" is {self.type}.\nThis movie was made in {self.year_of_production}.\nCast:'
