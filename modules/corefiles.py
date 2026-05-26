import os
import json
BASE_URL = 'data/'
def checkFile(archivo:str,data):
    if(not(os.path.isfile(BASE_URL+ archivo))):
        with open(BASE_URL + archivo ,"w") as bw:
            json.dump(data,bw,indent=4)

def readDataFile(archivo)-> dict:
    with open(BASE_URL+archivo,"r+") as rf:
       return json.load(rf)
    
def createData(archivo,data):
    with open(BASE_URL+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)

def updateData(data,srcData):
    if (len(data) <=0):
        print('😎 No se encontro información 😎')
        os.system('pause')
    else:
        for key in data.keys():
            if(key != 'nit'):
                if(type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if(bool(input(f'Desea modificar el {key2} s(si) o Enter No'))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                else:
                    if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key} :')
        srcData['proveedores'].update({data['nit']:data})
        UpdateFile('inventario.json',srcData)
    os.system('pause')

def UpdateFile(archivo,data):
    with open(BASE_URL+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)

def delData(data):
    delVal = input("Ingrese el Nit del proveedor que desea borrar -> ")
    data['proveedores'].pop(delVal)
    UpdateFile('inventario.json',data)

def searchProv(data):
    valor = input("Ingrese el Nit del proveedor a buscar -> ")
    result= data['proveedores'].get(valor)
    nit,nombrePro,tipo,direccion = result.values()
    ciudad,ubicacion,longitud,latitud = direccion.values()
    print(f'Nit {nit}:')
    os.system('pause')