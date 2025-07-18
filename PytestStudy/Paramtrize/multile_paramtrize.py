import pytest


class TestParamtrize:

    # 多个参数被赋予多个不同的值的组合
    @pytest.mark.parametrize("a,b", [(1, 2), (2, 3), (3, 4)])
    def test_b(self, a, b):
        print('\n------------------> test_b has ran, and a = {}, b = {}'.format(a, b))
        assert 1 == a and 2 == b


if __name__ == '__main__':
    pytest.main(['-s', 'test_parametrize.py'])
