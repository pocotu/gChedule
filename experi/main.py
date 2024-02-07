from prettytable import PrettyTable
from agendas import horarios, Agenda

def imprimir_horario(horarios):
    horario_table = PrettyTable()

    # Lista de días de la semana
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    horario_table.field_names = ['Hora'] + dias_semana

    # Crear una matriz para representar el horario
    matriz_horario = [[''] * len(dias_semana) for _ in range(14)]  # 6 horas por día

    for clase in horarios:
        hora_index = clase.horario - 1  # Ajustar el índice de la hora
        dia_index = clase.diaSemana - 1  # Ajustar el índice del día
        info_clase = f"{clase.idCurso}\nClase: {clase.idClase}\nSalón: {clase.idSalon}\nProfesor: {clase.idDocente}"
        if matriz_horario[hora_index][dia_index]:
            # Si ya hay cursos en esa casilla, añadir el nuevo curso en la misma casilla
            matriz_horario[hora_index][dia_index] += f"\n\n{info_clase}"
        else:
            matriz_horario[hora_index][dia_index] = info_clase

    # Llenar la tabla con la matriz
    for hora_index, hora in enumerate(range(7, 21)):  # Suponiendo un horario de 6 horas
        row_data = [f"{hora}:00 - {hora + 1}:00"]
        row_data.extend(matriz_horario[hora_index])
        horario_table.add_row(row_data)
        # Agregar una línea entre cada hora
        horario_table.add_row(["--------"] * (len(dias_semana) + 1))

    print("Horario:")
    print(horario_table)

if __name__ == "__main__":
    imprimir_horario(horarios)
