
def line_line(pathone, pathtwo):
    f = open (pathone, "r")
    ft = open (pathtwo, "r")
    lineaOne = f.readlines()
    lineaDos = ft.readlines()
    for linea in lineaOne:
        print(linea.strip())
        for lineat in lineaDos:
            primero = lineat
            segundo = linea.strip()
            if(segundo in primero):
                print(lineat)
    f.close()