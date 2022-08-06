from output.models.ms_data.datatypes.non_positive_integer_xsd.non_positive_integer import ComplexTest
from output.models.ms_data.datatypes.non_positive_integer_xsd.non_positive_integer import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=0
)
