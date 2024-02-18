from output.models.ms_data.datatypes.unsigned_long_xsd.unsigned_long import ComplexTest
from output.models.ms_data.datatypes.unsigned_long_xsd.unsigned_long import Root
from output.models.ms_data.datatypes.unsigned_long_xsd.unsigned_long import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=SimpleTest(
        value=0
    )
)
