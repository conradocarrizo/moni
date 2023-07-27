import pytest
from unittest.mock import patch
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
@patch("services.moni.moni_client.MoniClient.get_pre_score")
def test_check_pre_score(monkeypatch, dni, expected_status, moni_client):
    def mock_get_pre_score(dni):
        return {"status": "approve", "has_error": False}

    monkeypatch.setattr(moni_client, "get_pre_score", mock_get_pre_score)

    if expected_status:
        assert moni_client.check_pre_score(dni)
    else:
        with pytest.raises(APIValidationError):
            moni_client.check_pre_score(dni)
