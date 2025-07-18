import pytest


@pytest.fixture(autouse=True)
def login():
    print('\n登录操作')
    yield
    print('\n退出登录!')


class TestLogin:
    def test_01(self):
        print('---用例01---')


if __name__ == '__main__':
    pytest.main(['-vs'])
