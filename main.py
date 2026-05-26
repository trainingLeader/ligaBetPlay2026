import os
import modules.utils as u
import modules.corefiles as cf
import modules.ui.mainMenu as menu
ligaBetPlay = {}
FILE_NAME = 'ligabetplay.json'

if __name__=="__main__":
   ligaBetPlay = cf.readDataFile(FILE_NAME)
   try:
       menu.menuOptions(ligaBetPlay)
   except ValueError as e:
       print(f"An error occurred: {e}")