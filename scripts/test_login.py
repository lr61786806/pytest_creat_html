import pytest
class TestLogin:
    @pytest.mark.run(order=1)
    def test_login(self):
        print('aa')
        assert False
    def setup(self):
        print('setup')
    def teardown(self):
        print('teardown')
    @pytest.mark.skipif(True,reason='跳过命令')
    def test_2(self):
        print('2')
        assert True
    # 执行顺序
    @pytest.mark.run(order=2)
    def test_3(self):
        print('3')
        assert True
    def test_4(self):
        print('4')
        assert True
    # 预期失败
    @pytest.mark.xfail(True,reason='')
    def test_5(self):
        print('5')
        assert True