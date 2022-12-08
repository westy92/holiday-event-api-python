import holidays
import pytest


message = """\
Please provide a valid API key. \
Get one at https://apilayer.com/marketplace/checkiday-api#pricing.\
"""


def test_constructor_missing_api_key():
    with pytest.raises(ValueError) as e:
        holidays.client(None)
    assert message == str(e.value)


def test_constructor_blank_api_key():
    with pytest.raises(ValueError) as e:
        holidays.client('')
    assert message == str(e.value)


def test_constructor_success():
    result = holidays.client('apikey')
    assert result is not None
