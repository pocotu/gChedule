from prettytable import PrettyTable
from agendas import horarios, Agenda

def imprimir_horario_sin_conflictos(horarios):
    horario_table = PrettyTable()

    # Lista de días de la semana
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    horario_table.field_names = ['Hora'] + dias_semana

    horarios_sin_conflictos, horarios_reubicados = eliminar_y_reubicar_conflictos(horarios)

    # Crear una matriz para representar el horario
    matriz_horario = [[''] * len(dias_semana) for _ in range(6)]  # 6 horas por día

    for clase in horarios_sin_conflictos:
        hora_index = clase.horario - 1  # Ajustar el índice de la hora
        dia_index = clase.diaSemana - 1  # Ajustar el índice del día
        info_clase = f"{clase.idCurso}\nClase: {clase.idClase}\nSalón: {clase.idSalon}\nProfesor: {clase.idDocente}"
        matriz_horario[hora_index][dia_index] = info_clase

    # Llenar la tabla con la matriz
    for hora_index, hora in enumerate(range(1, 7)):  # Suponiendo un horario de 6 horas
        row_data = [f"{hora}:00 - {hora + 1}:00"]
        row_data.extend(matriz_horario[hora_index])
        horario_table.add_row(row_data)
        # Agregar una línea entre cada hora
        horario_table.add_row(["---"] * (len(dias_semana) + 1))

    print("Horario sin conflictos:")
    print(horario_table)

    if horarios_reubicados:
        imprimir_horario_reubicado(horarios_reubicados)

def eliminar_y_reubicar_conflictos(horarios):
    horarios_sin_conflictos = []
    horarios_reubicados = []
    horarios_ordenados = sorted(horarios, key=lambda x: (x.diaSemana, x.horario))

    for i in range(len(horarios_ordenados) - 1):
        current_clase = horarios_ordenados[i]
        next_clase = horarios_ordenados[i + 1]

        if current_clase.diaSemana == next_clase.diaSemana and current_clase.horario == next_clase.horario:
            # Hay conflicto, reubicar el curso en otro horario
            new_horario = (next_clase.horario + 1) if next_clase.horario < 6 else 1
            horarios_reubicados.append(Agenda(
                next_clase.idCurso,
                next_clase.idClase,
                next_clase.idDocente,
                next_clase.idSalon,
                next_clase.diaSemana,
                new_horario
            ))
        else:
            horarios_sin_conflictos.append(current_clase)

    # Añadir la última clase
    horarios_sin_conflictos.append(horarios_ordenados[-1])

    return horarios_sin_conflictos, horarios_reubicados

def imprimir_horario_reubicado(horarios_reubicados):
    horario_table = PrettyTable()

    # Lista de días de la semana
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    horario_table.field_names = ['Hora'] + dias_semana

    # Crear una matriz para representar el nuevo horario reubicado
    matriz_horario = [[''] * len(dias_semana) for _ in range(6)]  # 6 horas por día

    for clase in horarios_reubicados:
        hora_index = clase.horario - 1  # Ajustar el índice de la hora
        dia_index = clase.diaSemana - 1  # Ajustar el índice del día
        info_clase = f"{clase.idCurso}\nClase: {clase.idClase}\nSalón: {clase.idSalon}\nProfesor: {clase.idDocente}"
        matriz_horario[hora_index][dia_index] = info_clase

    # Llenar la tabla con la matriz
    for hora_index, hora in enumerate(range(1, 7)):  # Suponiendo un horario de 6 horas
        row_data = [f"{hora}:00 - {hora + 1}:00"]
        row_data.extend(matriz_horario[hora_index])
        horario_table.add_row(row_data)
        # Agregar una línea entre cada hora
        horario_table.add_row(["---"] * (len(dias_semana) + 1))

    print("\nHorario con cursos reubicados:")
    print(horario_table)

if __name__ == "__main__":
    imprimir_horario_sin_conflictos(horarios)
