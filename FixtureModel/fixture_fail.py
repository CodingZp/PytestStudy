import pytest


@pytest.fixture()
def login():
    # yield之前的是前置操作
    print('\n登录操作')
    assert False, "登录失败！"  # 这里故意失败
    yield
    # yield之后的是后置操作 不管用例是否执行通过，都会执行后置操作
    print('\n退出登录')


class TestLogin:
    def test_01(self, login):
        print('需要用到登录！')
        assert 1 == 1



if __name__ == '__main__':
    pytest.main(['-vs', "--setuo-show", "fixture_fail.py"])
