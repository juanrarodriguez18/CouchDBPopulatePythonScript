# encoding=utf8
import sys
import time
import json

reload(sys)
sys.setdefaultencoding('utf8')

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

# return [titulo, poster, rating, nvotos, fecha, duracion, pais, director, guion, musica, fotografia, actores, genero, sipnosis]


def extraer_lista(file):
    f = open(file, "r")
    l = f.read()
    f.close()
    return l

def leer_fichero(file):
    f = open(file, "r")
    s = f.read()
    f.close()
    return s

def populatePeliculas():
    print "Populando Peliculas"
    peliculas = leer_fichero("peliculasFinal").splitlines()
    json_line = ""
    i = 0
    printProgress(i, 8154, prefix='Progress:', suffix='Complete', barLength=50)
    f = open("peliculasFinal.json", "a")
    f.write("[")
    for p in peliculas:
        info_pelicula = eval(p)
        if info_pelicula[2]!='--' and info_pelicula[2]!='':
            valoracion_media = info_pelicula[2].replace(",",".")
        else:
            valoracion_media = 0
        if info_pelicula[3]!='':
            votaciones_totales = info_pelicula[3].replace(".","")
        else:
            votaciones_totales = 0
        if info_pelicula[5]!='':
            duracion = info_pelicula[5].split(" ")[0]
        else:
            duracion = 0
        json_line = {
            "titulo": info_pelicula[0].replace('\"'," "),
            "poster": info_pelicula[1].replace('\"'," "),
            "rating": valoracion_media,
            "nvotos": votaciones_totales,
            "fecha":  info_pelicula[4].replace('\"'," "),
            "duracion": duracion,
            "pais": info_pelicula[6].replace('\"'," "),
            "directores": [info_pelicula[7].replace('\"'," ").replace(",",'","')],
            "guion": [info_pelicula[8].replace('\"'," ").replace(",",'","')],
            "musica": [info_pelicula[9].replace('\"'," ").replace(",",'","')],
            "fotografia": [info_pelicula[10].replace('\"'," ").replace(",",'","')],
            "actores": [info_pelicula[11].replace('\"'," ").replace('"',"'").replace(",",'","')],
            "genero": info_pelicula[12].replace('\"'," "),
            "sipnosis": str(info_pelicula[13]).replace("'"," ").replace('"'," ")
        }


        # print(str(json_line).replace("u\'","\'").replace("'",'"'))
        if i < len(peliculas):
            f.write(str(json_line).replace("u\'","\'").replace("'",'"')+",")
            f.write("\n")
        else:
            f.write(str(json_line).replace("u\'", "\'").replace("'", '"'))
        i = i + 1
        printProgress(i, 8154, prefix='Progress:', suffix='Complete', barLength=50)
    f.write("]")
populatePeliculas()