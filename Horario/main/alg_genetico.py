import copy
import numpy as np

from horario import CostoHorario

class OptimizadorGenetico:
    def __init__(self, tam_poblacion=30, prob_mutacion=0.3, elite=5, max_iteraciones=100):

        self.tam_poblacion = tam_poblacion
        self.prob_mutacion = prob_mutacion
        self.elite = elite
        self.max_iteraciones = max_iteraciones

    def Iniciar_poblacion(self, horarios):
        self.poblacion = []

        for i in range(self.tam_poblacion):
            entidad = []

            # Genera horarios aleatorios y los agrega a la entidad
            for s in horarios:
                entidad.append(copy.deepcopy(s))

            self.poblacion.append(entidad)

    def Mutar(self, poblacionElite, salonRango):

        e = np.random.randint(0, self.elite, 1)[0]  # Elige un horario elite al azar
        pos = np.random.randint(0, 2, 1)[0]  # Decide qué aspecto del horario se va a mutar (0, 1 o 2)

        ep = copy.deepcopy(poblacionElite[e])  # Copia el horario elite seleccionado.

        for p in ep:
            pos = np.random.randint(0, 3, 1)[0]  # Decide qué característica específica del horario se va a mutar
            operation = np.random.rand()  # Genera un número aleatorio para decidir si se suma o resta

            if pos == 0:
                p.idSalon = self.AgregarResta(p.idSalon, operation, salonRango)  # Mutación en el ID del salón
            if pos == 1:
                p.diaSemana = self.AgregarResta(p.diaSemana, operation, 5)  # Mutación en el día de la semana
            if pos == 2:
                p.horario = self.AgregarResta(p.horario, operation, 5)  # Mutación en el horario

        print('## Mutacion en el horario: {} ##'.format(e + 1))  # Imprime el número de horario mutado
        return ep

    def AgregarResta(self, valor, op, valorRango):

        if op > 0.5:
            if valor < valorRango:
                valor += 1
            else:
                valor -= 1
        else:
            if valor - 1 > 0:
                valor -= 1
            else:
                valor += 1

        return valor

    def Cruzar(self, poblacionElite):

        e1 = np.random.randint(0, self.elite, 1)[0]  # Elige un primer horario elite al azar
        e2 = np.random.randint(0, self.elite, 1)[0]  # Elige un segundo horario elite al azar

        pos = np.random.randint(0, 2, 1)[0]  # Decide qué aspecto del horario se va a cruzar (0 o 1)

        ep1 = copy.deepcopy(poblacionElite[e1])  # Copia el primer horario elite seleccionado
        ep2 = poblacionElite[e2]  # Toma el segundo horario elite.

        for p1, p2 in zip(ep1, ep2):
            if pos == 0:
                p1.diaSemana = p2.diaSemana  # Cruce en el día de la semana
                p1.horario = p2.horario  # Cruce en el horario
            if pos == 1:
                p1.idSalon = p2.idSalon  # Cruce en el id del salón

        print('Cruce entre los horarios: {} y {}'.format(e1 + 1, e2 + 1))  # Imprime los números de horarios cruzados
        return ep1   

    def Evolucion(self, horarios, salonRango):
        mejorPunto = 0
        mejorHorario = None
    
        self.Iniciar_poblacion(horarios, salonRango)  # Inicializa la poblacion aleatoriamente
    
        conflictos_anteriores = float('inf')  # Inicializa el número de conflictos anteriores con un valor grande
        repeticiones = 0  # Inicializa el contador de repeticiones
    
        for i in range(self.max_iteraciones):
            indiceElite, mejorPunto = CostoHorario(self.poblacion, self.elite)  # Evalua y selecciona a la elite

            print('---------------------------------------------------------------')
            print('Iteracion: {} | conflicto: {} | Tamaño de la población elite: {}'.format(i + 1, mejorPunto, len(indiceElite)))
            print('---------------------------------------------------------------')

            if mejorPunto == 0:
                mejorHorario = self.poblacion[indiceElite[0]]
                print('#### Se encontro un horario sin conflictos ####')
                break
            
            nuevaPoblacion = [self.poblacion[indice] for indice in indiceElite]
    
            while len(nuevaPoblacion) < self.tam_poblacion:
                if np.random.rand() < self.prob_mutacion:
                    nuevaP = self.Mutar(nuevaPoblacion, salonRango)  # Aplica mutacion con cierta probabilidad
                else:
                    nuevaP = self.Cruzar(nuevaPoblacion)  # Realiza cruce entre horarios elite
    
                nuevaPoblacion.append(nuevaP)
    
            self.poblacion = nuevaPoblacion  # Actualiza la poblacion
    
            # Verifica si el número de conflictos no cambia
            if mejorPunto == conflictos_anteriores:
                repeticiones += 1
            else:
                repeticiones = 0
    
            # Detén el código si el mismo conflicto se repite más de 1000 veces
            if repeticiones >= 1000:
                print('Se detiene debido a repeticiones de conflicto.')
                break
            
            conflictos_anteriores = mejorPunto  # Actualiza el número de conflictos anteriores
    
        return mejorHorario


