import pytest


# 定义返回参数值的函数
def return_test_data():
    return [(1, 2), (2, 3), (3, 4)]


test_user_data = ['Tom', 'Jerry']


# 方法名作为参数
@pytest.fixture(scope='module')
def login_r(request):
    user = request.param  # 通过 request.param 获取测试参数
    print(f" 登录用户： {user}")
    return user


class TestParamtrize:

    @pytest.mark.parametrize("login_r", test_user_data, indirect=True)
    def test_login(self, login_r):
        a = login_r
        print(f"测试用例中 login_r 函数 的返回值； {a}")
        assert a != ""


if __name__ == '__main__':
    pytest.main(['-s', 'test_parametrize.py'])
