import modules.corefiles as cf
FILE_NAME = 'teams.json'
def addTeam(ligaBetPlay : dict):
    equipo = {
        "nombre" : 'A. Nacional'
    }
    cf.checkFile(FILE_NAME,ligaBetPlay)
    ligaBetPlay = cf.readDataFile(FILE_NAME)
    ligaBetPlay.update(equipo)
    cf.createData(FILE_NAME,ligaBetPlay)


