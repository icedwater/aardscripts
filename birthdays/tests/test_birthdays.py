import birthdays

def test_retrieve_dates_no_line():
    """
    Return empty list if the database returns an empty response.
    """
    dates = birthdays.retrieve_dates()
    assert dates == []

def test_retrieve_dates_one_line():
    assert False

def test_retrieve_dates_multi_line():
    assert False

