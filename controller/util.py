from utils.common_imports import *


def validate_date(date_text):

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def build_request_payload(firstname, lastname, checkindate, checkoutdate,
                          totalprice=None, depositpaid=None , additionalneeds=None):
            LOG.info('building request payload')
            validate_date(checkindate)
            validate_date(checkoutdate)
            payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates":
                {"checkin": checkindate,
                 "checkout": checkoutdate},
            "additionalneeds": additionalneeds}

            LOG.debug(f"Request payload: {payload}")

            return payload



def build_request_headers(access_token):
    LOG.info("build_request_headers")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "accept": accept_type
    }
    LOG.debug(f"Request headers: {headers}")

    return headers
