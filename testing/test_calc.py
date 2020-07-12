# coding = utf-8
import pytest
from pythoncode.calc import calculator
import yaml

with open("../data/datas.yml") as fr:
    data = yaml.safe_load(fr)
add_mydatas = list(data["add"].values())
add_myids = list(data["add"].keys())
sub_mydatas = list(data["sub"].values())
sub_myids = list(data["sub"].keys())
mul_mydatas = list(data["mul"].values())
mul_myids = list(data["mul"].keys())
div_mydatas = list(data["div"].values())
div_myids = list(data["div"].keys())


class Testcalculator:
    def setup_class(self):
        self.cal = calculator()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize(("a, b, result"), add_mydatas, ids=add_myids)
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize(("a, b, result"), sub_mydatas, ids=sub_myids)
    def test_sub(self, a, b, result):
        assert result == self.cal.sub(a, b)

    @pytest.mark.parametrize(("a, b, result"), mul_mydatas, ids=mul_myids)
    def test_mul(self, a, b, result):
        assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize(("a, b, result"), div_mydatas, ids=div_myids)
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)