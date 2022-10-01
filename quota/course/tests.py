from django.test import TestCase
from .models import ID, Course, Request

class CourseTsetCase(TestCase):

    def setUp(self):
        # create course id
        idcourse1 = ID.objects.create(code="CN201", coursename="OOP")
        idcourse2 = ID.objects.create(code="BBB", coursename="City B")

        Course.objects.create(
            subject=idcourse1, semester=1, year=2022, seat=2, coursestatus=1)

    def test_seat_available(self):
        """ is_seat_available should be True """

        course = Course.objects.first()

        self.assertTrue(course.is_seat_available())