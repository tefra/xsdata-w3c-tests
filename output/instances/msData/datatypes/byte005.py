from output.models.ms_data.datatypes.byte_xsd.byte import ComplexTest
from output.models.ms_data.datatypes.byte_xsd.byte import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=127
    ),
    simple_test=127
)
