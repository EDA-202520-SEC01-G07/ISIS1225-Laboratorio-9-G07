def new_list():
    newlist={
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist
def get_element(my_list, pos):
    posicion = 0
    node = my_list["first"]
    while posicion < pos:
        node = node["next"]
        posicion += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    existe = False
    temp = my_list["first"]
    count = 0
    while not existe and temp != None:
        if cmp_function(element, temp["info"]) == 0:
            existe = True
        else:
            temp = temp["next"]
            count += 1

    if not existe:
        count = -1
    return count

    """
    new_node es una función auxiliar para funciones donde se tenga que crear un nodo
    """
def new_node():
    nodo={
        "info":None,
        "next":None
    }
    return nodo
    
def add_first(list, element):
    nodo = new_node()
    nodo["info"]=element
    
    if list["size"]==0:
        list["first"]=nodo
        list["last"]=nodo
    else:
        primero = list["first"]
        nodo["next"]=primero
        list["first"]=nodo
    list["size"]+=1
    return list

def add_last(list,element):
    nodo = new_node()
    nodo["info"]=element
    
    if list["size"]==0:
        list["first"]=nodo
        list["last"]=nodo
    else:
        list["last"]["next"]=nodo
        list["last"]=nodo
    list["size"]+=1
    return list

def size (list):
    return list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]

def is_empty(list):
    x = None
    if list["size"]==0:
        x = True
    else:
        x = False
    return x

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        sig = my_list["first"]["next"]
        my_list["first"]=sig
    else:
        nodo = my_list["first"]
        sig = nodo["next"]
        ant = None
        cont = 0
        while cont < pos:
            ant = nodo
            nodo=nodo["next"]
            sig=nodo["next"]
            cont+=1
        ant["next"]=sig
    my_list["size"]-=1
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif my_list["size"] == 1:
        primero = my_list["first"]["info"]
        my_list["first"]=None
        my_list["last"]=None
    else:
        primero = my_list["first"]["info"]
        my_list["first"]=my_list["first"]["next"]
    my_list["size"]-=1
    return primero

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif my_list["size"]==1:
        ultimo = my_list["last"]["info"]
        my_list["first"]=None
        my_list["last"]=None
    else:
        ultimo = my_list["last"]["info"]
        nodo = my_list["first"]
        ant = None
        while nodo["next"] != None:
            ant=nodo
            nodo = nodo["next"]
        my_list["last"]=ant
        ant["next"]=None
    my_list["size"]-=1
    return ultimo

def insert_element(my_list, element, pos):
    nuevo = new_node()
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
            nuevo["next"]=my_list["first"]
            my_list["first"]=nuevo
    else:
        nodo = my_list["first"]
        ant = None
        cont = 0
        while cont < pos:
            ant = nodo
            nodo = nodo["next"]
            cont +=1    
        nuevo["next"]=nodo
        ant["next"]=nuevo
        nuevo["info"]=element
        if nodo == None:
            my_list["last"]=nuevo
    my_list["size"]+=1
    return my_list  

def change_info(my_list, pos, new_info):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        nodo = my_list["first"]
        cont = 0
        while cont < pos:
            nodo = nodo["next"]
            cont +=1
        nodo["info"]=new_info
    return my_list

def exchange(my_list, p1, p2):
    if p1 == p2:
        return my_list

    nodo1 = my_list["first"]
    for _ in range(p1):
        nodo1 = nodo1["next"]

    nodo2 = my_list["first"]
    for _ in range(p2):
        nodo2 = nodo2["next"]

    nodo1["info"], nodo2["info"] = nodo2["info"], nodo1["info"]

    return my_list
 
def sub_list(my_list, pos, num_elmts):
    tam= my_list["size"]
    if pos < 0 or pos > tam:
        raise Exception('IndexError: list index out of range')
    else:
        if pos + num_elmts > tam:
            num_elmts = tam -pos
        s_list = new_list()
        nodo = my_list["first"]
        cont = 0
        
        while cont<pos:
            nodo = nodo["next"]
            cont+=1
        
        while s_list["size"] < num_elmts:
            s_list = add_last(s_list, nodo["info"])
            nodo=nodo["next"]
    return s_list

#Funciones Lab 5
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted
sort_criteria = default_sort_criteria


def insertion_sort(my_list, default_sort_criteria):
    nodo = my_list["first"]
    while nodo != None and nodo["next"] != None:
        if not default_sort_criteria(nodo["info"], nodo["next"]["info"]):
            temp = nodo["info"]
            nodo["info"] = nodo["next"]["info"]
            nodo["next"]["info"] = temp
            nodo = my_list["first"]
        else:
            nodo = nodo["next"]
    return my_list
        
def selection_sort(list, sort_criteria):
    n = size(list)
    for i in range(n):
        min_index = i
        min_elem = get_element(list, i)
        for j in range(i + 1, n):
            elem = get_element(list, j)
            if sort_criteria(elem, min_elem):
                min_elem = elem
                min_index = j
        if min_index != i:
            exchange(list, i, min_index)
    return list

def shell_sort(my_list, sort_criteria):
    tam = size(my_list)
    h=(3 * tam + 1)//3
    if tam == 0 or tam == 1:
        return my_list
    else: 
        while h > 0:
            for i in range(tam):
                temp = get_element(my_list, i)
                gap = i+h
                while gap < tam:
                    if sort_criteria(get_element(my_list, gap),temp):
                        exchange(my_list, gap, i)
                    gap += h
            h = h//3
    return my_list

def merge_sort(my_list, sort_crit):
    tam = size(my_list)
    if tam == 0: #lista vacía
        return my_list
    elif tam == 1: #lista 1 elemento, caso recursivo
        return my_list
    else:
        m = tam//2
        izq = new_list()
        for k in range(0, m):
            add_last(izq, get_element(my_list, k))
        izq_f = merge_sort(izq, sort_crit)
        
        der = new_list()
        for l in range (m+1, tam-1):
            add_last(der, get_element(my_list, l))
        der_f = merge_sort(der, sort_crit)
        return merge(izq_f, der_f, sort_crit)
    
def merge(lst1, lst2, sort_crit):
    l=0
    r=0
    new = new_list()
    while l < size(lst1) and r < size(lst2):
        elem_l = get_element(lst1, l)
        elem_r = get_element(lst2, r)
        x = sort_crit(elem_l, elem_r)
        if x == True: # l < r
            add_last(new, elem_l)
            l += 1
        else:
            add_last(new, elem_r)
            r += 1
    return new

def quick_sort(list, sort_crit):
    tam = list["size"]
    if tam == 0 or tam > 1:
        return list
    else:
        pivot = get_element(list, 0)
        menores = new_list()
        mayores = new_list()
        for i in range(1, list["size"]):
            elem = get_element(list, i)
            if sort_crit(elem, pivot):
                add_last(menores, elem)
            else:
                add_last(mayores, elem)
        sorted_less = quick_sort(menores, sort_crit)
        sorted_greater = quick_sort(mayores, sort_crit)
            
    sorted_array = new_list()
    for i in range(sorted_less["size"]):
        add_last(sorted_array, get_element(sorted_less, i))
    
    add_last(sorted_array, pivot)
    for i in range(sorted_greater["size"]):
        add_last(sorted_array, get_element(sorted_greater, i))
    return sorted_array
            