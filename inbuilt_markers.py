from selenium import webdriver
import pytest


@pytest.fixture(autouse = True, scope='class')
def test_func():
    print('###########################################start project###########################################')
    yield
    print('###########################################end project###########################################')

class Tests():

    @pytest.mark.skip(reason = 'i am not interested to print stars ')
    def test_abc(self):
        for j in range(1,n+1):
            print('*'*j,end='\n')
    
class Testsif():

    @pytest.mark.skipif(3>4, reason = 'here condition is false so iam printing')
    def test_def(self):
        l= [j for j in range(1,10) if j%2 == 0]
        print(l)

    @pytest.mark.smoke
    def test_def1(self):
        for j in range(1,6):
            print(' *'*j,end='\n')

    @pytest.mark.regression
    def test_def2(self):
        for j in range(6,0,-1):
            print(' * '*j, end='\n')


class Testparam():

    @pytest.mark.parametrize('j',[3,6,9])
    def test_ghi(self,j):
        for n in range(1,j):
            print('j'*j)

    @pytest.mark.regression
    def test_def3(self):
        for j in range(6,0,-1):
            print(' * '*j, end='\n')


class Testx():
    @pytest.mark.xfail()
    def test_jkl(self):
        print('xfail test')    

    
##from selenium import webdriver
##
##@pytest.fixture(autouse = True , scope = 'class')
##def fixture(request):
##    d = webdriver.Chrome(executable_path=r'C:\Users\suren\Downloads\chromedriver_win32\chromedriver.exe')
##    request.cls.d = d
##    yield
##
##    d.quit()
##
##@pytest.mark.usefixtures('fixture')
##class TestD():
##    def test_web(self):
##        self.d.get('http://demowebshop.tricentis.com')
##
