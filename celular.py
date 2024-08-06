import sqlite3
from pydantic import BaseModel
class Celular(BaseModel):
    identificador : str
    marca :str
    modelo :str
    color: str
    precio : int
    def nueva(self, identificador,marca,modelo,color,precio):
        self.identificador = identificador
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio= precio
     
    def guardaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Celular(identificador,marca,modelo,color,precio) VALUES (
        '{self.identificador}', 
         '{self.marca}',
         '{self.modelo}',
         '{self.color}',
          {self.precio})'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Celular WHERE identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        sql = f'''UPDATE Celular SET marca=
        {self.marca},precio=
         {self.precio} where identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('tiendaCelular.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Celular'):
            objetoInterno = Celular(identificador= fila[0], 
                                    marca= fila[1],
                                    modelo= fila[2],
                                    color= fila[3],
                                    precio= fila[4])
            listaDevolver.append(objetoInterno)
        return listaDevolver