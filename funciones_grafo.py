from grafo import *
from pila-cola import *
# import heapq


def bfs (grafo):
	origen = grafo.obtener_vertice_azar()
	visitados = set()
	padres = {}
	orden = {}
	q = Cola()
	vistados.add(origen)
	padres[origen] = None
	orden[origen] = 0
	q.encolar(origen)
	while not q.esta_vacia():
		v = q.desencolar()
		for w in grafo.adyacentes(v):
			if w not in visitados:
				visitados.add(w)
				q.encolar(w)
				padres[w] = v
				orden[w] = orden[v] + 1
	return padres,orden
def orden_topologico(grafo):
	grados = {}
	vertices = grafo.obtener_vertices()
	for v in vertices: grado[v] = 0
	for v in vertices:
		for w in grafo.adyacentes(v):
			grado[w] += 1
	q = Cola()
	for v in vertices:
		if grado[v] == 0 : q.encolar(v)
	resul = []
	while not q.esta_vacia():
		v = q.desencolar()
		resul.append(v)
		for w in grafo.adyacentes(v):
			grado[w] -=1
			if grado[w] == 0:
				q.encolar(w)
	if (len(resul) == len(grafo)):
		return resul
	return None
def digkstra (grafo,origen,i = None):
	dist = {}
	padres = {}
	for v in grafo.obtener_vertices(): dist[v] = float('inf')
	dist[origen] = 0
	padre[origen] = None
	q = Heap()
	q.encolar((dist[origen],origen))
	while !q.esta_vacio():
		distancia,v = q.desencolar()
		for w in grafo.adyacentes(v):
			peso = grafo.ver_peso(v,w)
			if i != None:
				peso = peso[i]
			if distancia + peso < dist[w]:
				dist[w] = dist[v] + peso
				padre[w] = v
				q.encolar((dist[w],w))
	return padre,dist
def centralidad(grafo):
	cent = {}
	vertices = grafo.obtener_vertices()
	for v in vertices: cent[v]=0
	for v in vertices:
		for w in vertices:
			if v == w: continue
			padre,distancia = digkstra(grafo,v)
			if padre[w] is None: continue
			actual = padre[w]
			while actual != v:
				cent[actual] += 1
				actual = padre[actual]
	return cent

def mst_prim(grafo,parametro_peso = None):
	vertice = grafo.obtener_vertice_azar()
	visitados = set()
	visitados.add(vertice)
	q = Heap()
	for w in grafo.adyacentes(vertice):
		peso = grafo.ver_peso(vertice,w)
		if parametro_peso:
			peso = peso[parametro_peso]
		q.encolar(peso,vertice,w)
	arbol = Grafo()
	while not q.esta_vacio():
		p,v,w = q.desencolar()
		if w in visitados: continue
		arbol.agregar_arista(v,w,p)
		visitados.add(w)
		for x in grafo.adyacentes(w):
			if x not in visitados:
				peso = grafo.ver_peso(w,x)
				if parametro_peso:
					peso = peso[parametro_peso]
				q.encolar(peso,w,x)
	return arbol