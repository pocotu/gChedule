import numpy as np

# Clase de horario de clases
class Schedule:
    def __init__(self, courseId, classId, teacherId):
        """Init
        Argumentos:
            courseId: int, id unico del curso.
            classId: int, id unico de la clase.
            teacherId: int, id unico del profesor.
        """
        self.courseId = courseId
        self.classId = classId
        self.teacherId = teacherId

        self.roomId = 0
        self.weekDay = 0
        self.slot = 0

    def random_init(self, roomRange):
        """Ramdom init
        Argumentos:
            roomSize: int, numero de salones.
        """
        self.roomId = np.random.randint(1, roomRange + 1, 1)[0]
        self.weekDay = np.random.randint(1, 6, 1)[0]
        self.slot = np.random.randint(1, 6, 1)[0]


def schedule_cost(population, elite):
    """Calcula el conflicto de los horarios de clase.
    Argumentos:
        población: Lista, poblacion de horarios de clase.
        elite: int, numero de mejor resultado.
    """
    conflicts = []
    n = len(population[0])

    for p in population:
        conflict = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # check course in same time and same room
                if p[i].roomId == p[j].roomId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check course for one class in same time
                if p[i].classId == p[j].classId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check course for one teacher in same time
                if p[i].teacherId == p[j].teacherId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check same course for one class in same day
                if p[i].classId == p[j].classId and p[i].courseId == p[j].courseId and p[i].weekDay == p[j].weekDay:
                    conflict += 1

        conflicts.append(conflict)

    index = np.array(conflicts).argsort()

    return index[: elite], conflicts[index[0]]
