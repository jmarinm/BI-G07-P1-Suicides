from pydantic import BaseModel
from models.DataModel import DataModel

class DataModelList(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    records: list[DataModel]
    
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["text"]