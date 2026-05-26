import modules.corefiles as cf
import modules.utils as u
FILE_NAME = 'ligabetplay.json'
equipo = {}
titulos = {}
planta_tecnica = {}
jugadores = {}
estadisticas = {}
def addTeam(ligaBetPlay : dict):
    cf.checkFile(FILE_NAME,ligaBetPlay)
    ligaBetPlay = cf.readDataFile(FILE_NAME)
    nombre = input('Ingrese el nombre del equipo: ')
    estadio = input('Ingrese el nombre del estadio: ')
    ciudad = input('Ingrese la ciudad del equipo: ')
    fundacion = input('Ingrese el año de fundacion del equipo: ')
    equipo.setdefault("nombre", nombre)
    equipo.setdefault("estadio", estadio)
    equipo.setdefault("ciudad", ciudad)
    equipo.setdefault("fundacion", fundacion)
    equipo.setdefault("titulos", {})
    equipo.setdefault("planta_tecnica", {})
    equipo.setdefault("jugadores", {})
    equipo.setdefault("estadisticas", {})
    ligaBetPlay.update({str(len(ligaBetPlay)+1).zfill(2): equipo})
    cf.createData(FILE_NAME,ligaBetPlay)
    equipo.clear()

def searchTeam(ligaBetPlay : dict, name : str):
    for key, value in ligaBetPlay.items():
        if name.lower() in value.get("nombre").lower():
            return key
    return None

def deleteTeam(ligaBetplay : dict):
    name = input('Ingrese el nombre del equipo a eliminar: ')
    team = searchTeam(ligaBetplay, name)
    if team:
        # del ligaBetplay[team]
        ligaBetplay.pop(team)
        cf.createData(FILE_NAME,ligaBetplay)
        print(f'Equipo {name} eliminado exitosamente.')
        u.pausar_pantalla()
    else:
        print(f'No se encontró el equipo {name}.')
        u.pausar_pantalla()

def detailTeam(ligabetplay : dict):
    name = input('Ingrese el nombre del equipo a mostrar: ')
    team = searchTeam(ligabetplay, name)
    if team:
        print(f'Nombre {ligabetplay.get(team).get("nombre")}')
        print(f'Estadio {ligabetplay.get(team).get("estadio")}')
        print(f'Ciudad {ligabetplay.get(team).get("ciudad")}')
        print(f'Fundación {ligabetplay.get(team).get("fundacion")}')
        u.pausar_pantalla()
    else:
        print(f'No se encontró el equipo {name}.')
        u.pausar_pantalla()
