from playwright.sync_api import APIRequestContext, expect


# -------------------------------------------------------------------------------
# Test para el endpoint de usuario

# Test para comprobar el funcionamiento de la API frente a datos correctos
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


# Test para comprobar el funcionamiento de la API frente a datos incorrectos
# En este caso, se envía un tipo de negocio incorrecto
def testApiDatabaseBadData(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/"

    data = {
        "nombre_compañia": "", # Vacio
        "telefono_usuario": "123450",
        "tipo_de_negocio": "Tipo erroneo",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).not_to_be_ok()

# En este caso se envía un tipo de negocio correcto, pero el nombre de la compañía está vacío
def testApiDatabaseBadData2(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/"

    data = {
        "nombre_compañia": "", #Vacío
        "telefono_usuario": "123450",
        "tipo_de_negocio": "Restaurantes",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).not_to_be_ok()

# En este caso se envía una latitud y longitud incorrectas
def testApiDatabaseBadData3(api_request_context: APIRequestContext):
   url = "http://127.0.0.1:8000/procesar/"

   data = {
        "nombre_compañia": "Compañia Ejemplo",
        "telefono_usuario": "123450",
        "tipo_de_negocio": "Hoteles",
        "latitud": "",
        "longitud": "",
    }
   
   response = api_request_context.post(url, data=data)
   expect(response).not_to_be_ok()



# -------------------------------------------------------------------------------
# Test para el endpoint empresarial

# Test para comprobar el funcionamiento de la API empresarial con datos correctos
def test_api_database_post_register_empresarial(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/empresa/"

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


# Test para comprobar el funcionamiento de la API empresarial frente a datos incorrectos
# En este caso, se envía un correo electrónico vacío
def testEmpresarialBadData(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/empresa/"

    data = {
        "nombre_de_quien_registra": "Juan Pérez",
        "telefono_usuario": "1234567890",
        "correo_electronico": "",
        "tipo_de_negocio": "Hoteles",
        "nombre_compañia": "Compañía Ejemplo",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).not_to_be_ok()


# Test para comprobar el funcionamiento de la API empresarial con un tipo de negocio incorrecto
def testEmpresarialBadData2(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/empresa/"

    data = {
        "nombre_de_quien_registra": "Juan Pérez",
        "telefono_usuario": "1234567890",
        "correo_electronico": "juan.perez@example.com",
        "tipo_de_negocio": "Tipo inválido",
        "nombre_compañia": "Compañía Ejemplo",
        "latitud": "19.432608",
        "longitud": "-99.133209",
    }

    response = api_request_context.post(url, data=data)
    expect(response).not_to_be_ok()


# Test para comprobar el funcionamiento de la API empresarial con coordenadas inválidas
def testEmpresarialBadData3(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/procesar/empresa/"

    data = {
        "nombre_de_quien_registra": "Juan Pérez",
        "telefono_usuario": "1234567890",
        "correo_electronico": "juan.perez@example.com",
        "tipo_de_negocio": "Hoteles",
        "nombre_compañia": "Compañía Ejemplo",
        "latitud": "",
        "longitud": "",
    }

    response = api_request_context.post(url, data=data)
    expect(response).not_to_be_ok()

