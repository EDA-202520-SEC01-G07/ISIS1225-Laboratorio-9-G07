import sys
import App.logic as logic
from DataStructures.List import array_list as al
# TODO Realice la importación de lista como estructura de datos auxiliar para la presentación de los resultados

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""
#  -------------------------------------------------------------
# Funciones para la carga de datos
#  -------------------------------------------------------------

def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de buses de singapur y crear MinPQ")
    print("3- Atender la siguiente ruta con mayor prioridad")
    print("0- Salir")
    print("*******************************************")

"""
Menu principal
"""

def main():
    working = True
    routesfile = 'bus_routes_14000.csv'
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            control = new_logic()
        elif int(inputs[0]) == 2:
            print("\nCargando información de rutas de buses....")
            logic.load_data(control, routesfile)
            print('Registros cargados: ' + str(logic.stops_size(control)))
            print('Elementos en la cola de prioridad: ' + str(logic.pq_size(control)))
            print('Ruta con mayor prioridad: ' + str(logic.pq_first(control)))
        elif int(inputs[0]) == 3:
            print("\nObteniendo la ruta con mayor prioridad: ")
            route = logic.get_next_route(control)
            if route:
                print('Ruta ID: ' + str(route['route_id']) + ', Dirección: ' + str(route['direction']) + ', Prioridad: ' + str(route['priority']))
                print('Elementos restantes en la cola de prioridad: ' + str(logic.pq_size(control)))
            else:
                print('No hay rutas en la cola de prioridad.')
        else:
            sys.exit(0)
    sys.exit(0)