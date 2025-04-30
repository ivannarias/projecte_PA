from pelicula import Pelicula
from llibre import Llibre

class Items():
    def __init__(self):
        self._dic_movies = {}
        self._dic_books = {}

    def llegir_fitxer_movies(self, nom_fitxer):
        with open (nom_fitxer, "r") as fitxer:
            for linia in fitxer:
                movie = linia.split(",")
                id = movie[0]
                title = movie[1]
                geners = movie[2:]
                peli = Pelicula(id, title, geners)
                self._dic_movies[id] = peli
    
        def llegir_fitxer_books(self, nom_fitxer):
            with open (nom_fitxer, "r") as fitxer:
                for linia in fitxer:
                    book = linia.split(",")
                    isbn = movie[0]
                    title = movie[1]
                    author =  movie[2]
                    year_publication = int(movie[3])
                    publisher = movie[4]
                    llibre = Llibre(id, title, geners)
                    self._dic_movies[id] = peli