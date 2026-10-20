from app import crear_app

print("Iniciando Agenda...")

app = crear_app()

print("Abriendo servidor...")

app.run(host="127.0.0.1", port=5000, debug=False)