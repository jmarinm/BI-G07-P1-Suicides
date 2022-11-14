from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    text: str


#Esta función retorna un diccionario con los atributos del modelo
    def to_dict(self):
        return {
            "text": self.text
        }
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["text"]
