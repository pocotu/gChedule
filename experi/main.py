from prettytable import PrettyTable
from agendas import Agenda, horarios

def imprimir_horario(horarios):
    horario_tabla = PrettyTable()

    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario_tabla.field_names = ['Hora'] + dias_semana

    matriz_horario = [[''] * len(dias_semana) for _ in range(14)]

    #recorre la lista de clases horarios y organiza la información de cada clase en una matriz matriz_horario 
    #según su horario y día de la semana. Si hay varias clases en el mismo horario y día
    for clase in horarios:
        indice_hora = clase.horario - 1
        indice_dia = clase.diaSemana - 1

        info_clase = f"{clase.idCurso}\nClase: {clase.idClase}\nSalon: {clase.idSalon}\nProfesor: {clase.idDocente}"

        if matriz_horario[indice_hora][indice_dia]:
            # si hay algun curso en esa casilla, agregar el nuevo curso en la misma casilla
            matriz_horario[indice_hora][indice_dia] += f"\n\n{info_clase}"

        else:
            matriz_horario[indice_hora][indice_dia] = info_clase

    # llenar la tabla con la matriz
    for indice_hora, hora in enumerate(range(7, 21)):
        fila_hora = [f"{hora}:00 - {hora + 1}:00"]
        fila_hora.extend(matriz_horario[indice_hora])
        horario_tabla.add_row(fila_hora)

        horario_tabla.add_row(["--------"] * (len(dias_semana) + 1))

    print("Horario")
    print(horario_tabla)

if __name__== "__main__":
    imprimir_horario(horarios)
