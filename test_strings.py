from strings_utils import uppercase_list

def test_uppercase_list():
    result = uppercase_list("smogtether")
    assert result == list("SMOGTETHER")
