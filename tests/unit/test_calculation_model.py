import pytest
import uuid
from app.models.calculation import Addition, Subtraction, Multiplication, Division, LCM, AbstractCalculation

# --- Addition ---
def test_addition_inputs_not_list():
    calc = Addition(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "Inputs must be a list" in str(exc.value)

def test_addition_inputs_too_short():
    calc = Addition(user_id=uuid.uuid4(), inputs=[5])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "at least two numbers" in str(exc.value)

# --- Subtraction ---
def test_subtraction_inputs_not_list():
    calc = Subtraction(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_subtraction_inputs_too_short():
    calc = Subtraction(user_id=uuid.uuid4(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

# --- Multiplication ---
def test_multiplication_inputs_not_list():
    calc = Multiplication(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_multiplication_inputs_too_short():
    calc = Multiplication(user_id=uuid.uuid4(), inputs=[2])
    with pytest.raises(ValueError):
        calc.get_result()

# --- Division ---
def test_division_by_zero():
    calc = Division(user_id=uuid.uuid4(), inputs=[10, 0])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "Cannot divide by zero" in str(exc.value)

# --- AbstractCalculation factory ---
def test_create_invalid_type():
    with pytest.raises(ValueError) as exc:
        AbstractCalculation.create("invalidtype", uuid.uuid4(), [1, 2])
    assert "Unsupported calculation type" in str(exc.value)

# --- LCM ---
def test_lcm_valid_basic():
    calc = LCM(user_id=uuid.uuid4(), inputs=[4, 6])
    assert calc.get_result() == 12

def test_lcm_valid_primes():
    calc = LCM(user_id=uuid.uuid4(), inputs=[5, 7])
    assert calc.get_result() == 35

def test_lcm_valid_same_number():
    calc = LCM(user_id=uuid.uuid4(), inputs=[9, 9])
    assert calc.get_result() == 9

def test_lcm_inputs_not_list():
    calc = LCM(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "Inputs must be a list" in str(exc.value)

def test_lcm_inputs_too_short():
    calc = LCM(user_id=uuid.uuid4(), inputs=[5])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "LCM requires exactly two numbers" in str(exc.value)

def test_lcm_invalid_non_integer_float():
    calc = LCM(user_id=uuid.uuid4(), inputs=[4.5, 6])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "positive integers" in str(exc.value)

def test_lcm_invalid_negative():
    calc = LCM(user_id=uuid.uuid4(), inputs=[-4, 6])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "positive integers" in str(exc.value)

def test_lcm_invalid_zero():
    calc = LCM(user_id=uuid.uuid4(), inputs=[0, 6])
    with pytest.raises(ValueError) as exc:
        calc.get_result()
    assert "positive integers" in str(exc.value)

# --- AbstractCalculation factory for LCM ---
def test_create_lcm_type():
    calc = AbstractCalculation.create("lcm", uuid.uuid4(), [4, 6])
    assert isinstance(calc, LCM)
    assert calc.get_result() == 12