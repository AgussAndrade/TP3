import csv
import sys
import random
from grafo import *
from pilacola import *
from funciones_grafo import *
from funciones_tp import *
PARAMETROS_COMANDOS = sys.stdin
PARAMETROS = sys.argv[1:]
print(f'{PARAMETROS}')
LARGO_PARAMETROS = len(PARAMETROS)
OPERACIONES = {'listar_operaciones': -1,'camino_mas' : 0,'camino_escalas' : 1,'centralidad' : 2,'centralidad_aprox' : 3,'pagerank' : 4,'nueva_aerolinea' : 5,'recorrer_mundo' : 6,'recorrer_mundo_aprox' : 7,'vacaciones' : 8, 'itinerario' : 9, 'exportar_kml' : 10}
ER_CARPETA = 'ER_CARPETA'
ERROR_CENTRALIDAD_APROX = 'ERROR_CENTRALIDAD_APROX'
ERROR_VACACIONES = 'ERROR_VACACIONES'
ERROR_PARAMETROS = 'ERROR_PARAMETROS'
ERROR_CENTRALIDAD = 'ERROR_CENTRALIDAD'
ERROR_CAMINO_MAS = 'ERROR_CAMINO_MAS'
ERROR_NUEVA_AEROLINEA = 'ERROR_NUEVA_AEROLINEA'
ERROR_RECORRER_MUNDO = 'ERROR_RECORRER_MUNDO'
ERROR_RECORRER_MUNDO_APROX = 'ERROR_RECORRER_MUNDO_APROX'
ERROR_PAGERANK = 'ERROR_PAGERANK'
NO_PERTENECE_OPERACIONES = 'NO_PERTENECE_OPERACIONES'
def revisar_parametros():
	if(LARGO_PARAMETROS != 2):
		print(ERROR_PARAMETROS)
		return False
	if (PARAMETROS[0].find(".csv") != -1 or PARAMETROS[1].find(".csv") != -1):
		return True
	return False

def guardar_aeropuertos():
	try:

		with open(PARAMETROS[0], encoding = 'utf8') as archivo_aeropuertos:
			r = csv.reader(archivo_aeropuertos, delimiter = ',')
			aeropuertos = {}
			linea = next ( r, None)
			while linea :
				if(linea[0] in aeropuertos): aeropuertos[linea[0]].append([linea])
				else: aeropuertos[linea[0]] = [linea]
				linea = next (r, None)
			return aeropuertos
	except FileNotFoundError:
		print( ER_CARPETA)
	return None 

def guardar_vuelos():
	try:
		with open(PARAMETROS[1],encoding = 'utf8') as archivo_vuelos:
			r = csv.reader(archivo_vuelos,delimiter = ',')
			vuelos = Grafo()
			linea = next(r,None)
			while linea:
				print(linea[2:])
				vuelos.agregar_arista(linea[0],linea[1],linea[2:])
				vuelos.agregar_arista(linea[1],linea[0],linea[2:])
				linea = next(r,None)
			return vuelos
	except FileNotFoundError:
		print(ER_CARPETA)
	return None
def envolver_comandos(aeropuertos,vuelos):
	linea = input()
	while linea:
		comando = linea.rstrip('\n').split(' ')

		if(not comando[0] in OPERACIONES): 
			print(NO_PERTENECE_OPERACIONES)
			linea = input()

			continue

		valor = OPERACIONES[comando[0]]

		if valor == -1:
			for key in OPERACIONES.keys():
				print(f'{key}')
			linea = input()
			continue

		comandos_validos = (' '.join(comando[1:])).split(',') # es un asco hacer esto pero es lo mas valido que se me ocurre
		largo = len(comandos_validos)

		if valor == 0:
			if (comandos_validos[0] == "rapido" and largo >2):
				camino_mas(0,aeropuertos,vuelos,comandos_validos[1],comandos_validos[2])
			elif(comandos_validos[0] == "barato" and largo >2):
				camino_mas(1,aeropuertos,vuelos,comandos_validos[1],comandos_validos[2])
			else:
				print(ERROR_CAMINO_MAS)
		elif valor == 1:
			if(largo == 2):
				camino_escalas(aeropuertos,vuelos,comandos_validos[0],comandos_validos[1])
			else:
				print(ERROR_CAMINO_ESCALAS)
		elif valor == 2:
			if(largo == 1 and comandos_validos[0].isdigit()):
				centralidad(vuelos,int(comandos_validos[0]))
			else:
				print(ERROR_CENTRALIDAD)
		elif valor == 3:
			if(largo == 1 and comandos_validos[0].isdigit()):
				centralidad_aprox(vuelos,int(comandos_validos[0]))
			else:
				print(ERROR_CENTRALIDAD_APROX)
		# if valor == 4:
		# 	if(largo == 1 and comandos_validos[0].isdigit()):
		# 		pagerank(aeropuertos,vuelos,int(comandos_validos[0]))
		# 	else:
		# 		print(ERROR_PAGERANK)
		# 	continue
		# if valor == 5:
		# 	if(largo == 1 and find(".csv",comandos_validos[0]) != -1):
		# 		nueva_aerolinea(aeropuestos,vuelos,comandos_validos[0])
		# 	else:
		# 		print(ERROR_NUEVA_AEROLINEA)
		# 	continue
		# if valor == 6:
		# 	if(largo == 1):
		# 		recorrer_mundo(aeropuertos,vuelos,comandos_validos[0])
		# 	else:
		# 		print(ERROR_RECORRER_MUNDO)
		# 	continue

		# if valor == 7:
		# 	if(largo == 1):
		# 		recorrer_mundo_aprox(aeropuertos,vuelos,comandos_validos[0])
		# 	else:
		# 		print(ERROR_RECORRER_MUNDO_APROX)
		# 	continue

		# if valor == 8:
		# 	if(largo == 2 and comandos_validos[1].isdigit()):
		# 		vacaciones(aeropuertos,vuelos,comandos_validos[0],int(comandos_validos[1]))
		# 	else:
		# 		print(ERROR_VACACIONES)
		# 	continue

		# # if valor == 9:

		# # if valor == 10:
		linea = input()

def main():
	if revisar_parametros():
		aeropuertos = guardar_aeropuertos()
		vuelos = guardar_vuelos()
		envolver_comandos(aeropuertos,vuelos)

main()