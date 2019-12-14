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
La centralidad es una métrica para definir la importancia de un vértice en una red (algo muy utilizado en redes sociales). Hay distintas formas de medir esto: 
- Centralidad de grado (literalmente, el grado de cada vértice). 
- Centralidad de cercanía (suma de todas las distancias al resto de los vértices)
- Centralidad de decaimiento (suma de un delta entre 0 y 1, que elevamos a la distancia). 
- Centralidad de intermediación, o Betweenness (cantidad de veces que se utiliza al vértice como intermediario en un camino mínimo entre dos pares de vértices). 
- Centralidad de autovalores (la importancia de un vértice es relativa a la importancia de sus vecinos). Si, está hablando de los autovalores de la matriz de adyacencia. 

Y otras tantas más, que se estudian al analizar redes sociales. 

En particular, la que se vio en clase es la de Intermediación. Esto es útil por ejemplo para el TP3, porque el enunciado es explícito en que le interesa saber en cuáles aeropuertos se tienden a hacer más escalas*. Si aplican Pagerank para resolver este problema, en realidad van a estar calculando una aproximación para la centralidad de autovalores, que en pos de aplicación de algoritmos sencillos, podemos considerar que son similares. 

Por qué utilizar una centralidad y no otra? A priori en el TP tiene sentido, pero en otras aplicaciones podría no ser tan evidente. Lo dejamos para algún curso de Redes Sociales el analizar cada caso y ver ejemplos de cada uno :) 

* Honestamente me pareció raro el resultado, pero buscando en internet me enteré que es efectivamente correcto: el aeropuerto de Atalanta es en sí el más utilizado para esto, y por ende uno de los más importantes del mundo.