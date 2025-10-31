
from DataStructures.List import array_list as al
from DataStructures.Priority_queue import priority_queue as pq
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
    return {
        'elements': al.new_list(),
        'size': 0,
        'is_min_pq': None #cambiarlo despues
    }