from bs4 import BeautifulSoup
import tkinter
import sqlite3
import urllib.request
import re

class objectDB():
    def __init__(self, titulo, tituloOriginal, pais, fechaEstreno, director, generos):
        self.titulo = titulo
        self.tituloOriginal = tituloOriginal
        self.pais = pais
        self.fechaEstreno = fechaEstreno
        self.director = director
        self.generos = generos
    def toString(self):
        return 'Titulo: ' + self.titulo + '. Titulo original: ' + self.tituloOriginal + ' (' + self.pais + '). Fecha de estreno: ' + self.fechaEstreno + '. Dirigida por: ' + self.director + '. Generos: ' + str(self.generos) + '.'
        


class DB:
    
    #Crea la base de datos y la tabla que vamos a usar  
    def __init__(self, name = "database.db"):
            self.name = name
            connection = sqlite3.connect(self.name)
            connection.execute('''DROP TABLE IF EXISTS PELICULA;''')
            connection.execute('''CREATE TABLE PELICULA
                  (ID INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
                  TITULO           TEXT    NOT NULL,
                  TITULOORIGINAL   TEXT,
                  PAIS             TEXT,
                  FECHAESTRENO     TEXT,
                  DIRECTOR         TEXT,
                  GENEROS          TEXT);''')
            connection.close()

    #Insert con todos los parametros
    def insert(self, titulo, tituloOriginal, pais, fechaEstreno, director, generos):
            connection = sqlite3.connect(self.name)

            template = """INSERT INTO PELICULA (TITULO, TITULOORIGINAL, PAIS, FECHAESTRENO, DIRECTOR, GENEROS) VALUES ("{titulo}","{tituloOriginal}","{pais}","{fechaEstreno}","{director}","{generos}");"""
            conversion = ",".join(map(str,generos))
            print(conversion)
            formatted_string = template.format(titulo = titulo, tituloOriginal = tituloOriginal, pais = pais, fechaEstreno = fechaEstreno, director = director, generos = conversion)
            print("SQL: " + formatted_string)
            connection.execute(formatted_string)
            connection.commit()
            connection.close()

    #Select todos los objetos. Devuelve una lista con todos los objetos
    def select(self):
            lista = list()
            connection = sqlite3.connect(self.name)
            res = connection.execute("""SELECT * FROM PELICULA;""")
            for obj in res:
                  print(obj)
                  lista.append(objectDB(obj[1],obj[2],obj[3],obj[4],obj[5],obj[6].split(",")))
            connection.close()
            return lista        
    
    def selectByGenero(self, genero):
            lista = list()
            connection = sqlite3.connect(self.name)
            template = """SELECT * FROM PELICULA WHERE GENEROS LIKE "%{genero}%";"""
            formatted_string = template.format(genero = genero)
            res = connection.execute(formatted_string)
            for obj in res:
                  print(obj)
                  lista.append(objectDB(obj[1],obj[2],obj[3],obj[4],obj[5],obj[6].split(",")))
            connection.close()
            return lista    


def scrap():
    listaRes = list()

    #descargar web como 'main.html'
    urllib.request.urlretrieve('https://www.elseptimoarte.net/estrenos/','main.html')
    html_doc = open('main.html','r')
    #Abrimos usando el parser 'html.parser'
    soup = BeautifulSoup(html_doc, 'html.parser')

    small_soup = soup.find('section', id = "collections")
    small_soup = small_soup.find('ul', class_ = "elements")

    for article in small_soup.find_all('li'):
        try:
            pais = ""
            link = 'https://www.elseptimoarte.net' + article.find('a')['href']
            
            urllib.request.urlretrieve(link,'temp.html')
            temp_html = open('temp.html','r')
            soup2 = BeautifulSoup(temp_html, 'html.parser')
            small_soup2 = soup2.find('section', class_ = 'highlight')

            for film in small_soup2.find_all('dt'):
                if film.string == "Título":  
                    titulo = film.find_next().string        
                    #print(titulo)
                
                if film.string == "Título original":
                    tituloOriginal = film.find_next().string        
                    #print(tituloOriginal)
                
                if film.string == "País":
                    for a in film.find_next().find_all('a'):
                        pais = pais + " " + a.string        
                    #print(pais)
                
                if film.string == "Estreno en España":
                    fechaEstreno = film.find_next().string        
                    #print(fechaEstreno)
                
                if film.string == "Director":
                    director = film.find_next().a.string    
                    #print(director)
                

            generos = article.find('p', class_ = 'generos').string
            #print(generos)

            objeto = objectDB(titulo, tituloOriginal, pais, fechaEstreno, director, generos)
            listaRes.append(objeto)
            
        except Exception:
            print("Error en la extraccion!")

        

    return listaRes

def main():
    lista = scrap()

    for elemento in lista:
        print(elemento.toString())

if __name__ == "__main__":
    main()