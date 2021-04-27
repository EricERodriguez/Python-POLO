try:
    f = open("miarchivo.txt", "w")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
except FileNotFoundError:
    print("El archivo no se encontro.")
finally:
    print("El try y except finalizo")