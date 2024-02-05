import prettytable 

from horario import Agenda
from alg_genetico import OptimizadorGenetico

def vis(VHorario):
    if VHorario is None:
        print('No se encontro un horario sin conflictos')
    else:
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
    # Orden de los parametros: Agenda(idCurso, idClase, idDocente, idSalon, diaSemana, horario)
    horarios = [
        Agenda('Algebra Lineal',        1201, 11101, 103, 3, 4),
        Agenda('Algebra Lineal',        1201, 11101, 103, 3, 4),
        Agenda('Matematica 1',          1201, 11102, 102, 2, 5),
        Agenda('Matematica 1',          1201, 11102, 102, 2, 5),
        Agenda('Sociedad y Cultura',    1201, 11103, 201, 1, 1),
        Agenda('Sociedad y Cultura',    1201, 11103, 201, 1, 1),
        Agenda('Redaccion de textos',   1201, 11106, 101, 4, 3),
        Agenda('Redaccion de textos',   1201, 11106, 101, 4, 3),

        Agenda('Matematica 1',          1202, 11102, 102, 2, 5), 
        Agenda('Matematica 1',          1202, 11102, 102, 2, 5),
        Agenda('Filosofia',             1202, 11104, 101, 3, 1),
        Agenda('Filosofia',             1202, 11104, 101, 3, 1),
        Agenda('Redaccion de textos',   1202, 11106, 101, 4, 3),
        Agenda('Redaccion de textos',   1202, 11106, 101, 4, 3),

        Agenda('Sociedad y Cultura',    1203, 11103, 201, 1, 1),
        Agenda('Sociedad y Cultura',    1203, 11103, 201, 1, 1),
        Agenda('Filosofia',             1203, 11104, 101, 3, 1),
        Agenda('Filosofia',             1203, 11104, 101, 3, 1),
        Agenda('Coro',                  1203, 11105, 108, 5, 2),
        Agenda('Coro',                  1203, 11105, 108, 5, 2),
        Agenda('Redaccion de textos',   1203, 11106, 101, 4, 3),
        Agenda('Redaccion de textos',   1203, 11106, 101, 4, 3)
    ]

    return horarios

if __name__ == '__main__':
    horarios = cargar_horarios()  # Se cargan los horarios disponibles desde un archivo de texto   

    ga = OptimizadorGenetico(tam_poblacion=100, elite=20, max_iteraciones=10000)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, salonRango=200)

    vis(resultado)
