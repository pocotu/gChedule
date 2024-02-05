import numpy as np

class Agenda:
    def __init__(self, idCurso, idClase, idDocente, idSalon, diaSemana, horario):

        self.idCurso = idCurso
        self.idClase = idClase
        self.idDocente = idDocente

        self.idSalon = idSalon
        self.diaSemana = diaSemana
        self.horario = horario

def CostoHorario(poblacion, elite):

    conflictos = []
    n = len(poblacion[0]) 

    for p in poblacion:
        conflicto = 0

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # Compara el id del salon, el dia de la semana y el horario
                if (
                    p[i].idSalon == p[j].idSalon and 
                    p[i].diaSemana == p[j].diaSemana and 
                    p[i].horario == p[j].horario
                ):
                    conflicto += 1
                    print(f'==== conflicto en Salon: {p[i].idSalon}, Dia: {p[i].diaSemana}, Hora: {p[i].horario}')
                    #print(f'\033[93m==== conflicto en Salon: {conflicto.idSalon}, Dia: {conflicto.diaSemana}, Hora: {conflicto.horario}\033[0m')

                # Compara el id de la clase, el dia de la semana y el horario
                if (
                    p[i].idClase == p[j].idClase and 
                    p[i].diaSemana == p[j].diaSemana and 
                    p[i].horario == p[j].horario
                ):
                    conflicto += 1
                    print(f'==== conflicto en Clase: {p[i].idClase }, Dia: {p[i].diaSemana}, Hora: {p[i].horario}')

                # Compara el id del docente, el dia de la semana y el horario
                if (
                    p[i].idDocente == p[j].idDocente and 
                    p[i].diaSemana == p[j].diaSemana and 
                    p[i].horario == p[j].horario
                ):
                    conflicto += 1
                    print(f'==== conflicto en Docente: {p[i].idDocente}, Dia {p[i].diaSemana}, Hora: {p[i].horario}')

                # Compara el id de la clase, el id del curso y el dia de la semana
                if (
                    p[i].idClase == p[j].idClase and 
                    p[i].idCurso == p[j].idCurso and 
                    p[i].diaSemana == p[j].diaSemana
                ):
                    conflicto += 1
                    print(f'==== conflicto en Clase: {p[i].idClase}, Curso: {p[i].idCurso}, Dia: {p[i].diaSemana}')

        conflictos.append(conflicto)  # Agrega el numero de conflictos para este horario a la lista

    # Ordena los horarios en funcion de sus conflictos en orden ascendente
    indice = np.array(conflictos).argsort()

    # Devuelve los indices de los horarios elite (los menos conflictivos) y el numero de conflictos del mejor horario
    return indice[: elite], conflictos[indice[0]]