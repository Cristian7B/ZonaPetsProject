from playwright.sync_api import APIRequestContext, expect

# Test para comprobar el funcionamiento de la API 
def test_api_register(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/registrar/"
    data = {
        "nombre_compañia": "Compañia Ejemplo",
        "telefono_usuario": "123450",
        "tipo_de_negocio": "Hoteles",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).to_be_ok()

def test_api_register_empresa(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/registrar/empresa/"

    data = {
        "nombre_de_quien_registra": "Juan Pérez",
        "telefono_usuario": "12312",
        "correo_electronico": "juan.perez@example.com",
        "tipo_de_negocio": "Hoteles",
        "nombre_compañia": "Compañía Ejemplo",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).to_be_ok()