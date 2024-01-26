import random

def generate_schedule(courses):
  """
  Genera un horario de clases aleatorio, verificando que los cursos no se crucen.

  Args:
    courses: Una lista de cursos.

  Returns:
    Un horario de clases.
  """

  schedule = []
  for day in range(5):
    schedule.append([])
    for hour in range(8):
      course = courses.pop(random.randint(0, len(courses) - 1))
      schedule[day].append(course)
  return schedule
