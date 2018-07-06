import allure, pytest


class Test_001:
    #添加测试步骤
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('登录')
    def test_01(self):
        allure.attach('描述','描述1')
        allure.attach('描述','描述2')
        allure.attach('描述','描述3')
        print('hello')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step('注册')
    def test_02(self):
        allure.attach('描述','1111')
        print('world')
        assert 1
