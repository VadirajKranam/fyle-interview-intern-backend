from core.libs.exceptions import FyleError

def test_exception_1():
    test_error=FyleError(404,'Not found error')
    res=test_error.to_dict()
    assert res['message']=='Not found error'
    assert test_error.status_code==404