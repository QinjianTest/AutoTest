import pytest

#判断xx为真
#1、定义方法进行assert
def test_1():
    a = True
    assert a

#判断XX不为真
def test_2():
    a= True
    assert not a

#判断b包含a
def test_3():
    a="hello"
    b="hello world"
    assert a in b
#判断a==b
def test_4():
    a=b="hello"
    assert a ==b

#判断a!=b
def test_5():
    a="hello"
    b="hello world"
    assert a !=b

#2、运行查看结果
if __name__ == "__main__":
    pytest.main(["pytest_assert.py"])



