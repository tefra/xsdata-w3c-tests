from output.models.ms_data.datatypes.long_xsd.long import ComplexTest
from output.models.ms_data.datatypes.long_xsd.long import Root
from output.models.ms_data.datatypes.long_xsd.long import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=9223372036854775807
    ),
    simple_test=SimpleTest(
        value=9223372036854775807
    )
)
