# For-Each Schleife
obstarten = ['Apfel', 'Birne', 'Traube', 'Raspberry', 'Dingleberry']

# Iterieren über die Liste obstarten
for obst in obstarten:
    print(obst)
print ('\n')
    # Wie kann ich den Index ermitteln
for i in range(len(obstarten)):
    print(i, obstarten[i])
print ('\n')

    # for_each
for index, value in enumerate(obstarten):
    if value == 'Dingleberry':
        obstarten[index] = 'Klabusterbeere heißt das'

print (obstarten)