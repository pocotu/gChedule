import csv

def get_courses():
  """
  Devuelve una lista de cursos, eliminando los duplicados.

  Args:
    None

  Returns:
    Una lista de cursos.
  """

  with open('DR.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    courses = []
    for row in reader:
      courses.append(row[0])
  return list(set(courses))
