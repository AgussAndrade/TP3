class Grafo:
	def __init__(self):
		self.vertices = {}
		self.cantidad_vertices = 0
		self.cantidad_aristas = 0

	def agregar_vertice(self,vertice):
		self.vertices[vertice] = {}
		self.cantidad_vertices += 1

	def agregar_arista(self,v_salida,v_llegada,peso = 0):
		if not v_salida in self.vertices :
			self.vertices[v_salida] = {}
			self.cantidad_vertices +=1
		if not v_llegada in self.vertices:
			self.vertices[v_llegada] = {}
			self.cantidad_vertices +=1
		self.vertices[v_salida][v_llegada] = peso
		self.cantidad_aristas +=1
	def estan_unidos(self,v1,v2):
		if v1 in self.vertices and v2 in self.vertices:
			if v2 in self.vertices[v1]: return True
		return False
	def sacar_arista(self,v_salida,v_llegada):
		if v_salida in self.vertices and v_llegada in self.vertices:
			if v_llegada in self.vertices[v_salida]:
				self.vertices[v_salida].pop(v_llegada)
				self.cantidad_aristas -=1
				return True
		return False
	def sacar_vertice(self,v):
		if v in self.vertices:
			for key in self.vertices.keys():
				if v in key:
					key.pop(v)
					self.cantidad_aristas -=1
			self.vertices.pop(v)
			self.cantidad_vertices -=1
			return True
		return False
	def adyacentes(self,vertice):
		if vertice in self.vertices:
			rta = []
			for v in self.vertices[vertice].keys():
				rta.append(v)
			return rta
		return None
	def ver_peso(self,v_salida,v_llegada):
		if v_salida in self.vertices and v_llegada in self.vertices:
			return self.vertices[v_salida][v_llegada]
		return None
	def existe(self,v):
		if v in self.vertices:
			return True
		return False
	def obtener_vertice_azar (self):
		vertices = self.vertices.keys()
		if len(vertices) > 0 : return vertices[0]
		return None
	def obtener_vertices (self):
		rta = []
		for v in self.vertices.keys():
			rta.append(v)
		return rta
	def __len__(self):
		return self.cantidad_vertices