import modules.utils as u
import modules.teams.team as t
MENU_OPTIONS = '1. Agregar Equipo\n2. Agregar Planta tecnica\n3. Registrar Jugadores\n4. Programar fecha\n5. Estadisticas\n6. Buscar\n7. Eliminar Equipo \n8. Detalles del Equipo \n0. Salir'
def menuOptions(ligaBetPlay : dict):
    while True:
        try:
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
                case 7:
                    t.deleteTeam(ligaBetPlay)
                case 8:
                    t.detailTeam(ligaBetPlay)
                case 0:
                    return
                case _:
                    print('Error en la opcion seleccionada')
                    u.pausar_pantalla()
        except KeyboardInterrupt:
            print("\nOps Presionaste algo ummmm...")
            u.pausar_pantalla()
            continue
        except ValueError as e:
            print(f"An error occurred: {e}")
            u.pausar_pantalla()
            continue
    
                    