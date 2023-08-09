import subprocess

def openGedit():
    try:
        subprocess.run(["gedit"])
        return {"status":"ok", "message":"Vale abriendo gedit"}
    except Exception as e:
        return {"status":"erro", "message": e}

def openBrowser(url):
    try:
        subprocess.run(["google-chrome", url])
        return {"status":"ok", "message":"Vale abriendo navegador"}
    except Exception as e:
        return {"status":"erro", "message": e}

def openNautilus():
    try:
        subprocess.run(["nautilus"])
        return {"status":"ok", "message":"Vale abriendo nautilus"}
    except Exception as e:
        return {"status":"erro", "message": e}

def openVsc():
    try:
        subprocess.run(["code"])
        return {"status":"ok", "message":"Vale abriendo code"}
    except Exception as e:
        return {"status":"erro", "message": e}