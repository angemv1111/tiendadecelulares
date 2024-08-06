from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import celular
import factura
import facturaCelular
import bdscript
app= FastAPI()

bdscript.create_tables()

@app.get("/index")
async def root():
    return FileResponse('index.html')

@app.get("/sidePic")
async def root():
    return FileResponse("Fotos/sideFoto.jpg")
@app.get("/sidePic2")
async def root():
    return FileResponse("Fotos/sideFoto2.jpg")

@app.get("/fondo3")
async def root():
    return FileResponse("Fotos/fondoBarbie.jpg")

@app.get("/telefono")
async def root():
    return FileResponse("Fotos/iph.jpg")

@app.get("/doblada")
async def root():
    return FileResponse("Fotos/doblada.jpg")

@app.get("/tienda2")
async def root():
    return FileResponse("Fotos/tienda.jpg")



@app.get("/facebook")
async def root():
    return FileResponse("Fotos/facebook.png")

@app.get("/instagram")
async def root():
    return FileResponse("Fotos/instagram.png")

@app.get("/tik-tok")
async def root():
    return FileResponse("Fotos/tik-tok.png")





@app.put("/celular")
async def root(item:celular.Celular):
    objetoPersona = celular.Celular(identificador = item.identificador, 
                                    marca=item.marca, modelo=item.modelo, color=item.color, precio = item.precio)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/celular")
async def root():
    objetoPersona = celular.Celular(identificador='',marca='',modelo='',color='',precio=0)
    return objetoPersona.seleccionatodoenBD()

@app.delete("/celular")
async def root(item:celular.Celular):
    print(item)
    objetoPersona = celular.Celular(identificador=  item.identificador,
                                    marca='',
                                    modelo='',
                                    color='',
                                    precio=0)
    objetoPersona.eliminaenBD()
    return objetoPersona.seleccionatodoenBD()


@app.get("/celularHTML")
async def root():
    return FileResponse("celular.html")





@app.put("/factura")
async def root(item:factura.Factura):
    objetoPersona = factura.Factura(identificador=item.identificador,fecha=item.fecha, comprador= item.comprador, montoTotal=item.montoTotal)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

@app.get("/factura")
async def root():
    objetoPersona = factura.Factura(identificador='',fecha='', comprador='',montoTotal=0)

    return objetoPersona.seleccionatodoenBD()

@app.put("/facturaCelular")
async def root(item:facturaCelular.Factura_Celular):
    objetoPersona = facturaCelular.Factura_Celular(identificadorFactura=item.identificadorFactura,identificadorCelular=item.identificadorCelular)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBDxFactura()

@app.get("/facturacelularxfactura")
async def root(item:facturaCelular.Factura_Celular):
    objetoPersona = facturaCelular.Factura_Celular(identificadorFactura=item.identificadorFactura,identificadorCelular='')
    return objetoPersona.seleccionatodoenBDxFactura()

@app.get("/facturaHTML")
async def root():
    return FileResponse("factura.html")







@app.delete("/celular")
async def root(item:celular.Celular):
    print(item)
    objetoPersona = celular.Celular(identificador='',marca='',modelo='',color='',precio=0)
    objetoPersona.eliminaenBD()
    return objetoPersona.seleccionatodoenBDxFactura()

@app.post("/celular")
async def root(item:celular.Celular):
    print(item)
    objetoPersona = celular.Celular(identificador = item.identificador, 
                                    marca=item.marca, modelo=item.modelo, color=item.color, precio = item.precio)
    objetoPersona.actualizaenBD()
    return objetoPersona.seleccionatodoenBDxFactura()


