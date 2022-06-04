from utils.common_imports import *
from utils.base_api import *
from utils.config import *
from controller.auth import *


@pytest.fixture(scope="session")
def generateToken():
    LOG.info("Generate Token")
    response = Auth.createToken()
    assert response.status_code == 200

    token = response.json["token"]
    yield token
