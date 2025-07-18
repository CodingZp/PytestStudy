import pytest


class TestLogin:
    # def test_01(self, sub_my_fixture):
    #     print('需要用到登录！')
    #     assert False
    # def test_02(self):
    #     print('不需要登录！')

    # 只要将fixture放在参数中，那么这个方法就会自动调用fixture, 不管这条测试用例是否可以通过
    # test_module.py
    # def test_1(self, session_fixture, module_fixture, function_fixture):
    #     print("运行测试 test_1")
    #     assert session_fixture == "session_data"
    #
    # def test_2(self, session_fixture, module_fixture):
    #     print("运行测试 test_2")
    #     # 未显式调用 function_fixture，因此不会触发其 setup/teardown
    def test_2(self, session_fixture):
        print("\n运行测试 test_2")

    def test_1(self):
        print("\n运行测试 test_1")
    #
    # def test_2(self, class_fixture):
    #     print("\n运行测试 test_2")
