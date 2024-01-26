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
                # Compara el id del salon, el dia de la semana y el horario
                if p[i].idSalon == p[j].idSalon and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id de la clase, el dia de la semana y el horario
                if p[i].idClase == p[j].idClase and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id del docente, el dia de la semana y el horario
                if p[i].idDocente == p[j].idDocente and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Compara el id de la clase, el id del curso y el dia de la semana
                if p[i].idClase == p[j].idClase and p[i].idCurso == p[j].idCurso and p[i].diaSemana == p[j].diaSemana:
                    conflicto += 1

        conflictos.append(conflicto)  # Agrega el numero de conflictos para este horario a la lista

    # Ordena los horarios en funcion de sus conflictos en orden ascendente
    indice = np.array(conflictos).argsort()

    # Devuelve los indices de los horarios elite (los menos conflictivos) y el numero de conflictos del mejor horario
    return indice[: elite], conflictos[indice[0]]
