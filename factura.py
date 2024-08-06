#creado por marito
#en la fecha x
#clase para atributos de tipo persona
import sqlite3
import facturaCelular
from pydantic import BaseModel
class Factura(BaseModel):
    identificador:str
    fecha:str
    comprador:str
    montoTotal:float
    



    def nueva(self, identificador,fecha, comprador, montoTotal):
        self.identificador = identificador
        self.fecha= fecha
        self.comprador=comprador
        self.montoTotal = montoTotal
        
  

    def guardaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura(identificador,fecha,comprador,montoTotal) VALUES (
        '{self.identificador}', 
        '{self.fecha}',
        '{self.comprador}',
        {self.montoTotal})'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Factura WHERE identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''UPDATE Factura SET fecha= 
        {self.fecha} , comprador=
        {self.comprador}, montoTotal=
        {self.montoTotal}  where identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()

    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Factura'):
            objetoInterno = Factura( identificador = fila[0],fecha= fila[1],comprador=fila[2],montoTotal = fila[3])
            objetoFacturaCelulars = facturaCelular.Factura_Celular(identificadorFactura=objetoInterno.identificador,identificadorCelular='')
            #objetoInterno.listaderepuestos = objetoFacturaCelular.seleccionatodoenBDxFactura()
            listaDevolver.append(objetoInterno)
        return listaDevolver
   