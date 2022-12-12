import pytest
import holidays


with open('test/responses/search-default.json', 'r') as f:
    default = f.read()
with open('test/responses/search-parameters.json', 'r') as f:
    parameters = f.read()


def test_search_with_default_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/search?query=zucchini',
        text=default,
    )
    result = client.search('zucchini')
    assert requests_mock.called
    assert result['adult'] is False
    assert len(result['events']) == 3
    assert result['events'][0] == {
        'id': 'cc81cbd8730098456f85f69798cbc867',
        'name': 'National Zucchini Bread Day',
        'url': 'https://www.checkiday.com/cc81cbd8730098456f85f69798cbc867/national-zucchini-bread-day',
    }


def test_search_with_set_parameters(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/search?query=porch day&adult=true',
        text=parameters,
    )
    result = client.search('porch day', adult=True)
    assert requests_mock.called
    assert result['adult'] is True
    assert result['query'] == 'porch day'
    assert len(result['events']) == 1
    assert result['events'][0] == {
        'id': '61363236f06e4eb8e4e14e5925c2503d',
        'name': "Sneak Some Zucchini Onto Your Neighbor's Porch Day",
        'url': 'https://www.checkiday.com/61363236f06e4eb8e4e14e5925c2503d/sneak-some-zucchini-onto-your-neighbors-porch-day',
    }


def test_search_query_too_short(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/search?query=a',
        status_code=400,
        json={'error': 'Please enter a longer search term.'},
    )

    with pytest.raises(RuntimeError) as e:
        client.search('a')
    assert 'Please enter a longer search term.' == str(e.value)
    assert requests_mock.called


def test_search_too_many_results(requests_mock):
    client = holidays.client('abc123')
    requests_mock.get(
        'https://api.apilayer.com/checkiday/search?query=day',
        status_code=400,
        json={'error': 'Too many results returned. Please refine your query.'},
    )

    with pytest.raises(RuntimeError) as e:
        client.search('day')
    assert 'Too many results returned. Please refine your query.' == str(e.value)
    assert requests_mock.called


def test_search_missing_parameters():
    client = holidays.client('abc123')
    with pytest.raises(ValueError) as e:
        client.search(query=None)
    assert 'Search query is required.' == str(e.value)
