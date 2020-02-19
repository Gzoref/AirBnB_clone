#!/usr/bin/python3
from models.state import State

from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    '''
    =========================
    User tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = State
        self.test_name = "State"

    def test_state_id(self):
        state = self.test_class()
        self.assertIsInstance(state.name, str)
