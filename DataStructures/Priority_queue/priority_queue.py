from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq=True):
    """
    Crea una nueva cola de prioridad (heap).

    Parámetros:
    ------------
    is_min_pq : bool
        Indica si la cola de prioridad es de tipo min-heap (True) o max-heap (False).

    Retorna:
    ------------
    Una nueva instancia de una cola de prioridad.
    """
    lista = al.new_list()
    al.add_first(lista, None)
    cmp_function = default_compare_higher_value
    if is_min_pq:
        cmp_function = default_compare_lower_value
    return {
        'elements': lista,
        'size': 0,
        'cmp_function': cmp_function
    }

def priority(heap, parent, child):
    p = pqe.get_priority(parent)
    c = pqe.get_priority(child)
    cmp = heap["cmp_function"]
    return cmp(parent, child)
 
def insert(heap, priority, value):
    nuevo = pqe.new_pq_entry(priority, value)
    lista = heap["elements"]
    al.add_last(lista, nuevo)
    heap["size"] += 1
    pos = al.size(lista)-1
    swim(heap, pos)
    return heap

def exchange(heap, posi, posj):
    return al.exchange(heap["elements"],posi, posj)

def swim(heap, pos):
    centinela = False
    while pos > 1 and not centinela:
        padre = al.get_element(heap["elements"], int(pos//2))
        hijo = al.get_element(heap["elements"], int(pos))

        x = priority(heap, padre, hijo) #Si true entonces Padre tiene mayor prioridad que el hijo, False el hijo tiene mayor prioridad
        if x:#Si mi padre tiene mayor prioridad, no subo
            exchange(heap, pos, int(pos//2))
            pos = pos//2
        else:
            centinela = True
    return heap

def size(heap):
    return heap["size"]

def is_empty(heap):
    if size(heap) == 0:
        return True
    return False

def remove(heap):
    if is_empty(heap):
        return None
    lista = heap["elements"]
    elemento = al.get_element(lista, 1)
    al.exchange(lista, 1, al.size(lista)-1)
    al.remove_last(lista)
    sink(heap, 1)
    heap["size"] -= 1
    return pqe.get_value(elemento)

def sink(heap, pos):
    centinela = True
    while pos*2 <= size(heap) and centinela:
        padre = al.get_element(heap["elements"], int(pos))
        hijo1 = al.get_element(heap["elements"], int(pos*2))
        if pos*2+1 <= size(heap):
            hijo2 = al.get_element(heap["elements"], int(pos*2+1))
        else:
            hijo2 = None
            
        prioritario = 2*pos
        if hijo2 != None:
            x = priority(heap, hijo1, hijo2)
            if not x: 
                prioritario = 2*pos+1
        
        if not priority(heap, padre, al.get_element(heap["elements"], prioritario)): #Si el hijo tiene más prioridad que el padre (False), el padre baja
            exchange(heap, pos, prioritario)
            pos = prioritario
        else:
            centinela = False
    return heap

def get_first_priority(heap):
    if size(heap) >= 1:
        return al.get_element(heap["elements"],1)["value"]
    return None

def is_present_value(my_heap, value):
    lista = my_heap["elements"]
    for i in range(1, al.size(lista)):
        elemento = al.get_element(lista, i)
        if pqe.get_value(elemento) == value:
            return i
    return -1

def contains(my_heap, value):
    pos = is_present_value(my_heap, value)
    if pos != -1:
        return True
    return False
    
def improve_priority(my_heap, priority, value):
    pos = is_present_value(my_heap, value)
    if pos == -1:
        return my_heap
    elemento = al.get_element(my_heap["elements"], pos)
    pqe.set_priority(elemento, priority)
    swim(my_heap, pos)
    return my_heap

