from utils.base_api import *
from utils.config import *


class Auth(Base):
    def __init__(self):
        Base.__init__(self)
        self.auth_url = APP_URL + "/auth"

    def createToken(self):
        LOG.info("Create Admin Token")
        res = self.send_request(
            Base.RequestMethod.POST,
            custom_url=self.auth_url,
            payload={"username": ADMIN_USER, "password": ADMIN_PASSWORD},
            headers={"Content-Type": "application/x-www-form-urlencoded",
                           "accept": "application/json"}
        )
        return res
