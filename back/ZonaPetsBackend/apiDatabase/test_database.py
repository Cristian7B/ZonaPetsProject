from playwright.sync_api import APIRequestContext, expect

def test_api_database_post_register(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/"

    data = {
        "nombre_compañia": "Compañia Ejemplo",
        "telefono_usuario": "123450",
        "tipo_de_negocio": "Hoteles",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).to_be_ok()

