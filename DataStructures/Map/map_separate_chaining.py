from DataStructures.List import array_list as alt
from DataStructures.List import single_linked_list as slt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random 

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def rehash(my_map):
    """
    Realiza un rehash de la tabla de simbolos.
    Para realizar un rehash se debe seguir los siguientes pasos:
    Crear una nueva tabla map_separate_chaining con capacity que sea el siguiente primo al doble del capacity actual.
    Recorrer la tabla actual y reinsertar cada elemento en la nueva tabla.
    Asignar la nueva tabla como la tabla actual.
    Retornar la tabla nueva.
    """
    
    cap_nueva = mf.next_prime(2*my_map["capacity"])
    new_table = alt.new_list()
    for i in range(0, cap_nueva):
        elem = slt.new_list()
        alt.add_last(new_table, elem)
        
    contador = 0
    cap_ant = my_map["capacity"]
    old_table = my_map["table"]
    my_map["capacity"] = cap_nueva
    
    for i in range(cap_ant):
        entry = alt.get_element(old_table, i)
        for j in range(slt.size(entry)):
            elem = slt.get_element(entry, j)
            h = mf.hash_value(my_map, elem["key"]) % my_map["capacity"]
            
            entry_nuevo = alt.get_element(new_table, h)
            slt.add_last(entry_nuevo,me.new_map_entry(elem["key"], elem["value"]))
            contador += 1
    my_map["size"] = contador 
    my_map["current_factor"] = my_map["size"]/my_map["capacity"]
    my_map["table"] = new_table
    return my_map

def new_map(num_elements, load_factor, prime=109345121):
    y=mf.next_prime(num_elements//load_factor)
    x = alt.new_list()
    map = {"prime": prime,
           "capacity": y,
           "scale":1,
           "shift":0,
           "table": x,
           "current_factor": 0,
           "limit_factor": load_factor,
           "size": 0
    }
    for i in range(y):
        lista = slt.new_list()
        alt.add_last(map["table"], lista)
    return map

def put(mapa, key, value):
    llave = mf.hash_value(mapa, key) % mapa["capacity"] #Hash de la llave
    entry = alt.get_element(mapa["table"], llave)
    appears = False
    for i in range(slt.size(entry)):
        elem = slt.get_element(entry, i)
        if elem["key"]==key:
            appears = True
            me.set_value(elem, value)
            break
    if appears == False:
        slt.add_last(entry, me.new_map_entry(key, value))
        mapa["size"] += 1
        mapa["current_factor"] = mapa["size"]/mapa["capacity"]
       
    if mapa["current_factor"] > mapa["limit_factor"]:
        mapa = rehash(mapa)
    return mapa

def contains(mapa, key):
    encontrado = False
    hash = mf.hash_value(mapa, key)
    entry = alt.get_element(mapa["table"], hash)
    for i in range(slt.size(entry)):
        elem = slt.get_element(entry, i)
        if key == me.get_key(elem):
            encontrado = True
    return encontrado

def get(mapa, key):
    hash = mf.hash_value(mapa,key)
    entry = alt.get_element(mapa["table"], hash)
    x = None
    for i in range(slt.size(entry)):
        elem = slt.get_element(entry, i)
        if key == me.get_key(elem):
            x = me.get_value(elem)
    return x

def remove(mapa, key):
    hash= mf.hash_value(mapa,key)
    entry = alt.get_element(mapa["table"], hash)
    for i in range(slt.size(entry)):
        elem = slt.get_element(entry, i)
        if key == me.get_key(elem):
            slt.delete_element (entry, i)
            mapa["size"] -= 1
            mapa["current_factor"] = mapa["size"]/mapa["capacity"]
    return mapa

def size(mapa):
    return mapa["size"]

def is_empty(mapa):
    vacio = False
    if mapa["size"]==0:
        vacio = True
    return vacio

def key_set(mapa):
    tam = alt.size(mapa["table"])
    llaves = alt.new_list()
    for i in range(tam):
        entry = alt.get_element(mapa["table"], i)
        for i in range(slt.size(entry)):
            elem = slt.get_element(entry, i)
            alt.add_last(llaves, me.get_key(elem))
    return llaves

def value_set(mapa):
    tam = alt.size(mapa["table"])
    valores = alt.new_list()
    for i in range(tam):
        entry = alt.get_element(mapa["table"], i)
        for i in range(slt.size(entry)):
            elem = slt.get_element(entry, i)
            alt.add_last(valores, me.get_value(elem))
    return valores