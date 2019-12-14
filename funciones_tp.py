import csv
import sys
import random
from grafo import *
from pilacola import *
from funciones_grafo import *
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
ERROR_CAMINO_ESCALAS = 'ERROR_CAMINO_ESCALAS'

NO_PERTENECE_OPERACIONES = 'NO_PERTENECE_OPERACIONES'
def camino_mas(formato,aeropuertos,vuelos,desde,hasta):
	if not desde in aeropuertos or not hasta in aeropuertos:
		print(ERROR_CAMINO_MAS)
		return
	codigos_validos = []
	padres = {}
	dist = {}
	menor = float('inf')
	a_utilizar = ''
	for datos_hasta in aeropuertos[hasta]:
		codigos_validos.append(datos_hasta[1])
	for listas in aeropuertos[desde]:
		padres_aux,dist_aux = camino_minimo(vuelos,listas[1],formato)
		for aeropuerto_hasta in codigos_validos:
			if dist_aux[aeropuerto_hasta] < menor:
				menor = dist_aux[aeropuerto_hasta]
				dist = dist_aux
				padres = padres_aux
				a_utilizar = aeropuerto_hasta
	
	pila = Pila()
	while a_utilizar != None:
		pila.apilar(a_utilizar)
		a_utilizar = padres[a_utilizar]
	while not pila.esta_vacia():
		print(pila.desapilar(), end = '')
		if not pila.esta_vacia():
			print(' -> ', end = '')
	print()
	return

def camino_escalas(aeropuertos,vuelos,desde,hasta):
	if not desde in aeropuertos or not hasta in aeropuertos:
		print(ERROR_CAMINO_ESCALAS)
		return
	codigos_validos = []
	padres = {}
	orden = {}
	menor = float('inf')
	a_utilizar = ''
	for datos_hasta in aeropuertos[hasta]:
		codigos_validos.append(datos_hasta[1])
	for listas in aeropuertos[desde]:
		padres_aux,orden_aux = bfs(vuelos,listas[1])
		for aeropuerto_hasta in codigos_validos:
			if orden_aux[aeropuerto_hasta] < menor:
				menor = orden_aux[aeropuerto_hasta]
				orden = orden_aux
				padres = padres_aux
				a_utilizar = aeropuerto_hasta

	pila = Pila()
	while a_utilizar != None:
		pila.apilar(a_utilizar)
		a_utilizar = padres[a_utilizar]
	while not pila.esta_vacia():
		print(pila.desapilar(), end = '')
		if not pila.esta_vacia():
			print(' -> ', end = '')
	print()
	return

def centralidad(vuelos,formato):
	cent = grafo_centralidad(vuelos,2)
	minimos = Heap()
	contador = 0
	for codigo,tam in cent.items():
		if(contador < formato):
			minimos.encolar((tam,codigo))
			contador +=1
			continue
		if tam > minimos.ver_min()[0]:
			minimos.desencolar()
			minimos.encolar((tam,codigo))
	pila = Pila()
	while not minimos.esta_vacio():
		pila.apilar(minimos.desencolar()[1])
	while not pila.esta_vacia():
		print(pila.desapilar(), end = '')
		if not pila.esta_vacia():
			print(',', end = '')
	print()
	return
def centralidad_aprox(vuelos,formato):
	cent = vuelos.cent_aprox(2)
	minimos = Heap()
	cantidad = 0
	for codigo,tam in cent.items():
		if(cantidad < formato):
			minimos.encolar((tam,codigo))
			cantidad +=1
			continue
		if tam > minimos.ver_min()[0]:
			minimos.desencolar()
			minimos.encolar((tam,codigo))
	pila = Pila()
	while not minimos.esta_vacio():
		pila.apilar(minimos.desencolar()[1])
	while not pila.esta_vacia():
		print(pila.desapilar(), end = '')
		if not pila.esta_vacia():
			print(',', end = '')
	print()
	return
					# pagerank(aeropuertos,vuelos,ord(comandos_validos[0]))
					# nueva_aerolinea(aeropuestos,vuelos,comandos_validos[0])
def _vacaciones(vuelos,desde,actual,rta,visitados,cant_visitados,cantidad):
	if cant_visitados == cantidad:
		if vuelos.estan_unidos(desde,actual): return True
		else: return False
	ady = vuelos.adyacentes(actual)

	for v in ady:
		if v not in visitados:
			rta.append(v)
			visitados.add(v)
			cant_visitados+=1
			if(_vacaciones(vuelos,desde,v,rta,visitados,cant_visitados,cantidad)):
				return True
			rta.pop()
			visitados.remove(v)
			cant_visitados-=1
	return False
def vacaciones(aeropuertos,vuelos,desde,cantidad):
	if not desde in aeropuertos:
		print(ERROR_VACACIONES)
	rta = []
	visitados = set()
	cant_visitados = 0
	for codigos in aeropuertos[desde]:

		codigo = codigos[1]
		rta.append(codigo)
		visitados.add(codigo)
		cant_visitados+=1
		if (_vacaciones(vuelos,codigo,codigo,rta,visitados,cant_visitados,cantidad)):
			largo_rta = len(rta)
			for i in range(largo_rta):
				print(f'{rta[i]} -> ',end = '')
			print(rta[0])
			return
		else:
			rta.pop()
			visitados.remove(codigo)
			cant_visitados-=1
	print(ERROR_RECORRER_MUNDO)
	return
					# recorrer_mundo_aprox(aeropuertos,vuelos,comandos_validos[0])
					# vacaciones(aeropuertos,vuelos,comandos_validos[0],ord(comandos_validos[1]))
