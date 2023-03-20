import pytest

from sandbox import sandbox_function, is_even_number

def test_sandbox_function():
    assert 5 == sandbox_function()


@pytest.mark.parametrize(
    'argument, expected_result, expected_exception',
    [
        (1, False, None),
        (2, True, None),
        (5, False, None),
        (2.3, False, ValueError),
    ]
)
def test_sandbox(
    argument,
    expected_result,
    expected_exception
):
    if expected_exception:
        with pytest.raises(ValueError):
            is_even_number(argument)
    else:
        is_even_number(argument) ==  expected_result

