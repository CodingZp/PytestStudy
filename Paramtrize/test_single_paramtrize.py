import pytest


class TestParamtrize:

    # 单个参数被赋予多个不同的值
    @pytest.mark.parametrize("a", [1, 2, 3])
    def test_a(self, a):
        # 此处的入参名称需要和pytest.mark.parametrize中定义的参数名称一致
        print('\n------------------> test_a has ran, and a = {}'.format(a))
        # assert 1 == a


if __name__ == '__main__':
    pytest.main(['-s', 'test_single_paramtrize.py'])
