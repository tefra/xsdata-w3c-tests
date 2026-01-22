from output.models.ms_data.datatypes.integer_xsd.integer import ComplexTest
from output.models.ms_data.datatypes.integer_xsd.integer import Root
from output.models.ms_data.datatypes.integer_xsd.integer import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=SimpleTest(
        value=0
    )
)
