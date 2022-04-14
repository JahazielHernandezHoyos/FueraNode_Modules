import os

def elimnar_node_modules():
    current_dir = os.getcwd()
    for dir in os.listdir(current_dir):
        if dir == "node_modules":
            os.system("rmdir /S /Q node_modules")

def buscar_dentro_de_carpetas():
    current_dir = os.getcwd()
    for dir in os.listdir(current_dir):
        if os.path.isdir(dir):
            if dir == "node_modules":
                elimnar_node_modules()
                print("elimine carpeta node molesta yuju")
            else:
                os.chdir(dir)
                buscar_dentro_de_carpetas()
                os.chdir("..")
        
buscar_dentro_de_carpetas()
