import pytest


@pytest.fixture(scope="class")
def _prepare_faces()-> any:
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def _very_important_fixture()->None:
    print(":)", "\n")


@pytest.fixture(autouse=True)
def _print_smiling_faces()->None:
    print(":-Р", "\n")  # noqa: RUF001


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, _prepare_faces, _very_important_fixture):
        pass

    def test_second_smiling_faces(self, _prepare_faces):
        pass
