class _Nodo:

    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

class Cola:

    def __init__(self):
        self.prim = None
        self.ultimo = None

    def __len__(self):
        'Devuelve la longitud de la cola'
        actual = self.prim
        contador = 0
        while actual:
            contador += 1
            actual = actual.prox
        return contador

    def ver_primero(self):
        'Devuelve el dato del primer elemento de la cola'
        return self.prim.dato

    def encolar(self, dato):
        'Agrega un elemento a la cola'
        nuevo_nodo = _Nodo(dato)
        if self.ultimo is not None:
            self.ultimo.prox = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.prim = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        'Saca el primer elemento de la cola'
        if self.esta_vacia():
            raise IndexError
        dato = self.prim.dato
        self.prim = self.prim.prox
        if not self.prim:
            self.ultimo = None
        return dato

    def esta_vacia(self):
        'Devuelve True si la cola esta vacia si no False'
        return self.ultimo == None

class Pila:

    def __init__(self):
        self.ult = None

    def apilar (self,dato):
        'Agrega un elemento a la pila'
        if self.ult == None:
            self.ult = _Nodo(dato)
        else:
            dato_a_agregar = _Nodo(dato,self.ult)
            self.ult = dato_a_agregar

    def desapilar(self):
        'Saca un elemento de la pila'
        dato = self.ult.dato
        self.ult = self.ult.prox
        return dato

    def esta_vacia(self):
        'Devuelve True si el atributo ultimo es igual a none si no False'
        return self.ult == None

    def ver_tope(self):
        'Devuelve el dato del ultimo nodo'
        return self.ult.dato
def obtener_padre(posicion):
    return (posicion - 1)//2
def ob_hijo_i(pos):
    return 2* pos + 1
def ob_hijo_d(pos):
    return 2*pos +2
def swap(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux
def upheap(arr,inicio,act,final):
    if act <= inicio or act >= final: return
    i = act
    while i > inicio:
        padre = obtener_padre(i)
        if (padre < inicio) : return
        if(arr[i][0] < arr[padre][0]):
            swap(arr,i,padre)
            i = padre
        else: return
    return

def downheap(arr,inicio,act,final):
    if act < inicio or act >= final or inicio == final: return
    i = act
    while(i < final):
        hijo_d = ob_hijo_d(i)
        hijo_i = ob_hijo_i(i)
        if(hijo_d < final and hijo_i < final):
            aux = 0
            if(arr[hijo_d][0] < arr[hijo_i][0]):
                aux = hijo_d
            else : aux = hijo_i
            if (arr[aux][0] < arr[i][0]):
                swap(arr,aux,i)
                i = aux
                continue
            else: return
        elif (hijo_d < final):
            if(arr[hijo_d][0] < arr[i][0]):
                swap(arr,i,hijo_d)
                i = hijo_d
                continue
        elif (hijo_i < final):
            if(arr[hijo_i][0] < arr[i][0]):
                swap(arr,i,hijo_i)
                i = hijo_i
                continue
            return
        else: return
    return
class Heap:
    def __init__(self):
        self.arr = []
        self.cantidad = 0
    def cantidad(self):
        return self.cantidad
    def ver_min(self):
        return self.arr[0]
    def esta_vacio(self):
        return self.cantidad == 0
    def desencolar(self):
        if self.esta_vacio(): return None
        elem = self.arr[0]
        swap(self.arr,0,self.cantidad -1)
        self.arr.pop(self.cantidad - 1)
        self.cantidad -=1
        downheap(self.arr,0,0,self.cantidad)
        return elem
    def encolar(self, elem):
        self.arr.append(elem)
        upheap(self.arr,0,self.cantidad,self.cantidad + 1)
        self.cantidad +=1

def quicksort(lista):
    if len(lista) < 2:
        return lista
    izquierda,medio,derecha = partir(lista,len(lista) -1)
    return quicksort(izquierda) + [medio] + quicksort(derecha)
def partir(lista, fin):
    pivote = lista[0]
    izquierda = []
    derecha = []
    i = 1
    while i <= fin:
        if lista[i][1] < pivote[1]:
            izquierda.append(lista[i])
            i += 1
        else:
            derecha.append(lista[i])
            i += 1
    return izquierda,pivote,derecha
def merge_sort(lista):
 """Ordena lista mediante el método merge sort.
 Pre: lista debe contener elementos comparables.
 Devuelve: una nueva lista ordenada."""
 if len(lista) < 2:
  return lista
 medio = len(lista) // 2
 izq = merge_sort(lista[:medio])
 der = merge_sort(lista[medio:])
 return merge(izq, der)

def merge(lista1, lista2):
 """Intercala los elementos de lista1 y lista2 de forma ordenada.
 Pre: lista1 y lista2 deben estar ordenadas.
 Devuelve: una lista con los elementos de lista1 y lista2."""

 i, j = 0, 0
 resultado = []

 while(i < len(lista1) and j < len(lista2)):
  if (lista1[i][1] > lista2[j][1]):
   resultado.append(lista1[i])
   i += 1
  else:
   resultado.append(lista2[j])
   j += 1

 # Agregar lo que falta
 resultado += lista1[i:]
 resultado += lista2[j:]

 return resultado