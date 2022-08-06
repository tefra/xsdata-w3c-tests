from output.models.ms_data.datatypes.positive_integer_xsd.positive_integer import ComplexTest
from output.models.ms_data.datatypes.positive_integer_xsd.positive_integer import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=1
    ),
    simple_test=1
)
