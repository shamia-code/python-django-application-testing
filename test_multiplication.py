
#We can generate details of the test execution in an xml file,
#this is useful when we have a dashboard that projects details of the test execution.

import pytest

@pytest.mark.parametrize("num, output",[(1,11), (2,22),(3,35),(4,44)])

def test_multiplication_11(num,output):
    
    assert 11*num == output 


#run this test using: pytest test_multiplication.py -v --junitxml="result.xml"
