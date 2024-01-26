import prettytable 

from horario import Agenda
from alg_genetico import OptimizadorGenetico

def vis(VHorario):
    etiqueta_colum = ['Hora', '1', '2', '3', '4', '5']  # Etiquetas de las columnas (horas y dias)
    tabla_valores = [[i + 1, '', '', '', '', ''] for i in range(5)]  # Inicializa una matriz de valores en blanco

    tabla = prettytable.PrettyTable(etiqueta_colum, hrules=prettytable.ALL)  # Crea una tabla con las etiquetas y bordes

    for s in VHorario:
        diaSemana = s.diaSemana
        horario = s.horario
        texto = 'curso: {} \n clase: {} \n salon: {} \n Profesor: {}'.format(s.idCurso, s.idClase, s.idSalon, s.idDocente)
        tabla_valores[diaSemana - 1][horario] = texto

    for row in tabla_valores:
        tabla.add_row(row)  # Agrega cada fila de la matriz a la tabla

    print(tabla)

if __name__ == '__main__':
    horarios = []

    horarios.append(Agenda(201, 1201, 11101))
    horarios.append(Agenda(201, 1201, 11101))
    horarios.append(Agenda(202, 1201, 11102))
    horarios.append(Agenda(202, 1201, 11102))
    horarios.append(Agenda(203, 1201, 11103))
    horarios.append(Agenda(203, 1201, 11103))
    horarios.append(Agenda(206, 1201, 11106))
    horarios.append(Agenda(206, 1201, 11106))

    horarios.append(Agenda(202, 1202, 11102))
    horarios.append(Agenda(202, 1202, 11102))
    horarios.append(Agenda(204, 1202, 11104))
    horarios.append(Agenda(204, 1202, 11104))
    horarios.append(Agenda(206, 1202, 11106))
    horarios.append(Agenda(206, 1202, 11106))

    horarios.append(Agenda(203, 1203, 11103))
    horarios.append(Agenda(203, 1203, 11103))
    horarios.append(Agenda(204, 1203, 11104))
    horarios.append(Agenda(204, 1203, 11104))
    horarios.append(Agenda(205, 1203, 11105))
    horarios.append(Agenda(205, 1203, 11105))
    horarios.append(Agenda(206, 1203, 11106))
    horarios.append(Agenda(206, 1203, 11106))
    

    ga = OptimizadorGenetico(tam_poblacion=50, elite=10, max_iteraciones=500)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, 3)  # Se ejecuta el algoritmo genetico para encontrar un horario optimo.

    horario_visualizado = []
    for r in resultado:
        if r.idClase == 1203:
            horario_visualizado.append(r)  # Se seleccionan los horarios especificos de la clase 1203.

    vis(horario_visualizado)  # Se visualiza el horario resultante.
