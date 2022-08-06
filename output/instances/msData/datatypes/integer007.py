from output.models.ms_data.datatypes.integer_xsd.integer import ComplexTest
from output.models.ms_data.datatypes.integer_xsd.integer import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1
    ),
    simple_test=-1
)
