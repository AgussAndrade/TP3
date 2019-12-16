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
		print(f'codigo: {codigo} -- tam: {tam}')
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
def pagerank(grafo,cantidad,iteraciones):
	pagerank = {}
	links = {}
	cant_vertices = 0
	contador = 0
	rank = Heap()
	vertices = grafo.obtener_vertices()
	for v in vertices:
		cant_vertices += 1
		pagerank[v] = 0
		links[v] = 0
		for w in grafo.adyacentes(v):
			links[v] += 1
	for i in range(iteraciones):
		for vert in vertices:
			pagerank_suma = 0
			for w in grafo.adyacentes(vert):
				pagerank_suma += (pagerank[w]/links[w])
			pagerank[vert] += (((1-0.85)/cant_vertices) + (0.85 * pagerank_suma))
	for k,v in pagerank.items():
		if(contador < cantidad):
			rank.encolar((v,k))
			contador +=1
			continue
		if v > rank.ver_min()[0]:
			rank.desencolar()
			rank.encolar((v,k))
	pila = Pila()
	while not rank.esta_vacio():
		pila.apilar(rank.desencolar()[1])
	while not pila.esta_vacia():
		print(pila.desapilar(), end = '')
		if not pila.esta_vacia():
			print(', ', end = '')
	print()
	return
def nueva_aerolinea(aeropuertos,vuelos,archivo_a_escribir):
	try:
		with open(archivo_a_escribir,'w',encoding = 'utf8') as archivo:
			arbol_a_escribir = mst_prim(vuelos,None,0)
			visitados = set()
			for v in arbol_a_escribir.obtener_vertices():
				for w in arbol_a_escribir.adyacentes(v):
					if not (v,w) in visitados and (w,v) not in visitados:
						visitados.add((v,w))
						arr_a_escribir = [v,w] + vuelos.ver_peso(v,w)
						linea = ','.join(arr_a_escribir)
						archivo.write(f'{linea}\n')
		print('OK')
	except FileNotFoundError:
		print(ERROR_NUEVA_AEROLINEA)
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

# def recorrer_mundo(aeropuertos,vuelos,desde):
# 	if not desde in aeropuertos:
# 		print(ERROR_RECORRER_MUNDO)
# 	recorrido = None
# 	costo = float('inf')
# 	padre = {}
# 	dist = {}
# 	for codigos in aeropuertos[desde]:
# 		padre_aux,dist_aux = camino_minimo(vuelos,codigos[1],0)
# 		costo_aux = max(dist_aux.values())
# 		if costo > costo_aux:
# 			costo = costo_aux
# 			recorrido = recorrido_aux
# 			padre= padre_aux
# 			dist = dist_aux
# 	for v in .obtener_vertices():
# 		minimos.encolar((dist[v],v))
# 	while not minimos.esta_vacio():
# 		rta.append(minimos.desencolar())
# 	largo = len(rta)
# 	for i in range(largo):
# 		print(f'{rta[i][1]}',end ='')
# 		if (i != largo -1):
# 			print(' -> ',end ='')
# 			if not recorrido.estan_unidos(rta[i+1][1],rta[i][1]):
# 				contador = i-1
# 				while not recorrido.estan_unidos(rta[i+1][1],rta[contador][1]) and contador >0:
# 					if recorrido.estan_unidos(rta[contador][1],rta[contador+1][1]):
# 						print(f'{rta[contador][1]} -> ',end ='')
# 						costo+=int(vuelos.ver_peso(rta[contador][1],rta[contador +1][1])[0])
# 					contador -= 1

# 	print()
# 	print(costo)
def _recorrer_mundo(vuelos,desde,actual,rta,valor,visitados,cant_visitados):
	if cant_visitados == len(vuelos):
		return True
	ady = vuelos.adyacentes(actual)
	tiempo_min = []
	for v in ady:
		tiempo_min.append((v,int(vuelos.ver_peso(actual,v)[0])))
	tiempo_ordenado = quicksort(tiempo_min)
	for tupla in tiempo_ordenado:
		v = tupla[0]
		pertenece = v not in visitados
		if v != desde:
			rta.append(v)
			if pertenece:
				visitados.add(v)
				cant_visitados+=1
			valor[0]+= int(vuelos.ver_peso(actual,v)[0])
			if(_recorrer_mundo(vuelos,desde,v,rta,valor,visitados,cant_visitados)):
				return True
			rta.pop()
			if pertenece:
				visitados.remove(v)
				cant_visitados-=1
			valor[0]-=int(vuelos.ver_peso(actual,v)[0])
	return False
def recorrer_mundo(aeropuertos,vuelos,desde):
	if not desde in aeropuertos:
		print(ERROR_RECORRER_MUNDO)
		return
	rta = []
	valor = [0]
	visitados = set()
	cant_visitados = 0
	for codigos in aeropuertos[desde]:
		codigo = codigos[1]
		rta.append(codigo)
		visitados.add(codigo)
		cant_visitados+=1
		if (_recorrer_mundo(vuelos,codigo,codigo,rta,valor,visitados,cant_visitados)):
			largo_rta = len(rta)
			for i in range(largo_rta - 1):
				print(f'{rta[i]} -> ',end = '')
			print(rta[largo_rta -1])
			print(valor[0])
			return
		else:
			rta.pop()
			visitados.remove(codigos)
			cant_visitados-=1
	print(ERROR_RECORRER_MUNDO)
	return

