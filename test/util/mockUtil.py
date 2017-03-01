from mock import create_autospec


def create_mock(some_class):
    return create_autospec(some_class, spec_set=True)
