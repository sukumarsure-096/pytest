from library import is_even,is_pollin
#import library.is_even
# from text_unidecode import unidecode
import pytest
class TestLibrary():

    @pytest.mark.smoke      #this test is a brief test run like this pytest -vs -m smoke testing the critical test
    def test_even(self):
        print('Executing is even')
        assert is_even(10) == True

    def test_odd(self):
        print('Executing is odd')
        assert is_even(3) == False
    
    def test_string(self):
        print('executing string')
        with pytest.raises(TypeError):
            is_even('10')

    @pytest.mark.regression  #its take deep test --------------run like this in console pytest -vs -m regression
    def test_pollin_string(self):
        print('Executing is even')
        assert is_pollin('wow') == True

    def test_pollin_number(self):
        print('Executing is even')
        assert is_pollin(10) == True

class TestYantra():
    def test_yantra(self):
        print('testing the test_yanta')

class Testhai:
    def test_hai(self):
        print('testing hai')

class TestLogin:

    @pytest.mark.dependency()
    def test_login(self):
        print('login successfull')
        assert True

    @pytest.mark.dependency(depends = ["TestLogin::test_login"])
    def test_logout(self):
        print('logout success')
    
    



