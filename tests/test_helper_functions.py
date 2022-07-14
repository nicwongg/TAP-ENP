import helper_functions


def test_valid_url():
    assert helper_functions.valid_url('') == False
    assert helper_functions.valid_url('google.com') == False
    assert helper_functions.valid_url('notalink') == False
    assert helper_functions.valid_url('htp://www.google.com') == False
    assert helper_functions.valid_url('www.google.com') == False
    assert helper_functions.valid_url('http://www.google.com') == True
    assert helper_functions.valid_url('https://www.google.com') == True


def test_valid_alias():
    assert helper_functions.valid_alias('') == False
    assert helper_functions.valid_alias('!!!') == False
    assert helper_functions.valid_alias('sp3c!@lch@rsN0TA!!lowed') == False
    assert helper_functions.valid_alias('asdklajsd@asd') == False
    assert helper_functions.valid_alias('thishastobemorethan16chars') == False
    assert helper_functions.valid_alias('h3ll0') == True
