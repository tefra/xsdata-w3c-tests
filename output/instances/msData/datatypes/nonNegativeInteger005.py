from output.models.ms_data.datatypes.non_negative_integer_xsd.non_negative_integer import ComplexTest
from output.models.ms_data.datatypes.non_negative_integer_xsd.non_negative_integer import Root
from output.models.ms_data.datatypes.non_negative_integer_xsd.non_negative_integer import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=12345678901234567890123456789
    ),
    simple_test=SimpleTest(
        value=12345678901234567890123456789
    )
)
