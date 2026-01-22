from output.models.ms_data.datatypes.byte_xsd.byte import ComplexTest
from output.models.ms_data.datatypes.byte_xsd.byte import Root
from output.models.ms_data.datatypes.byte_xsd.byte import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-128
    ),
    simple_test=SimpleTest(
        value=-128
    )
)
