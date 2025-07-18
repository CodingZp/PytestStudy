import pytest


@pytest.fixture()
def login():
    print('登录操作')
    yield
    print('退出登录!')


@pytest.fixture()
def log():
    print('打开日志功能！')
    yield
    print('关闭日志功能！')


class TestLogin:
    def test_01(self):
        print('\n需要用到登录！')



if __name__ == '__main__':
    pytest.main(['-vs', "--setuo-show", "test_multiple_fixture.py"])
