# pylint: disable=C0114, C0115, C0116, W0105, W0401
import pytest
# from the gadget.py file, get the function `gadget_cost`
from gadget import gadget_cost 

def test_gadget_cost_small() -> None:
    assert gadget_cost(1, "hi") == pytest.approx(0.6)

def test_gadget_cost_medium() -> None:
    assert gadget_cost(10, "tech") == pytest.approx(7)
    # Intentionally defined incorrectly to view a failing test