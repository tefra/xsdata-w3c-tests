from output.models.ms_data.datatypes.unsigned_short_xsd.unsigned_short import ComplexTest
from output.models.ms_data.datatypes.unsigned_short_xsd.unsigned_short import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=0
)
