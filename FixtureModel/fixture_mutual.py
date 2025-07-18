import pytest


@pytest.fixture()
def login():
    print('\n登录操作')
    yield
    print('\n退出登录!')


# 直接将被调用fixture的函数名放到调用的fixture当做参数传入。
@pytest.fixture()
def log(login):
    print('打开日志功能！')
    yield
    print('\n关闭日志功能！')


class TestLogin:
    def test_01(self, log):
        print('\n需要用到登录！')

    def test_02(self):
        print('\n不需要登录！')

    def test_03(self, log):
        print('\n这里需要用到登录！')


if __name__ == '__main__':
    pytest.main(['-vs'])
