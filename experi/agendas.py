class Agenda:
    def __init__(self, idCurso, idClase, idDocente, idSalon, diaSemana, horario):
        self.idCurso = idCurso
        self.idClase = idClase
        self.idDocente = idDocente
        self.idSalon = idSalon
        self.diaSemana = diaSemana
        self.horario = horario

# Orden de los parametros: Agenda(idCurso, idClase, idDocente, idSalon, diaSemana, horario)
# diaSemana: 1-Lunes, 2-Martes, 3-Miércoles, 4-Jueves, 5-Viernes
# horario: 1-7:00-8:00, 2-8:00-9:00, 3-9:00-10:00, 4-10:00-11:00, 5-11:00-12:00, 6-12:00-13:00
# Lista de horarios: 1201 - 1202 - 1203

        
horarios = [
    Agenda('Algebra Lineal'     , 'A', 'Docente 1', '103', 3, 4),
    Agenda('Algebra Lineal'     , 'A', 'Docente 1', '103', 3, 4),
    Agenda('Matematica 1'       , 'A', 'Docente 2', '102', 2, 5),
    Agenda('Matematica 1'       , 'A', 'Docente 2', '102', 2, 5),
    Agenda('Sociedad y Cultura' , 'A', 'Docente 3', '201', 1, 1),
    Agenda('Sociedad y Cultura' , 'A', 'Docente 3', '201', 1, 1),
    Agenda('Redaccion de textos', 'A', 'Docente 6', '101', 4, 3),
    Agenda('Redaccion de textos', 'A', 'Docente 6', '101', 4, 3),

    Agenda('Matematica 1'       , 'B', 'Docente 2', '102', 2, 5), 
    Agenda('Matematica 1'       , 'B', 'Docente 2', '102', 2, 5),
    Agenda('Filosofia'          , 'B', 'Docente 4', '101', 3, 1),
    Agenda('Filosofia'          , 'B', 'Docente 4', '101', 3, 1),
    Agenda('Redaccion de textos', 'B', 'Docente 6', '101', 4, 3),
    Agenda('Redaccion de textos', 'B', 'Docente 6', '101', 4, 3),

    Agenda('Sociedad y Cultura' , 'C', 'Docente 3', '201', 1, 1),
    Agenda('Sociedad y Cultura' , 'C', 'Docente 3', '201', 1, 1),
    Agenda('Filosofia'          , 'C', 'Docente 4', '101', 3, 2),
    Agenda('Filosofia'          , 'C', 'Docente 4', '101', 3, 2),
    Agenda('Coro'               , 'C', 'Docente 5', '108', 5, 2),
    Agenda('Coro'               , 'C', 'Docente 5', '108', 5, 2),
    Agenda('Redaccion de textos', 'C', 'Docente 6', '101', 4, 3),
    Agenda('Redaccion de textos', 'C', 'Docente 6', '101', 4, 3)
]

# Orden de los parametros: Agenda(idCurso, idClase, idDocente, idSalon, diaSemana, horario)
# diaSemana: 1-Lunes, 2-Martes, 3-Miércoles, 4-Jueves, 5-Viernes
# horario:  1-(7), 2-(8), 3-(9), 4-(10), 5-(11), 6-(12), 7-(13), 8-(14),
#           9-(15), 10-(16), 11-(17), 12-(18), 13-(19), 14-(20), 15-(21)

#horarios = [
#    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN108', )
#]