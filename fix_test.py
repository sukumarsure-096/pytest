import pytest

# @pytest.fixture(autouse = True,scope= 'class') 
# def func():
#     print('in func')


# class TestEx:
#     def test_f1(self):
#         print('in f1')


#     def test_f2(self):
#         print('in f2')

@pytest.fixture(autouse = True) 
def func():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@in func')
    yield
    print('in teardown@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


class TestEx:
    def test_f1(self):
        print('in f1')


    def test_f2(self):
        print('in f2')

# class TestEx1:
#     def test_f3(self):
#         print('in f1')


#     def test_f4(self):
#         print('in f2')


# @pytest.fixture(autouse = True,scope= 'module')  #this created fixture
# def func(request):
#     print('in func')
#     def teardown():
#         print('in teardown')
#     request.addfinalizer(teardown)

# @pytest.mark.usefixture(func)
# class TestEx:
#     def test_f1(self):
#         print('in f1')


    def test_f2(self):
        print('in f2')

class TestEx1:
    def test_f3(self):
        print('in f1')


    def test_f4(self):
        print('in f2')


