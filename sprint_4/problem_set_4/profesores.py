#Dictionaries of Dictionaries (of Dictionaries)

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# Define a procedure, involved(courses, person), that takes as
#input a courses structure and a person and returns a Dictionary that describes
#all the courses the person is involved in.  A person is involved in a course if
#they are a value for any property for the course.  The output Dictionary should
#have hexamesters as its keys, and each value should be a list of courses that
#are offered that hexamester (the courses in the list can be in any order).

def involved(courses, person):
    # Tenemos que devovler un dict con el hexamester como clave y cursos valor
    res = {}
    for hexamester in courses:
        for course in courses[hexamester]:
            # Si la persona está en la lista de valores de cursos
            if person in list(courses[hexamester][course].values()):
                # si no existe hexamester como clave en el dict lo creamos y asignamos una lista vacia
                if hexamester not in res.keys():
                    res[hexamester] = []
                # agregamos el curso a la lista de nuestro dict si cumple las condiciones
                res[hexamester].append(course)
    return res

print(involved(courses, 'Dave')) # => {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}
# print involved(courses, 'Peter C.') => {'apr2012': ['cs262'], 'feb2012': ['cs101']}
# print involved(courses, 'Dorina') => {'jan2044': ['cs001']}
