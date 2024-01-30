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
    # Orden de los parametros: Agenda(idCurso, idClase, idDocente)
    horarios = [
        Agenda('Algebra Lineal',        103, 11101),
        Agenda('Algebra Lineal',        103, 11101),
        Agenda('Matematica 1',          102, 11102),
        Agenda('Matematica 1',          102, 11102),
        Agenda('Sociedad y Cultura',    201, 11103),
        Agenda('Sociedad y Cultura',    201, 11103),
        Agenda('Redaccion de textos',   101, 11106),
        Agenda('Redaccion de textos',   101, 11106),

        Agenda('Matematica 1',          102, 11102),
        Agenda('Matematica 1',          102, 11102),
        Agenda('Filosofia',             101, 11104),
        Agenda('Filosofia',             101, 11104),
        Agenda('Redaccion de textos',   101, 11106),
        Agenda('Redaccion de textos',   101, 11106),

        Agenda('Sociedad y Cultura',    201, 11103),
        Agenda('Sociedad y Cultura',    201, 11103),
        Agenda('Filosofia',             101, 11104),
        Agenda('Filosofia',             101, 11104),
        Agenda('Coro',                  108, 11105),
        Agenda('Coro',                  108, 11105),
        Agenda('Redaccion de textos',   101, 11106),
        Agenda('Redaccion de textos',   101, 11106)
    ]

    return horarios

if __name__ == '__main__':
    horarios = cargar_horarios()  # Se cargan los horarios disponibles desde un archivo de texto   

    ga = OptimizadorGenetico(tam_poblacion=100, elite=20, max_iteraciones=10000)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, salonRango=200)

    vis(resultado)
