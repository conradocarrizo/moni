import pytest
from services.moni.moni_client import (
    MoniClient,
    APIValidationError,
)


@pytest.fixture
def moni_client():
    return MoniClient()


@pytest.mark.parametrize(
    "dni, expected_status",
    [
        ("12345678", True),
        ("87654321", True),
        ("abc12345", False),
    ],
)
def test_check_pre_score(monkeypatch, dni, expected_status, moni_client):
    def mock_get_pre_score(dni):
        return {"status": "approve", "has_error": False}

    def mock_is_not_config():
        return True

    monkeypatch.setattr(moni_client, "get_pre_score", mock_get_pre_score)
    monkeypatch.setattr(moni_client, "is_not_config", mock_is_not_config)

    if expected_status:
        assert moni_client.check_pre_score(dni)
    else:
        with pytest.raises(APIValidationError):
            moni_client.check_pre_score(dni)
