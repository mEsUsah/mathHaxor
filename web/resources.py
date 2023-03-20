import os

def problemsCssFile():
    dirName=os.path.dirname(__file__)
    absolutPath=os.path.join(dirName,'resources','css','problemPrint.css')
    
    return absolutPath