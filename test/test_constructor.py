import holidays
import pytest

def test_constructor_missing_api_key():
    with pytest.raises(ValueError) as e:
        holidays.client(None)
    assert 'Please provide a valid API key. Get one at https://apilayer.com/marketplace/checkiday-api#pricing.' == str(e.value)

def test_constructor_blank_api_key():
    with pytest.raises(ValueError) as e:
        holidays.client('')
    assert 'Please provide a valid API key. Get one at https://apilayer.com/marketplace/checkiday-api#pricing.' == str(e.value)

def test_constructor_success():
    result = holidays.client('apikey')
    assert result != None
