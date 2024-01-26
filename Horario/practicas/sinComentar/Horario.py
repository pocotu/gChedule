import numpy as np

class Agenda:
    def __init__(self, idCurso, idClase, idDocente):
        self.idCurso = idCurso
        self.idClase = idClase
        self.idDocente = idDocente

        self.idSalon = 0
        self.diaSemana = 0
        self.horario = 0

    def Inicializador_aleatorio(self, salonRango):
        self.idSalon = np.random.randint(1, salonRango + 1, 1)[0]
        self.diaSemana = np.random.randint(1, 6, 1)[0]
        self.horario = np.random.randint(1, 6, 1)[0]


def CostoHorario(poblacion, elite):
    conflictos = []
    n = len(poblacion[0])

    for p in poblacion:
        conflicto = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if p[i].idSalon == p[j].idSalon and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1
                if p[i].idClase == p[j].idClase and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1
                if p[i].idDocente == p[j].idDocente and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1
                if p[i].idClase == p[j].idClase and p[i].idCurso == p[j].idCurso and p[i].diaSemana == p[j].diaSemana:
                    conflicto += 1

        conflictos.append(conflicto)

    indice = np.array(conflictos).argsort()

    return indice[: elite], conflictos[indice[0]]
