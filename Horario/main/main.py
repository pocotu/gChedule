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
        Agenda('Algebra Lineal',        '103', 'Ines'),
        Agenda('Algebra Lineal',        '103', 'Ines'),
        Agenda('Matematica 1',          '102', 'Donato'),
        Agenda('Matematica 1',          '102', 'Donato'),
        Agenda('Sociedad y Cultura',    '201', 'Edwin'),
        Agenda('Sociedad y Cultura',    '201', 'Edwin'),
        Agenda('Redaccion de textos',   '101', 'Carla'),
        Agenda('Redaccion de textos',   '101', 'Carla'),

        Agenda('Matematica 1',          '102', 'Donato'),
        Agenda('Matematica 1',          '102', 'Donato'),
        Agenda('Filosofia',             '101', 'Jose'),
        Agenda('Filosofia',             '101', 'Jose'),
        Agenda('Redaccion de textos',   '101', 'Carla'),
        Agenda('Redaccion de textos',   '101', 'Carla'),

        Agenda('Sociedad y Cultura',    '201', 'Edwin'),
        Agenda('Sociedad y Cultura',    '201', 'Edwin'),
        Agenda('Filosofia',             '101', 'Jose'),
        Agenda('Filosofia',             '101', 'Jose'),
        Agenda('Coro',                  '108', 'Ray'),
        Agenda('Coro',                  '108', 'Ray'),
        Agenda('Redaccion de textos',   '101', 'Carla'),
        Agenda('Redaccion de textos',   '101', 'Carla')
    ]

    return horarios

if __name__ == '__main__':
#    horarios = []
    horarios = cargar_horarios()  # Se cargan los horarios disponibles desde un archivo de texto   

    ga = OptimizadorGenetico(tam_poblacion=50, elite=10, max_iteraciones=10000)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, 3)  

    vis(resultado)
