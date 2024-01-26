import prettytable

from Horario import Agenda
from alg_genetico import OptimizadorGenetico

def vis(VHorario):
    # funcion para visualizar el horario de clases de forma tabular
    etiqueta_colum = ['Hora', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']  # Etiquetas de las columnas (horas y dias)

    # Matriz de valores para la tabla [horas, lunes, martes, miercoles, jueves, viernes
    tabla_valores = [
        ["7 am", "", "", "", "", ""],
        ["8 am", "", "", "", "", ""],
        ["9 am", "", "", "", "", ""],
        ["10 am", "", "", "", "", ""],
        ["11 am", "", "", "", "", ""],
        ["12 pm", "", "", "", "", ""],
    ]

    # Crea una tabla con las etiquetas y bordes
    # etiqueta_colum: etiquetas de las columnas
    # hrules: estilo de los bordes, prettytable.ALL: todos los bordes
    tabla = prettytable.PrettyTable(etiqueta_colum, hrules=prettytable.ALL)

    for s in VHorario:
        # Se obtienen los valores de la clase
        # Se crea un string con la información de la clase
        # Se agrega el string a la matriz en la posición correspondiente
        diaSemana = s.diaSemana
        horario = s.horario
        texto = 'Curso: {} \n Clase: {} \n Salon: {} \n Profesor: {}'.format(s.idCurso, s.idClase, s.idSalon, s.idDocente, s.diaSemana, s.horario)
        tabla_valores[diaSemana - 1][horario] = texto  # Agrega la informacion del horario en la matriz

        # Si 
        if horario == 5:
            tabla_valores[5][diaSemana] = texto  # Agrega la información de la clase en la fila de "12 pm"

    for row in tabla_valores:
        tabla.add_row(row)  # Agrega cada fila de la matriz a la tabla

    print(tabla)  # Imprime la tabla visual del horario

if __name__ == '__main__':
    horarios = []

    ## Se crean instancias de Agenda con diferentes combinaciones de identificadores de curso, clase y docente
    ## se crea una instancia de Agenda por cada clase que se desea programar con los siguientes parametros:
    # idCurso: identificador del curso (nombre del curso)
    # idClase: identificador de la clase (codigo de la clase)
    # idDocente: identificador del docente (nombre del docente)
    # idSalon: identificador del salon (numero del salon)
    # diaSemana: dia de la semana (1: lunes, 2: martes, 3: miercoles, 4: jueves, 5: viernes)
    # horario: horario de la clase (1: 7 am, 2: 8 am, 3: 9 am, 4: 10 am, 5: 11 am, 6: 12 pm)
    horarios.append(Agenda("Algebra",           "IF061AIN", "Docente 1", 101, 1, 1))
    horarios.append(Agenda("Algebra",           "IF061AIN", "Docente 1", 101, 1, 1))
    horarios.append(Agenda("A.D.A.",            "IF061AIN", "Docente 2", 102, 1, 2))
    horarios.append(Agenda("A.D.A.",            "IF061AIN", "Docente 2", 102, 1, 2))
    horarios.append(Agenda("Avanzados",         "IF061AIN", "Docente 3", 103, 1, 3))
    horarios.append(Agenda("Avanzados",         "IF061AIN", "Docente 3", 103, 1, 3))
    horarios.append(Agenda("M. Discreta",       "IF061AIN", "Docente 6", 106, 1, 5)) 
    horarios.append(Agenda("M. Discreta",       "IF061AIN", "Docente 6", 106, 1, 5))

    horarios.append(Agenda("A.D.A.",            "IF484AIN", "Docente 2", 102, 2, 2))
    horarios.append(Agenda("A.D.A.",            "IF484AIN", "Docente 2", 102, 2, 2))
    horarios.append(Agenda("Programacion 1",    "IF484AIN", "Docente 4", 104, 2, 4))
    horarios.append(Agenda("Programacion 1",    "IF484AIN", "Docente 4", 104, 2, 4))
    horarios.append(Agenda("M. Discreta",       "IF484AIN", "Docente 6", 106, 2, 6))
    horarios.append(Agenda("M. Discreta",       "IF484AIN", "Docente 6", 106, 2, 6))

    horarios.append(Agenda("Avanzados",         "IF554AIN", "Docente 3", 103, 3, 3))
    horarios.append(Agenda("Avanzados",         "IF554AIN", "Docente 3", 103, 3, 3))
    horarios.append(Agenda("Programacion 1",    "IF554AIN", "Docente 4", 104, 3, 4))
    horarios.append(Agenda("Programacion 1",    "IF554AIN", "Docente 4", 104, 3, 4))
    horarios.append(Agenda("BioInformatica",    "IF554AIN", "Docente 5", 105, 3, 5))
    horarios.append(Agenda("BioInformatica",    "IF554AIN", "Docente 5", 105, 3, 5))
    horarios.append(Agenda("M. Discreta",       "IF554AIN", "Docente 6", 106, 3, 6))
    horarios.append(Agenda("M. Discreta",       "IF554AIN", "Docente 6", 106, 3, 6))

    ga = OptimizadorGenetico(tam_poblacion=50, elite=10, max_iteraciones=2000)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, 3)  # Se ejecuta el algoritmo genetico para encontrar un horario optimo.

    horario_visualizado = []
    for r in resultado:
        if r.idClase == "IF554AIN":
            horario_visualizado.append(r)  # Se seleccionan los horarios específicos de la clase 1203.

    vis(horario_visualizado)  # Se visualiza el horario resultante.
