import copy
import numpy as np

from horario import CostoHorario

class OptimizadorGenetico:
    def __init__(self, tam_poblacion=30, prob_mutacion=0.3, elite=5, max_iteraciones=100):
        """
        Inicializa un objeto OptimizadorGenetico con los parámetros especificados.

        Args:
            tam_poblacion (int): Tamaño de la población de horarios candidatos.
            prob_mutacion (float): Probabilidad de aplicar mutación a un horario.
            elite (int): Número de horarios elite que se mantendrán sin cambios en cada generación.
            max_iteraciones (int): Número máximo de iteraciones del algoritmo genético.
        """
        self.tam_poblacion = tam_poblacion
        self.prob_mutacion = prob_mutacion
        self.elite = elite
        self.max_iteraciones = max_iteraciones

    def Iniciar_poblacion(self, horarios, salonRango):
        """
        Inicializa la población de horarios de forma aleatoria.

        Args:
            horarios (list): Lista de horarios disponibles.
            salonRango (int): Rango de valores para el ID del salón.

        Returns:
            None
        """
        self.poblacion = []

        for i in range(self.tam_poblacion):
            entidad = []

            # Genera horarios aleatorios y los agrega a la entidad
            for s in horarios:        
                s.Inicializador_aleatorio(salonRango)
                entidad.append(copy.deepcopy(s))

            self.poblacion.append(entidad)

    def Mutar(self, poblacionElite, salonRango):
        # Aplica una mutacion en uno de los horarios de la población elite

        e = np.random.randint(0, self.elite, 1)[0]  # Elige un horario elite al azar
        pos = np.random.randint(0, 2, 1)[0]  # Decide que aspecto del horario se va a mutar (0, 1 o 2)

        ep = copy.deepcopy(poblacionElite[e])  # Copia el horario elite seleccionado.

        for p in ep:
            pos = np.random.randint(0, 3, 1)[0]  # Decide que caracteristica especifica del horario se va a mutar
            operation = np.random.rand()  # Genera un numero aleatorio para decidir si se suma o resta

            if pos == 0:
                p.idSalon = self.AgregarResta(p.idSalon, operation, salonRango)  # Mutacion en el id del salon
            if pos == 1:
                p.diaSemana = self.AgregarResta(p.diaSemana, operation, 5)  # Mutacion en el dia de la semana
            if pos == 2:
                p.horario = self.AgregarResta(p.horario, operation, 5)  # Mutacion en el horario

        return ep

    def AgregarResta(self, valor, op, valorRango):
        # Realiza una operacion de suma o resta en funcion de la probabilidad op

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
        # Realiza un cruce (intercambio) entre dos horarios de la población olite

        e1 = np.random.randint(0, self.elite, 1)[0]  # Elige un primer horario elite al azar
        e2 = np.random.randint(0, self.elite, 1)[0]  # Elige un segundo horario elite al azar

        pos = np.random.randint(0, 2, 1)[0]  # Decide que aspecto del horario se va a cruzar (0 o 1)

        ep1 = copy.deepcopy(poblacionElite[e1])  # Copia el primer horario elite seleccionado
        ep2 = poblacionElite[e2]  # Toma el segundo horario elite.

        for p1, p2 in zip(ep1, ep2):
            if pos == 0:
                p1.diaSemana = p2.diaSemana  # Cruce en el dia de la semana
                p1.horario = p2.horario  # Cruce en el horario
            if pos == 1:
                p1.idSalon = p2.idSalon  # Cruce en el id del salon

        return ep1

    def Evolucion(self, horarios, salonRango):
        # Realiza la evolucion de la poblacion a lo largo de varias iteraciones

        mejorPunto = 0
        mejorHorario = None

        self.Iniciar_poblacion(horarios, salonRango)  # Inicializa la poblacion aleatoriamente

        for i in range(self.max_iteraciones):
            indiceElite, mejorPunto = CostoHorario(self.poblacion, self.elite)  # Evalua y selecciona a la elite

            print('Iteracion: {} | conflicto: {}'.format(i + 1, mejorPunto))

            if mejorPunto == 0:
                mejorHorario = self.poblacion[indiceElite[0]]
                break

            nuevaPoblacion = [self.poblacion[indice] for indice in indiceElite]

            while len(nuevaPoblacion) < self.tam_poblacion:
                if np.random.rand() < self.prob_mutacion:
                    nuevaP = self.Mutar(nuevaPoblacion, salonRango)  # Aplica mutacion con cierta probabilidad
                else:
                    nuevaP = self.Cruzar(nuevaPoblacion)  # Realiza cruce entre horarios elite

                nuevaPoblacion.append(nuevaP)

            self.poblacion = nuevaPoblacion  # Actualiza la poblacion

        return mejorHorario
