import web

urls = (
    '/', 'mvc.controllers.hello.Index', 
    '/ver', 'mvc.controllers.hello.Ver',
    '/borrar', 'mvc.controllers.hello.Borrar',
    '/actualizar', 'mvc.controllers.hello.Actualizar',
    '/insertar', 'mvc.controllers.hello.Insertar',
    '/calculadora', 'mvc.controllers.calculadora.CalculadoraControlador'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug= False
    app.run()