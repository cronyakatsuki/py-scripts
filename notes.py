import sys
import subprocess
import os
import getpass

python = '.py'
text = '.txt'
batch = '.cmd'
powershell = '.ps1'

extensions = {
    'python' : python,
    '.py' : python,
    'text' : text,
    '.txt' : text,
    'batch' : batch,
    '.cmd' : batch,
    'powershell' : powershell,
    '.ps1' : powershell,
}

startingDir = os.getcwd()
user = getpass.getuser()

def create():
    os.chdir('C:/Users/' + user + '/Documents/Notes/')
    
    extension = str(sys.argv[3])
    folderName = str(sys.argv[2])
    fileName = str(sys.argv[1])
    
    try:
        extension = extensions[extension]
    except Exception:
        print(extension)
        extension = ".txt"
    
    fileName = fileName + extension
    
    if os.path.isdir("./" + folderName):
        os.chdir("./" + folderName)
    else:
        os.mkdir(folderName)
        os.chdir("./" + folderName)
    
    if not os.path.isfile("./" + fileName):
        open(fileName, 'a').close()
    
    subprocess.Popen(['notepad++', fileName])
    
    os.chdir(startingDir)

if __name__ == '__main__':
    create()