# coding = utf-8
import pytest
from pythoncode.calc import calculator


@pytest.fixture(autouse=True, scope="function")
def start():
    print("开始计算")
    cal = calculator()
    yield
    print("完成计算")
