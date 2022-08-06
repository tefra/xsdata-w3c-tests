from output.models.ms_data.datatypes.unsigned_long_xsd.unsigned_long import ComplexTest
from output.models.ms_data.datatypes.unsigned_long_xsd.unsigned_long import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=1
    ),
    simple_test=1
)
