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
def digkstra (grafo,origen):
	dist = {}
	padres = {}
	for v in grafo.obtener_vertices(): dist[v] = float('inf')
	dist[origen] = 0
	padre[origen] = None
	q = Heap()
	q.encolar(q,(dist[origen],origen))
	while !q.esta_vacio():
		distancia,v = heapq.desencolar(q)
		for w in grafo.adyacentes(v):
			if distancia + grafo.peso(v,w) < dist[w]:
				dist[w] = dist[v] + grafo.peso(v,w)
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

