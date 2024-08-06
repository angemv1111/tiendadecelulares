# Importa el módulo sqlite3 para trabajar con bases de datos SQLite
import sqlite3
# Conecta a una base de datos llamada 'tiendaCelular.db'
con = sqlite3.connect('tiendaCelular.db')
# Crea un cursor para interactuar con la base de datos
cur = con.cursor()

# Define una función para crear las tablas en la base de datos
def create_tables():
    # Ejecuta una sentencia SQL para crear la tabla 'Celular' si no existe
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Celular (
    identificador TEXT PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    color TEXT,
    precio REAL
    );""")
    # Confirma (commit) los cambios realizados en la base de datos
    con.commit()
    # Ejecuta una sentencia SQL para crear la tabla 'Factura' si no existe
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Factura (
    identificador TEXT PRIMARY KEY,
    fecha TEXT,
    comprador TEXT,
    montoTotal REAL
    );""")
    # Confirma (commit) los cambios realizados en la base de datos
    con.commit()
    # Ejecuta una sentencia SQL para crear la tabla 'Factura_Celular' si no existe
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Factura_Celular (
    identificadorFactura TEXT,
    identificadorPrenda TEXT,
    CONSTRAINT fk_factura_Factura_Celular FOREIGN KEY (identificadorFactura)
    REFERENCES Factura (identificador),
    CONSTRAINT fk_Celular_Factura_Celular FOREIGN KEY (identificadorPrenda)
    REFERENCES Celular (identificador)
    );""")
    # Confirma (commit) los cambios realizados en la base de datos
    con.commit()

    # Cierra la conexión con la base de datos
    con.close()
