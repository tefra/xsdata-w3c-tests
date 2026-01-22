from output.models.ms_data.datatypes.integer_xsd.integer import ComplexTest
from output.models.ms_data.datatypes.integer_xsd.integer import Root
from output.models.ms_data.datatypes.integer_xsd.integer import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=12345678901234567890123456789
    ),
    simple_test=SimpleTest(
        value=12345678901234567890123456789
    )
)
