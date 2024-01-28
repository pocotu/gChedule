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

def cargar_horarios():
    horarios = [
        Agenda('Algebra Lineal',        1201, 11101),
        Agenda('Algebra Lineal',        1201, 11101),
        Agenda('Matematica 1',          1201, 11102),
        Agenda('Matematica 1',          1201, 11102),
        Agenda('Sociedad y Cultura',    1201, 11103),
        Agenda('Sociedad y Cultura',    1201, 11103),
        Agenda('Redaccion de textos',   1201, 11106),
        Agenda('Redaccion de textos',   1201, 11106),

        Agenda('Matematica 1',          1202, 11102),
        Agenda('Matematica 1',          1202, 11102),
        Agenda('Filosofia',             1202, 11104),
        Agenda('Filosofia',             1202, 11104),
        Agenda('Redaccion de textos',   1202, 11106),
        Agenda('Redaccion de textos',   1202, 11106),

        Agenda('Sociedad y Cultura',    1203, 11103),
        Agenda('Sociedad y Cultura',    1203, 11103),
        Agenda('Filosofia',             1203, 11104),
        Agenda('Filosofia',             1203, 11104),
        Agenda('Coro',                  1203, 11105),
        Agenda('Coro',                  1203, 11105),
        Agenda('Redaccion de textos',   1203, 11106),
        Agenda('Redaccion de textos',   1203, 11106),

#        Agenda('Algebra Lineal',        1204, 11101),
#        Agenda('Algebra Lineal',        1204, 11101),
#        Agenda('Matematica 1',          1204, 11102),
#        Agenda('Matematica 1',          1204, 11102),
#        Agenda('Sociedad y Cultura',    1204, 11103),
#        Agenda('Sociedad y Cultura',    1204, 11103),
#        Agenda('Redaccion de textos',   1204, 11106),
#        Agenda('Redaccion de textos',   1204, 11106)

    ]

    return horarios

if __name__ == '__main__':
#    horarios = []
    horarios = cargar_horarios()  # Se cargan los horarios disponibles desde un archivo de texto   
    # los parametros son: idCurso, idClase, idDocente

#    horarios.append(Agenda('Algebra Lineal',        1201, 11101))
#    horarios.append(Agenda('Algebra Lineal',        1201, 11101))
#    horarios.append(Agenda('Matematica 1',          1201, 11102))
#    horarios.append(Agenda('Matematica 1',          1201, 11102))
#    horarios.append(Agenda('Sociedad y Cultura',    1201, 11103))
#    horarios.append(Agenda('Sociedad y Cultura',    1201, 11103))
#    horarios.append(Agenda('Redaccion de textos',   1201, 11106))
#    horarios.append(Agenda('Redaccion de textos',   1201, 11106))
#
#    horarios.append(Agenda('Matematica 1',          1202, 11102))
#    horarios.append(Agenda('Matematica 1',          1202, 11102))
#    horarios.append(Agenda('Filosofia',             1202, 11104))
#    horarios.append(Agenda('Filosofia',             1202, 11104))
#    horarios.append(Agenda('Redaccion de textos',   1202, 11106))
#    horarios.append(Agenda('Redaccion de textos',   1202, 11106))
#
#    horarios.append(Agenda('Sociedad y Cultura',    1203, 11103))
#    horarios.append(Agenda('Sociedad y Cultura',    1203, 11103))
#    horarios.append(Agenda('Filosofia',             1203, 11104))
#    horarios.append(Agenda('Filosofia',             1203, 11104))
#    horarios.append(Agenda('Coro',                  1203, 11105))
#    horarios.append(Agenda('Coro',                  1203, 11105))
#    horarios.append(Agenda('Redaccion de textos',   1203, 11106))
#    horarios.append(Agenda('Redaccion de textos',   1203, 11106))
    

    ga = OptimizadorGenetico(tam_poblacion=50, elite=10, max_iteraciones=10000)  # Se crea una instancia del Optimizador Genetico.

    # Se ejecuta el algoritmo genetico para encontrar un horario optimo, donde 3
    # es el rango de valores para el id del salon.
    resultado = ga.Evolucion(horarios, 3)  

#    horario_visualizado = []
#    for r in resultado:
#        if r.idClase == 1203:
#            horario_visualizado.append(r)  # Se seleccionan los horarios especificos de la clase 1203.
#
#    vis(horario_visualizado)  # Se visualiza el horario resultante.
    vis(resultado)
