import os
class ElimiarEscenarios:
    def Eliminar():
        #Eliminar escenarios pasados
        Imagenes = os.listdir("Escenarios")
        for Imagen in Imagenes:
            # Comprobar si el archivo es una imagen
            if Imagen.endswith(".jpg") or Imagen.endswith(".png"):
                # Obtener la ruta completa del archivo
                ruta = os.path.join("Escenarios", Imagen)
                # Eliminar el archivo
                os.remove(ruta)