import winsound 

class NotaMusical:

    def separarNota(notaCompleta):
        #separar la nota y la escala
        notaCompleta=notaCompleta.lower().strip()
        if notaCompleta.find("sol")>=0:
            if len(notaCompleta)==4:
                #ejemplo sol5
                nota=notaCompleta[:3] #sol
                escala=int(notaCompleta[3:]) #5
            else:
                #ejemplo sol#5
                nota=notaCompleta[:4] #sol#
                escala=int(notaCompleta[4:]) #5
        else:
            if len(notaCompleta)==3:
                #ejemplo fa6
                nota=notaCompleta[:2] #fa
                escala=int(notaCompleta[2:]) #6
            else:
                #ejemplo mi#3
                nota=notaCompleta[:3] #mi#
                escala=int(notaCompleta[3:]) #3
        return [nota, escala]

    def __init__(varClase, notaCompleta, figura):
        sn = NotaMusical.separarNota(notaCompleta)
        varClase.nota = sn[0]
        varClase.escala = sn[1]

        notas = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
        valorD = []
        d = -9
        for n in notas:
            valorD.append(d)
            d += 1

        dNotas = dict(zip(notas, valorD))

        varClase.d = dNotas[varClase.nota]
        if varClase.escala < 3:
            varClase.d -= (3 - varClase.escala) * 12
        else:
            varClase.d += varClase.escala * 12

        t = 4000 # tiempo en milesimas de segundo

        figuras = ["semicorchea", "corchea", "negra", "blanca", "redonda"]
        tiempos = [16, 8, 4, 2, 1]

        dFiguras = dict(zip(figuras, tiempos))
        varClase.tiempo = int(t / dFiguras[figura.lower().strip()])

    def obtenerFrecuencia(varClase):
        r = 1.0594630943593
        return int(440 * r ** varClase.d)

    def reproducir(varClase):
        hz = varClase.obtenerFrecuencia()
        #reproducir
        winsound.Beep(hz, varClase.tiempo)

