import pytest


# 定义返回参数值的函数
def return_test_data():
    return [(1, 2), (2, 3), (3, 4)]


class TestParamtrize:

    # 使用预先定义好的函数的返回值作为入参，但是此处的函数返回值需要满足是元组式列表的格式
    @pytest.mark.parametrize("a,b", return_test_data())  # 使用函数返回值的方式传入参数值
    def test_c(self, a, b):
        print('\n------------------> test_c has ran, and a = {}, b = {}'.format(a, b))
        assert 1 == a and 2 == b


if __name__ == '__main__':
    pytest.main(['-s', 'test_parametrize.py'])
