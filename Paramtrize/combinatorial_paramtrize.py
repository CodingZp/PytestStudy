import pytest


class TestParamtrize:
    # 也可以使用多个pytest.mark.parametrize装饰器进行参数的组合，减少参数定义的次数
    @pytest.mark.parametrize("x", [1, 2])
    @pytest.mark.parametrize("y", [3, 4])
    def test_d(self, x, y):
        print("\n------------------> test_d has ran, and x={}, y={}".format(x, y))


if __name__ == '__main__':
    pytest.main(['-s', 'test_parametrize.py'])
