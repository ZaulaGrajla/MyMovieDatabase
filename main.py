from actors.actors import Actor
from movies.movies import Movie





# harrison=Actor("Harrison","Ford",1942,"USA")
# indiana = Movie("Raiders of the lost ark", 1980)
# # harrison.filmography.add_movie(indiana, "Indiana Jones")
#
harrison = Actor('Harrison', "Ford",1942, "USA")
indiana = Movie("Raiders of the lost ark","adventure", 1980)
indiana2 = Movie("Temple of doom", "adventure",1980)
indiana3 = Movie("Indiana Jones and the last Crusade", "adventure",1989)
starwarsy=Movie("Star Wars: Episode IV New Hope", "fantasy",1977)
# indiana.add_cast(harrison, "Indiana Jones")
# indiana.show_cast()
# print(indiana)
print(indiana.get_title())
# harrison.filmography.add_movie(indiana,"Indiana Jones")
# harrison.filmography.add_movie(indiana2,"Indiana Jones")
# harrison.filmography.add_movie(indiana3,"Indiana Jones")
# harrison.filmography.add_movie(starwarsy,"Han Solo")
#
harrison.filmography.print_filmography()
print(harrison.filmography.active_years)
indiana.add_cast(harrison,"Indiana Jones")
willie=Actor("Cate","Spielberg",1960,"USA","Female")
indiana.add_cast(willie,"Willie Scott")
# harrison.filmography.print_filmography()
indiana.show_cast()

