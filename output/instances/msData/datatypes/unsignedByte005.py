from output.models.ms_data.datatypes.unsigned_byte_xsd.unsigned_byte import ComplexTest
from output.models.ms_data.datatypes.unsigned_byte_xsd.unsigned_byte import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=255
    ),
    simple_test=255
)
