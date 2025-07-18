import pytest


@pytest.fixture(name='anjing')
def login():
    print('\n登录操作')
    yield
    print('\n退出登录!')


class TestLogin:
    # 此处需要使用name重新定义的名称进行函数的调用，如果使用login调用的话，会报错。
    def test_01(self, anjing):
        print('\n---用例01---')

    def test_02(self):
        print('\n---用例02---')

    def test_03(self, anjing):
        print('\n---用例03---')


if __name__ == '__main__':
    pytest.main(['-vs'])
