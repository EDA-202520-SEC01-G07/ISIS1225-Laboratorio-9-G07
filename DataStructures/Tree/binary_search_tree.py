from DataStructures.Tree import bst_node as n
from DataStructures.List import array_list as lt
def new_map():
    return {"root": None}

def size(my_bst):
    return size_tree(my_bst["root"])
    
def size_tree(node):
    if node is None:
        return 0
    else:
        return 1 + size_tree(node['left']) + size_tree(node['right'])

def put(my_bst, key, value):
    if my_bst["root"] != None:
        my_bst["root"] = insert_node(my_bst["root"], key, value)
        return my_bst
    else:
        my_bst["root"] = n.new_node(key, value)
        return my_bst

def insert_node(root, key, value):
    if root is None:
        root = n.new_node(key, value)
    elif key == root['key']:
        root['value'] = value
    elif key < root['key']:
        root["left"] = insert_node(root['left'], key, value)
    else:
        root["right"] = insert_node(root['right'], key, value)
    return root

def get(bst, key):
    return get_node(bst["root"], key)

def get_node(root, key):
    if root == None:
        return None
    elif root["key"] == key:
        return root["value"]
    else:
        if key < root["key"]:
            return get_node(root["left"], key)
        if key > root["key"]:
            return get_node(root["right"], key)
        

def contains(my_bst, key):
    if get(my_bst, key) is not None:
        return True
    else:
        return False

def is_empty(bst):
    if bst["root"] is None:
        return True
    return False

def key_set(bst):
    lista = lt.new_list()
    key_set_tree(bst["root"], lista)
    return lista
    
def key_set_tree(root, key_list):
    if root is None:
        return key_list
    else:
        lt.add_last(key_list, root["key"])
        key_set_tree(root["left"], key_list)
        key_set_tree(root["right"], key_list)
        return key_list
    
def value_set(bst):
    lista = lt.new_list()
    value_set_tree(bst["root"], lista)
    return lista
    
def value_set_tree(root, value_list):
    if root is None:
        return value_list
    else:
        lt.add_last(value_list, root["value"])
        key_set_tree(root["left"], value_list)
        key_set_tree(root["right"], value_list)
        return value_list
    
def get_min(bst):
    return get_min_tree(bst["root"])

def get_min_tree(root):
    if root is None:
        return None
    elif root["left"] is None:
        return root["key"]
    else:
        return get_min_tree(root["left"])
    
def get_max(bst):
    return get_max_tree(bst["root"])

def get_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["key"]
    else:
        return get_max_tree(root["right"])

def delete_min(bst): 
    bst["root"] = delete_min_tree(bst["root"])
    return bst["root"]

def delete_min_tree(root): 
    if root is None:
        return None
    elif root["left"] is None:
        return root["right"]
    else:
        root["left"] = delete_min_tree(root["left"])
        return root

def delete_max(bst): 
    bst["root"] = delete_max_tree(bst["root"])

def delete_max_tree(root):
    if root is None:
        return None
    elif root["right"] is None:
        return root["left"]
    else:
        root["right"] = delete_max_tree(root["right"])
        return root
    

def keys(bst, key_initial, key_final):
    list_keys = lt.new_list()
    return keys_range(bst["root"], key_initial, key_final, list_keys)

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

def values(bst, key_initial, key_final):
    list_values = lt.new_list()
    return values_range(bst["root"], key_initial, key_final, list_values)

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

def height(bst):
    return height_tree(bst["root"], -1)

def height_tree(root, contador):
    if root is None:
        return contador
    else:
        contador += 1
        return max(height_tree(root["left"], contador), height_tree(root["right"], contador))