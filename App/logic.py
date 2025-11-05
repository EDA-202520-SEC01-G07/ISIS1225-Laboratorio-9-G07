"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import csv
import time
import os
from DataStructures.List import array_list as al
from DataStructures.Priority_queue import priority_queue as pq
# TODO Realice la importación de priority queue
# TODO Realice la importación de ArrayList (al) o SingleLinked (sl) como estructura de datos auxiliar para sus requerimientos


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/singapur_bus_routes/'


def new_logic():
    """Inicializa el analizador.

    stops: Lista para guardar las paradas de bus (array_list)
    routes_pq: Cola de prioridad para gestionar las rutas de bus (priority_queue)

    Returns:
        dict: Analizador con las claves 'stops' y 'routes_pq' inicializadas a None.
    """
    analyzer = {
        'stops': None,
        'routes_pq': None
    }
    
    analyzer['stops'] = al.new_list() #TODO completar la creación de la lista
    analyzer['routes_pq'] = pq.new_heap() #TODO completar la creación de la cola de prioridad

    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def load_data(analyzer, file):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for stop in input_file:
        add_stop(analyzer, stop)
    return analyzer


def add_stop(analyzer, stop):
    """
    Adiciona una parada al analizador.

    Parámetros:
    ------------
    analyzer : dict
        Estructura de datos principal del analizador que contiene, entre otros,
        la lista de paradas ('stops') y la cola de prioridad ('pq').
    stop : dict
        Información completa de una parada de bus, que incluye al menos los campos:
        - ServiceNo: número de la ruta del bus
        - Direction: dirección del recorrido (1 o 2)
        - StopSequence: número de secuencia de la parada en la ruta
        - WD_FirstBus: hora de salida del primer bus en día laboral
        (además de otros datos complementarios)
    """

    # Agregar la parada a la lista general de paradas
    al.add_last(analyzer['stops'], stop)

    # TODO: Adicionar nuevo elemento a la cola de prioridad.
    # Para agregar un elemento a la cola de prioridad tener en cuenta las paradas
    # cuyo StopSequence sea igual a 1. 
    # La prioridad debe ser el valor de 'WD_FirstBus' y el valor asociado debe ser
    # un diccionario con la siguiente estructura:
    # {
    #   'route_id': stop['ServiceNo'],
    #   'direction': stop['Direction'],
    #   'priority': stop['WD_FirstBus']
    # }
    # Ejemplo:
    # if stop['StopSequence'] == 1:
    #     element = {
    #         'route_id': stop['ServiceNo'],
    #         'direction': stop['Direction'],
    #         'priority': stop['WD_FirstBus']
    #     }
    #     pq.insert(analyzer['pq'], element['priority'], element)
    lista_prioridad = analyzer["routes_pq"]
    if stop["StopSequence"] == "1":
        element = {
             'route_id': stop['ServiceNo'],
             'direction': stop['Direction'],
             'priority': stop['WD_FirstBus']
        }
        pq.insert(lista_prioridad, stop['WD_FirstBus'], element)
    return analyzer


# ___________________________________________________
#  Funciones de consulta
# ___________________________________________________

def stops_size(analyzer):
    """
    Obtener el número de paradas de bus
    """
    return al.size(analyzer['stops'])

def pq_size(analyzer):
    """
    Obtener el número de elementos en la cola de prioridad
    """
    return pq.size(analyzer['routes_pq'])

def pq_first(analyzer):
    """
    Obtener el primer elemento en la cola de prioridad
    """
    return pq.get_first_priority(analyzer['routes_pq'])

def get_next_route(analyzer):
    """
    Atiende la cola de prioridad del analizador.

    Esta función consulta la ruta con mayor prioridad (es decir, la de menor valor 
    de 'WD_FirstBus'), la elimina de la cola de prioridad y retorna la información 
    de dicha ruta.

    Parámetros:
    ------------
    analyzer : dict
        Estructura de datos principal del analizador que contiene, entre otros,
        la cola de prioridad ('pq') con las rutas pendientes de procesar.

    """

    # TODO: completar la función.
    # Pasos a seguir:
    # 1. Consultar el elemento con mayor prioridad en la cola (sin eliminarlo) usando pq.min(analyzer['pq'])
    # 2. Eliminar ese elemento de la cola usando pq.delMin(analyzer['pq'])
    # 3. Retornar la ruta obtenida en el paso 1
    #
    # Ejemplo:
    # next_route = pq.min(analyzer['pq'])
    # pq.delMin(analyzer['pq'])
    # return next_route
    lista_pq = analyzer["routes_pq"]
    ruta = pq.get_first_priority(lista_pq)
    pq.remove(lista_pq)
    return ruta