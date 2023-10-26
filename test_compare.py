#xfail and skip is used in situations where a test is not relevant for some time due to some reasons.
#Or when a new feature is being implemented and we already added a test for that feature 
#Later when the test becomes relevant, we can remove the markers

import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num =  100
    assert num >= 100 

@pytest.mark.skip
@pytest.mark.others
def test_less():
    num =100
    assert num < 200

#execute this test using: pytest test_compare.py -v 
