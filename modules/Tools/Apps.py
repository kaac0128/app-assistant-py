import subprocess
import jsonpickle

def vsc_open():
    subprocess.run(["code"])
    return jsonpickle.encode(True)