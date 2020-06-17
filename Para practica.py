import csv

with open('listado_aportantes.csv') as csvfile:
    datos = list(csv.DictReader(csvfile))

row = datos[0]
print('Fila 0', row)
dni = datos[3].get('DNI')
print(dni)