import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail()
def test_not_succeed():
    assert False  # noqa: B011, PT015


@pytest.mark.skip()
def test_skipped():
    assert False  # noqa: B011, PT015
