#!/usr/bin/python3
from models.review import Review

from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    '''
    =========================
    Review tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = Review
        self.test_name = "Review"

    def test_place_id(self):
        review = self.test_class()
        self.assertIsInstance(review.name, str)

    def test_user_id_review(self):
        review = self.test_class()
        self.assertIsInstance(review.name, str)

    def test_text(self):
        review = self.test_class()
        self.assertIsInstance(review.text, str)
