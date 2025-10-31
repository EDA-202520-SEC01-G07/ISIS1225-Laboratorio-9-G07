from DataStructures.Tree import rbt_node as n
from DataStructures.List import single_linked_list as lt
def new_map():
    return {"root":None}
#Funciones prerequisito
def default_compare(key, element):
    if key < element:
        return -1
    elif key > element:
        return 1
    else:
        return 0
    
def size_tree(root):
    if root is not None:
        return 1 + size_tree(root["left"]) + size_tree(root["right"])
    else:
        return 0
    
def is_red(node):
    if node is not None and node["color"] == 0:
        return True
    else:
        return False
    
def rotate_left(node): #Cuando hay un enlace rojo en la derecha
    if node is None or node["right"] is None:
        return None
    rotar = node["right"]
    temporal = rotar["left"]
    rotar["left"] = node
    node["right"] = temporal
    rotar["color"]= node["color"]
    node["color"] = 0 #Red
    return rotar

def rotate_right(node): #Cuando hay dos enlaces rojos seguidos
    if node is None or node["left"] is None:
        return None
    left = node["left"]
    node["left"]=left["right"]
    left["right"] = node
    left["color"] = node["color"]
    node["color"] = 0
    return left

def flip_node_color(node): #Cambia el color de un solo nodo
    if node is not None:
        color = node["color"]
        if color == 0:
            node["color"] = 1
        else:
            node["color"] = 0
    return node

def flip_colors(node): #Cambia el color del nodo y de sus dos hijos
    if node is not None:
        flip_node_color(node)
        izq = node["left"]["color"]
        der = node["right"]["color"]
        if node["left"] is not None:
            if izq == 0:
                node["left"]["color"] = 1
            else:
                node["left"]["color"] = 0
        if node["right"] is not None:
            if der == 0:
                node["right"]["color"] = 1
            else:
                node["right"]["color"] = 0
    return node

#Funciones del LAB
def put(rbt, key, value): #Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    rbt["root"] = insert_node(rbt["root"], key, value)
    rbt["root"]["color"] = 1
    return rbt

def insert_node(root, key, value): #Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    if root is None:
        return n.new_node(key, value)
    cmp = default_compare(key, root["key"])
    if cmp == -1:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp == 1:
        root["right"] = insert_node(root["right"], key, value)
    elif cmp == 0:
        root["value"] = value
        
    if is_red(root["right"]) and not is_red(root["left"]): #Si hay un enlace rojo en la derecha
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]): #Si hay dos enlaces rojos a la izq seguidos
        root = rotate_right(root)
    if is_red(root["right"]) and is_red(root["left"]): #Si los hijos tienen enlace rojo
        flip_colors(root)
    return root 

def get(rbt, key): #Devuelve el valor de la llave
    return get_node(rbt["root"], key)

def get_node(root, key):
    if root == None:
        return None
    cmp = default_compare(key, root["key"])
    if cmp == 0:
        return root["value"]
    else:
        if cmp == -1:
            return get_node(root["left"], key)
        elif cmp == 1:
            return get_node(root["right"], key)
        
def contains(rbt, key):
    if get(rbt, key) is None:
        return False
    else:
        return True
    
def size(rbt):
    return size_tree(rbt["root"])
    
def size_tree(node):
    if node is None:
        return 0
    else:
        return 1 + size_tree(node['left']) + size_tree(node['right'])
    
def is_empty(rbt):
    if rbt["root"] is None:
        return True
    return False

#def key_set(): #Necesita def key_set_tree():
def key_set(rbt):
    list_keys = lt.new_list()
    return key_set_tree(rbt["root"], list_keys)
def key_set_tree(root, list_keys):
    if root is None:
        return list_keys
    else:
        key_set_tree(root["left"], list_keys)
        lt.add_last(list_keys, root["key"])
        key_set_tree(root["right"], list_keys)
        return list_keys

#def value_set(): #Necesita def value_set_tree():
def value_set(rbt):
    list_values = lt.new_list()
    return value_set_tree(rbt["root"], list_values)
def value_set_tree(root, list_values):
    if root is None:
        return list_values
    else:
        value_set_tree(root["left"], list_values)
        lt.add_last(list_values, root["value"])
        value_set_tree(root["right"], list_values)
        return list_values
def get_min(rbt):
    return get_min_node(rbt["root"])

def get_min_node(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["key"]
    else:
        return get_min_node(root["left"])
    
def get_max(rbt):
    return get_max_node(rbt["root"])

def get_max_node(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["key"]
    else:
        return get_max_node(root["right"])
    
def height(rbt):
    return height_tree(rbt["root"], -1)

def height_tree(root, contador):
    if root is None:
        return contador
    else:
        contador += 1
        return max(height_tree(root["left"], contador), height_tree(root["right"], contador))
    
def keys(rbt, key_initial, key_final):
    list_keys = lt.new_list()
    return keys_range(rbt["root"], key_initial, key_final, list_keys)

def keys_range(root, key_initial, key_final, list_keys):
    if root is None:
        return list_keys
    else:
        if key_initial <= root["key"] <= key_final:
            lt.add_last(list_keys, root["key"])
        if key_initial < root["key"]:
            keys_range(root["left"], key_initial, key_final, list_keys)
        if root["key"] < key_final:
            keys_range(root["right"], key_initial, key_final, list_keys)
        return list_keys

def values(rbt, key_initial, key_final):
    list_values = lt.new_list()
    return values_range(rbt["root"], key_initial, key_final, list_values)

def values_range(root, key_initial, key_final, list_value):
        if root is None:
            return list_value
        else:
            if key_initial <= root["key"] <= key_final:
                lt.add_last(list_value, root["value"])
            if key_initial < root["key"]:
                values_range(root["left"], key_initial, key_final, list_value)
            if root["key"] < key_final:
                values_range(root["right"], key_initial, key_final, list_value)
            return list_value
        
#Funciones extra para el reto
def delete_min(rbt): 
    rbt["root"] = delete_min_tree(rbt["root"])
    return rbt["root"]

def delete_min_tree(root): 
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    else:
        root["left"] = delete_min_tree(root["left"])
        return root

def delete_max(rbt): 
    rbt["root"] = delete_max_tree(rbt["root"])
    return rbt

def delete_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["left"]
    else:
        root["right"] = delete_max_tree(root["right"])
        return root