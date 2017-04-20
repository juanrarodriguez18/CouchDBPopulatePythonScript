# encoding=utf8
import sys
import urllib2

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


def leer_fichero(file):
    f = open(file, "r")
    s = f.read()
    f.close()
    return s

peliculas = leer_fichero("peliculasDocuments.json").splitlines()
i = 0
fallos = 0
printProgress(i, 8154, prefix='Progress:', suffix='Complete', barLength=50)

for p in peliculas:
    data = str(p)
    url = 'http://127.0.0.1:5984/peliculas'
    try:
	    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	    f = urllib2.urlopen(req)
	    #for x in f:
	    #	print(x)
	    #f.close()
	    i = i + 1
    except:
            fallos = fallos + 1
    printProgress(i, 8154, prefix='Progress:', suffix='Complete', barLength=50)

print("\n\n Fallos:"+str(fallos))