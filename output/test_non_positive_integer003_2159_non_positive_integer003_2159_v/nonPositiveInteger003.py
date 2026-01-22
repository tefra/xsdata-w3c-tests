from output.models.ms_data.datatypes.non_positive_integer_xsd.non_positive_integer import ComplexTest
from output.models.ms_data.datatypes.non_positive_integer_xsd.non_positive_integer import Root
from output.models.ms_data.datatypes.non_positive_integer_xsd.non_positive_integer import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=SimpleTest(
        value=0
    )
)
