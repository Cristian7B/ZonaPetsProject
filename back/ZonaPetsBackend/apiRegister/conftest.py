import pytest
from playwright.sync_api import APIRequestContext, sync_playwright

@pytest.fixture
def api_request_context():
    with sync_playwright() as p:
        request_context: APIRequestContext = p.request.new_context(base_url="http://127.0.0.1:8000")
        yield request_context
        request_context.dispose()
