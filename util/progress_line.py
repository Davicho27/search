
def line_line(pathone):
    f = open (pathone, "r")
    while(True):
        linea = f.readline()
        print(linea)
        if not linea:
            break
    f.close()