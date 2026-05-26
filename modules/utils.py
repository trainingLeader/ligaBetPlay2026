import os
import subprocess
import sys
def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        subprocess.run(["clear"], check=False)
    else:
        subprocess.run(["cmd", "/c", "cls"], check=False)


def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presione una tecla para continuar...")
    else:
        subprocess.run(["cmd", "/c", "pause"], check=False)