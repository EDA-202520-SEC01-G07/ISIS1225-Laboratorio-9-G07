from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random 

def is_available(table, pos):
   if pos < 0 or pos >= lt.size(table):
      return False
   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   capacity = my_map["capacity"]
   hash_value = hash_value % capacity
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail   

def rehash(my_map):
   """
   Realiza un rehash de la tabla de simbolos.
   Para realizar un rehash se debe seguir los siguientes pasos:
   Crear una nueva tabla map_linear_probing con capacity que sea el siguiente primo al doble del capacity actual.
   Insertar los elementos de la tabla actual en la nueva tabla uno por uno.
   Asignar la nueva tabla a la tabla actual.
   Retornar la tabla nueva.
   """
   cap_nueva = mf.next_prime(2*my_map["capacity"])
   cap_ant = my_map["capacity"]
   nuevo = new_map(int(0.5*cap_nueva),0.5)
   
   
   """
   my_map["capacity"] = cap_nueva

   new_table = lt.new_list()
   for i in range(cap_nueva):
        lt.add_last(new_table, me.new_map_entry(None,None))
   
   
   for i in range(cap_ant):
      entry = lt.get_element(my_map["table"], i)
      if me.get_key(entry) is not None:
         llave = me.get_key(entry)
         valor = me.get_value(entry)
         h = mf.hash_value(my_map, llave) % my_map["capacity"] #Encuentra el nuevo valor hash
         ocupied, pos = find_slot(my_map, llave, h)
         if ocupied: #Si existe la llave, se cambia el valor
            me.set_value(lt.get_element(new_table, pos), valor)
         else: #No existe y se debe agregar la llave-valor  
            me.set_key(lt.get_element(new_table, pos), llave)
            me.set_value(lt.get_element(new_table, pos), valor)
   """
   
   for i in range(cap_ant):
      entry = lt.get_element(my_map["table"], i)
      if me.get_key(entry) is not None:
         llave = me.get_key(entry)
         valor = me.get_value(entry)
         put(nuevo, llave, valor)
   
   return nuevo

def new_map(num_elements, load_factor, prime=109345121):
    y=mf.next_prime(num_elements//load_factor)
    x = lt.new_list()
    for i in range(y):
        lt.add_last(x, me.new_map_entry(None,None))
    map = {"prime": prime,
           "capacity": y,
           "scale": random.randrange(1, prime-1),
           "shift":random.randrange(0, prime-1),
           "table": x,
           "current_factor": 0,
           "limit_factor": load_factor,
           "size": 0
    }
    return map
    
def put(mapa, key, valor):
   llave = mf.hash_value(mapa, key) #Hash de la llave
   ocupied, pos = find_slot(mapa, key, llave)
   entry = lt.get_element(mapa["table"], pos)
   if ocupied: #Si existe la llave, se cambia el valor
      me.set_value(entry, valor)
   else: #No existe y se debe agregar la llave-valor y añadir 1 en current factor
      me.set_key(entry, key)
      me.set_value(entry, valor)
      mapa["size"] += 1
      mapa["current_factor"] = mapa["size"]/mapa["capacity"]
      
   if mapa["current_factor"] > mapa["limit_factor"]:
      mapa = rehash(mapa)
#Si el current_factor supera el limit_factor, se realiza un rehash de la tabla.
#Se retorna la tabla con el nuevo elemento agregado.
   return mapa

def contains(my_map, key):
   encontrado = False
   for i in range(my_map["capacity"]):
      current = lt.get_element(my_map["table"], i)
      if me.get_key(current) == key:
         encontrado = True
         return encontrado
   return encontrado

def get(my_map, key):
   for i in range(my_map["capacity"]):
      current = lt.get_element(my_map["table"], i)
      if me.get_key(current) == key:
         return me.get_value(current)
   return None

def remove(mapa, key):
   hash = mf.hash_value(mapa, key)
   ocupied, pos = find_slot(mapa, key, hash)
   entry = lt.get_element(mapa["table"], pos)
   me.set_value(entry, "__EMPTY__")
   me.set_key(entry, "__EMPTY__")
   mapa["size"] -= 1
   mapa["current_factor"] = mapa["size"]/mapa["capacity"]
   return mapa

def size(mapa):
   return mapa["size"]

def is_empty(mapa):
   vacio = False
   if mapa["size"] == 0:
      vacio = True
   return vacio

def key_set(mapa):
   tam = lt.size(mapa["table"])
   llaves = lt.new_list()
   for i in range(tam):
      entry = lt.get_element(mapa["table"], i)
      if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
            lt.add_last(llaves, me.get_key(entry)) 
   return llaves


def value_set(mapa):
   tam = lt.size(mapa["table"])
   valores = lt.new_list()
   for i in range(tam):
      entry = lt.get_element(mapa["table"], i)
      if me.get_value(entry) is not None and me.get_value(entry) != "__EMPTY__":
            lt.add_last(valores, me.get_value(entry))
   return valores
