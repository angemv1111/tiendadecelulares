import sqlite3
from pydantic import BaseModel
class Factura_Celular(BaseModel):
    identificadorFactura:str
    identificadorCelular:str
    def nueva(self, identificadorFactura,identificadorCelular):
        self.identificadorFactura = identificadorFactura
        self.identificadorCelular= identificadorCelular

     
    def guardaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura_Celular(identificadorFactura,identificadorCelular) VALUES (
        '{self.identificadorFactura}', 
        '{self.identificadorCelular}'
        )'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBDxFactura(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute(f'SELECT * FROM Factura_Celular where identificadorFactura= {self.identificadorFactura}'):
            objetoInterno =  Factura_Celular( identificadorFactura = fila[0],identificadorCelular= fila[1])
            listaDevolver.append(objetoInterno)
        return listaDevolver