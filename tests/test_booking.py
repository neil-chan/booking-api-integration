from utils.common_imports import *
from controller.booking import *


class TestBooking:
    def test_get_booking_IDs(self):
        LOG.info('Test Get All Bookings')
        response = Booking().get_all_bookings()

        assert response.ok
