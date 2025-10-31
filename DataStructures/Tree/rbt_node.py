RED = 0
BLACK = 1


def new_node(key, value, color=RED):
    """
    Crea un nuevo nodo para un árbol rojo-negro  y lo retorna.
    color:0 - rojo  color:1 - negro
    Args:
        value: El valor asociado a la llave
        key: la llave asociada a la pareja
        size: El tamaño del subarbol que cuelga de este nodo
        color: El color inicial del nodo

    Returns:
        Un nodo con la pareja <llave, valor>
    Raises:
        Exception
    """
    node = {
        "key": key,
        "value": value,
        "size": 1,
        "left": None,
        "right": None,
        "color": color,
        "type": "RBT",
    }

    return node


def is_red(my_node):
    """
    Informa si un nodo es rojo
    Args:
        my_node: El nodo a revisar

    Returns:
        True si el nodo es rojo, False de lo contrario
    Raises:
        Exception
    """
    return my_node["color"] == RED


def get_value(my_node):
    """Retorna el valor asociado a una pareja llave valor
    Args:
        my_node: El nodo con la pareja llave-valor
    Returns:
        El valor almacenado en el nodo
    Raises:
        Exception
    """
    value = None
    if my_node is not None:
        value = my_node["value"]
    return value


def get_key(my_node):
    """Retorna la llave asociado a una pareja llave valor
    Args:
        my_node: El nodo con la pareja llave-valor
    Returns:
        La llave almacenada en el nodo
    Raises:
        Exception
    """
    key = None
    if my_node is not None:
        key = my_node["key"]
    return key


def change_color(my_node, color):
    """Cambia el color de un nodo
    Args:
        my_node: El nodo a cambiar
        color: El nuevo color del nodo
    Returns:
        None
    Raises:
        Exception
    """
    my_node["color"] = color
