from playwright.sync_api import APIRequestContext, expect

# Test para comprobar el funcionamiento de la API 
def test_api_locations(api_request_context: APIRequestContext):
    url = "http://127.0.0.1:8000/ubicaciones/"

    response = api_request_context.get(url)
    expect(response).to_be_ok()