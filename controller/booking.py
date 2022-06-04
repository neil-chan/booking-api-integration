from utils.common_imports import *
from utils.base_api import *
from utils.config import *
from utils.conftest import *
from util import *


class Booking(Base):
    def __init__(self):
        Base.__init__(self)
        self.booking_url = APP_URL + "/booking"

    def get_all_bookings(self):
        LOG.info("get all bookings")
        response = SESSION.get(self.booking_url)

        return response

    def get_booking(self, id):
        LOG.info("get booking details for %s", id)
        response = SESSION.get(self.booking_url + '/' + str(id))

        return response

    # def create_booking(self, firstname, lastname, checkindate, checkoutdate, totalprice=None, depositpaid=None,
    #                    additionalneeds=None):
    #     LOG.info('creating new booking')
    #     payload = build_request_payload(firstname, lastname, checkindate, checkoutdate, totalprice, depositpaid,
    #                                     additionalneeds)
    #     access_token = generateToken()
    #     header = build_request_headers(access_token)
    #     response = SESSION.post(self.booking_url, json=payload, )
    #
    #     return response
