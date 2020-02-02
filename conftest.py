import pytest
from fixture.application import Application

@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    fixture.session.open_page()
    request.addfinalizer(fixture.destroy)
    return fixture