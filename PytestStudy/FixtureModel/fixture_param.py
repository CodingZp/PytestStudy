import pytest


@pytest.fixture()
def login(request):
    user = request.param
    print(f'登录操作: {user}')
    assert user == "Jerry"
    yield user
    print(f'退出登录: {user}')


class TestLogin:
    # 通过将参数传递给 fixture，实现参数化
    @pytest.mark.parametrize("login", ["Tom", "Jerry"], indirect=True)
    def test_login_user(self, login):
        assert login in ["Tom", "Jerry"]
        print(f"\n当前登录用户是：{login}")


if __name__ == '__main__':
    pytest.main(['-vs', "--setuo-show", "fixture_param.py"])

