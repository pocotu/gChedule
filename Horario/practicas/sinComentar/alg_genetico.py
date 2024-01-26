import copy
import numpy as np

from Horario import CostoHorario

class OptimizadorGenetico:
    def __init__(self, tam_poblacion=30, prob_mutacion=0.3, elite=5, max_iteraciones=100):
        self.tam_poblacion = tam_poblacion
        self.prob_mutacion = prob_mutacion
        self.elite = elite
        self.max_iteraciones = max_iteraciones

    def Iniciar_poblacion(self, horarios, salonRango):
        self.poblacion = []

        for i in range(self.tam_poblacion):
            entidad = []

            for s in horarios:
                s.Inicializador_aleatorio(salonRango)
                entidad.append(copy.deepcopy(s))

            self.poblacion.append(entidad)

    def Mutar(self, poblacionElite, salonRango):
        e = np.random.randint(0, self.elite, 1)[0]
        pos = np.random.randint(0, 2, 1)[0]

        ep = copy.deepcopy(poblacionElite[e])
    
        for p in ep:
            pos = np.random.randint(0, 3, 1)[0]
            operation = np.random.rand()

            if pos == 0:
                p.idSalon = self.AgregarResta(p.idSalon, operation, salonRango)
            if pos == 1:
                p.diaSemana = self.AgregarResta(p.diaSemana, operation, 5)
            if pos == 2:
                p.horario = self.AgregarResta(p.horario, operation, 5)

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
        e1 = np.random.randint(0, self.elite, 1)[0]
        e2 = np.random.randint(0, self.elite, 1)[0]

        pos = np.random.randint(0, 2, 1)[0]

        ep1 = copy.deepcopy(poblacionElite[e1])
        ep2 = poblacionElite[e2]

        for p1, p2 in zip(ep1, ep2):
            if pos == 0:
                p1.diaSemana = p2.diaSemana
                p1.horario = p2.horario
            if pos == 1:
                p1.idSalon = p2.idSalon

        return ep1

    def Evolucion(self, horarios, salonRango):
        mejorPunto = 0
        mejorHorario = None

        self.Iniciar_poblacion(horarios, salonRango)

        for i in range(self.max_iteraciones):
            indiceElite, mejorPunto = CostoHorario(self.poblacion, self.elite)

            print('Iteracion: {} | conflicto: {}'.format(i + 1, mejorPunto))

            if mejorPunto == 0:
                mejorHorario = self.poblacion[indiceElite[0]]
                break

            nuevaPoblacion = [self.poblacion[indice] for indice in indiceElite]

            while len(nuevaPoblacion) < self.tam_poblacion:
                if np.random.rand() < self.prob_mutacion:
                    nuevaP = self.Mutar(nuevaPoblacion, salonRango)
                else:
                    nuevaP = self.Cruzar(nuevaPoblacion)

                nuevaPoblacion.append(nuevaP)

            self.poblacion = nuevaPoblacion

        return mejorHorario
