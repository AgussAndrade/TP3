import csv
def f():
	with open("aeropuertos_inventados.csv", encoding = 'utf8') as archivo_aeropuertos:
		r = csv.reader(archivo_aeropuertos, delimiter = ',')
		linea = next ( r, None)
		d = {}
		d[0] = [[linea]]
		print(f'{d[0]}')
		while linea :
			print(f'{linea[0]}')
			linea = next (r, None)

f()
