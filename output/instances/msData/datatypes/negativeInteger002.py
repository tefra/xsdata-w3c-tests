from output.models.ms_data.datatypes.negative_integer_xsd.negative_integer import ComplexTest
from output.models.ms_data.datatypes.negative_integer_xsd.negative_integer import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1
    ),
    simple_test=-1
)
