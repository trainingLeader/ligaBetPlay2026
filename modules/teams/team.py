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

def addTechnicalStaff(ligaBetPlay : dict):
    name = input('Ingrese el nombre del equipo a mostrar: ')
    team = searchTeam(ligaBetPlay, name)
    if team:
        myTeam = ligaBetPlay.get(team)
        print(f'Staff tecnico del equipo {myTeam.get("nombre")}')
        planta_tecnica.setdefault("tecnico", input('Ingrese el nombre del DT: '))
        planta_tecnica.setdefault("medico", input('Ingrese el nombre del MD: '))
        planta_tecnica.setdefault("preparador_fisico", input('Ingrese el nombre del preparador físico: '))
        planta_tecnica.setdefault("psicologo", input('Ingrese el nombre del psicologo: '))
        planta_tecnica.setdefault("entrenador_arqueros", input('Ingrese el nombre del entrenador de arqueros: '))
        planta_tecnica.setdefault("entrenador_asistente", input('Ingrese el nombre del entrenador asistente: '))
        myTeam.get("planta_tecnica").update({str(len(myTeam.get("planta_tecnica"))+1).zfill(2): planta_tecnica})
        cf.createData(FILE_NAME,ligaBetPlay)
        planta_tecnica.clear()
        u.pausar_pantalla()
    else:
        print(f'No se encontró el equipo {name}.')
        u.pausar_pantalla()

def addPlayer(ligaBetPlay : dict):
    pass

def addStatistics(ligaBetPlay : dict):
    pass

def championShips(ligaBetPlay : dict):
    name = input('Ingrese el nombre del equipo a mostrar: ')
    team = searchTeam(ligaBetPlay, name)
    if team:
        myTeam = ligaBetPlay.get(team)
        print(f'Titulos del equipo {myTeam.get("nombre")}')
        titulos.setdefault("liga", input('Ingrese el nombre de la liga: '))
        titulos.setdefault("anio", input('Ingrese el año del titulo: '))
        titulos.setdefault("torneo", input('Ingrese el nombre del torneo: '))
        myTeam.get("titulos").update({str(len(myTeam.get("titulos"))+1).zfill(2): titulos})
        cf.createData(FILE_NAME,ligaBetPlay)
        titulos.clear()
        u.pausar_pantalla()
    else:
        print(f'No se encontró el equipo {name}.')
        u.pausar_pantalla()