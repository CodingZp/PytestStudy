import pytest


# 作用域是整个pytest测试期间
@pytest.fixture(scope='session')
def fix_session():
    print('\n这是属于session')
    yield
    print('\nsession')


# 在每个测试类中都执行一次
@pytest.fixture(scope='class')
def fix_class():
    print('\n这是属于class')
    yield
    print('\nclass')


# 在每个测试模块（module）执行一次
@pytest.fixture(scope='module')
def fix_module():
    print('\n这是属于module')
    yield
    print('\nmodule')


# 在每个测试函数中都执行一次
@pytest.fixture(scope='function')
def fix_function():
    print('\n这是属于function')
    yield
    print('\nfunction')


class TestScope:
    def test_01(self, fix_function, fix_class, fix_module, fix_session):
        print('----用例01---')


if __name__ == '__main__':
    pytest.main(['-vs'])
