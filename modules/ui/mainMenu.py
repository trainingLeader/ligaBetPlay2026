import modules.utils as u
import modules.teams.team as t
MENU_OPTIONS = '1. Agregar Equipo\n2. Agregar Planta tecnica\n3. Registrar Jugadores\n4. Programar fecha\n5. Estadisticas\n6. Buscar\n0. Salir'
def menuOptions(ligaBetPlay : dict):
    while True:
         u.borrar_pantalla()
         print(MENU_OPTIONS)
         op = int(input(':)'))
         match op:
            case 1:
                t.addTeam(ligaBetPlay)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 0:
                return
            case _:
                 print('Error en la opcion seleccionada')
                 u.pausar_pantalla()
                