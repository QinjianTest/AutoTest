import pytest
import allure
#测试方法
@allure.feature("接口测试，这是一个一级标签")
class TestAllure:
    @allure.title("测试用例标题1")
    @allure.description("执行测试用例1的结果是test1")
    @allure.story("这是一个二级标签：test1")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        print("test1")

    @allure.title("测试用例标题2")
    @allure.description("执行测试用例1的结果是test2")
    @allure.story("这是一个二级标签：test1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test2")

    @allure.title("测试用例标题3")
    @allure.description("执行测试用例1的结果是test3")
    @allure.story("这是一个二级标签：test3")
    def test_3(self):
        print("test3")

    @pytest.mark.parametrize("case",["case1","case2"])
    def test_4(self,case):
        print(case)
        allure.dynamic.title(case)

if __name__ == '__main__':
    pytest.main(["allure_demo.py"])
