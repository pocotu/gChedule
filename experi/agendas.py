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
    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN108', 2, 12),
    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN108', 2, 13),
    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN303', 4, 12),
    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN303', 4, 13),
    Agenda('Algoritmos avanzados', 'A', 'Lauro', 'IN108', 5, 2),

    Agenda('Analisis y diseno de algoritmos', 'A', 'Julio Cesar', 'IN301', 1, 5),
    Agenda('Analisis y diseno de algoritmos', 'A', 'Julio Cesar', 'IN301', 1, 6),
    Agenda('Analisis y diseno de algoritmos', 'A', 'Julio Cesar', 'IN201', 3, 5),
    Agenda('Analisis y diseno de algoritmos', 'A', 'Julio Cesar', 'IN201', 3, 6),

    Agenda('Compiladores', 'A', 'Tany', 'IN103', 2, 10),
    Agenda('Compiladores', 'A', 'Tany', 'IN103', 2, 11),
    Agenda('Compiladores', 'A', 'Tany', 'IN103', 4, 10),
    Agenda('Compiladores', 'A', 'Tany', 'IN103', 4, 11),

    Agenda('Desarrollo de software I', 'C', 'Stephan Joel', 'IN303', 1, 8),
    Agenda('Desarrollo de software I', 'C', 'Stephan Joel', 'IN303', 1, 9),
    Agenda('Desarrollo de software I', 'C', 'Stephan Joel', 'IN303', 3, 8),
    Agenda('Desarrollo de software I', 'C', 'Stephan Joel', 'IN303', 3, 9),

    Agenda('Inteligencia artificial', 'B', 'Maritza', 'IN303', 1, 3),
    Agenda('Inteligencia artificial', 'B', 'Maritza', 'IN303', 1, 4),
    Agenda('Inteligencia artificial', 'B', 'Maritza', 'IN107', 3, 3),
    Agenda('Inteligencia artificial', 'B', 'Maritza', 'IN107', 3, 4),
    Agenda('Inteligencia artificial', 'B', 'Maritza', 'IN107', 5, 4),

    Agenda('Analisis de datos empre...', 'A', 'Lino Prisciliano', 'IN304', 2, 1),
    Agenda('Analisis de datos empre...', 'A', 'Lino Prisciliano', 'IN304', 2, 2),
    Agenda('Analisis de datos empre...', 'A', 'Lino Prisciliano', 'IN206', 4, 1),
    Agenda('Analisis de datos empre...', 'A', 'Lino Prisciliano', 'IN206', 4, 2),

    Agenda('Quechua', 'A', 'Esther Cristina', 'IN201', 2, 8),
    Agenda('Quechua', 'A', 'Esther Cristina', 'IN201', 2, 9),
    Agenda('Quechua', 'A', 'Esther Cristina', 'IN201', 4, 8),
    Agenda('Quechua', 'A', 'Esther Cristina', 'IN201', 4, 9),

    Agenda('Bioinformatica', 'A', 'Julio Cesar', 'IN202', 2, 3),
    Agenda('Bioinformatica', 'A', 'Julio Cesar', 'IN202', 2, 4),
    Agenda('Bioinformatica', 'A', 'Julio Cesar', 'IN306', 4, 3),
    Agenda('Bioinformatica', 'A', 'Julio Cesar', 'IN306', 4, 4),
    Agenda('Bioinformatica', 'A', 'Julio Cesar', 'IN306', 5, 3),

    #############################################################
    Agenda('Analisis de datos empre...', 'B', 'Luis Alvaro', 'IN206', 4, 12),
    Agenda('Analisis de datos empre...', 'B', 'Luis Alvaro', 'IN206', 4, 13),
    Agenda('Analisis de datos empre...', 'B', 'Luis Alvaro', 'IN302', 5, 12),
    Agenda('Analisis de datos empre...', 'B', 'Luis Alvaro', 'IN302', 5, 13),

    Agenda('Organizacion y arquitec...', 'A', 'Edwin', 'IN108', 1, 3),
    Agenda('Organizacion y arquitec...', 'A', 'Edwin', 'IN108', 1, 4),
    Agenda('Organizacion y arquitec...', 'A', 'Edwin', 'IN310', 3, 3),
    Agenda('Organizacion y arquitec...', 'A', 'Edwin', 'IN310', 3, 4),
    Agenda('Organizacion y arquitec...', 'A', 'Edwin', 'IN108', 5, 3),

    Agenda('Organizacion y arquitec...', 'B', 'Manuel Aurelio', 'IN202', 2, 12),
    Agenda('Organizacion y arquitec...', 'B', 'Manuel Aurelio', 'IN202', 2, 13),
    Agenda('Organizacion y arquitec...', 'B', 'Manuel Aurelio', 'IN302', 4, 12),
    Agenda('Organizacion y arquitec...', 'B', 'Manuel Aurelio', 'IN302', 4, 13),
    Agenda('Organizacion y arquitec...', 'B', 'Manuel Aurelio', 'IN202', 5, 11),

    Agenda('Inteligencia artificial', 'A', 'Javier Arturo', 'IN301', 1, 3),
    Agenda('Inteligencia artificial', 'A', 'Javier Arturo', 'IN301', 1, 4),
    Agenda('Inteligencia artificial', 'A', 'Javier Arturo', 'IN202', 3, 3),
    Agenda('Inteligencia artificial', 'A', 'Javier Arturo', 'IN202', 3, 4),
    Agenda('Inteligencia artificial', 'A', 'Javier Arturo', 'IN202', 5, 4),

    Agenda('Desarrollo de software I', 'A', 'Carlos Ramon', 'IN302', 1, 1),
    Agenda('Desarrollo de software I', 'A', 'Carlos Ramon', 'IN302', 1, 2),
    Agenda('Desarrollo de software I', 'A', 'Carlos Ramon', 'IN302', 3, 1),
    Agenda('Desarrollo de software I', 'A', 'Carlos Ramon', 'IN302', 3, 2),

    Agenda('Desarrollo de software I', 'B', 'Boris', 'IN301', 1, 8),
    Agenda('Desarrollo de software I', 'B', 'Boris', 'IN301', 1, 9),
    Agenda('Desarrollo de software I', 'B', 'Boris', 'IN301', 3, 8),
    Agenda('Desarrollo de software I', 'B', 'Boris', 'IN301', 3, 9),

    Agenda('Computacion grafica II', 'A', 'Hans Harley', 'IN202', 2, 10),
    Agenda('Computacion grafica II', 'A', 'Hans Harley', 'IN202', 2, 11),
    Agenda('Computacion grafica II', 'A', 'Hans Harley', 'IN302', 4, 10),
    Agenda('Computacion grafica II', 'A', 'Hans Harley', 'IN302', 4, 11),
    Agenda('Computacion grafica II', 'A', 'Hans Harley', 'IN202', 5, 10),

    Agenda("Modelado y simulacion", 'A', 'Luis Beltran', 'IN301', 1, 1),
    Agenda("Modelado y simulacion", 'A', 'Luis Beltran', 'IN301', 1, 2),
    Agenda("Modelado y simulacion", 'A', 'Luis Beltran', 'IN201', 3, 1),
    Agenda("Modelado y simulacion", 'A', 'Luis Beltran', 'IN201', 3, 2),
    Agenda("Modelado y simulacion", 'A', 'Luis Beltran', 'IN201', 5, 1),
]
# diaSemana: 1-Lunes, 2-Martes, 3-Miércoles, 4-Jueves, 5-Viernes
# horario:  1-(7), 2-(8), 3-(9), 4-(10), 5-(11), 6-(12), 7-(13), 8-(14),
#           9-(15), 10-(16), 11-(17), 12-(18), 13-(19), 14-(20)

#horarios = [
#    Agenda('Algebra Lineal'     , 'A', 'Docente 1', '103', 3, 4),
#    Agenda('Algebra Lineal'     , 'A', 'Docente 1', '103', 3, 4),
#    Agenda('Matematica 1'       , 'A', 'Docente 2', '102', 2, 5),
#    Agenda('Matematica 1'       , 'A', 'Docente 2', '102', 2, 5),
#    Agenda('Sociedad y Cultura' , 'A', 'Docente 3', '201', 1, 1),
#    Agenda('Sociedad y Cultura' , 'A', 'Docente 3', '201', 1, 1),
#    Agenda('Redaccion de textos', 'A', 'Docente 6', '101', 4, 3),
#    Agenda('Redaccion de textos', 'A', 'Docente 6', '101', 4, 3),
#
#    Agenda('Matematica 1'       , 'B', 'Docente 2', '102', 2, 5), 
#    Agenda('Matematica 1'       , 'B', 'Docente 2', '102', 2, 5),
#    Agenda('Filosofia'          , 'B', 'Docente 4', '101', 3, 1),
#    Agenda('Filosofia'          , 'B', 'Docente 4', '101', 3, 1),
#    Agenda('Redaccion de textos', 'B', 'Docente 6', '101', 4, 3),
#    Agenda('Redaccion de textos', 'B', 'Docente 6', '101', 4, 3),
#
#    Agenda('Sociedad y Cultura' , 'C', 'Docente 3', '201', 1, 1),
#    Agenda('Sociedad y Cultura' , 'C', 'Docente 3', '201', 1, 1),
#    Agenda('Filosofia'          , 'C', 'Docente 4', '101', 3, 2),
#    Agenda('Filosofia'          , 'C', 'Docente 4', '101', 3, 2),
#    Agenda('Coro'               , 'C', 'Docente 5', '108', 5, 2),
#    Agenda('Coro'               , 'C', 'Docente 5', '108', 5, 2),
#    Agenda('Redaccion de textos', 'C', 'Docente 6', '101', 4, 3),
#    Agenda('Redaccion de textos', 'C', 'Docente 6', '101', 4, 3)
#]

# Orden de los parametros: Agenda(idCurso, idClase, idDocente, idSalon, diaSemana, horario)
# diaSemana: 1-Lunes, 2-Martes, 3-Miércoles, 4-Jueves, 5-Viernes
# horario:  1-(7), 2-(8), 3-(9), 4-(10), 5-(11), 6-(12), 7-(13), 8-(14),
#           9-(15), 10-(16), 11-(17), 12-(18), 13-(19), 14-(20)