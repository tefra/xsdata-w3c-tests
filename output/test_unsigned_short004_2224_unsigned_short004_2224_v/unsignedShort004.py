from output.models.ms_data.datatypes.unsigned_short_xsd.unsigned_short import ComplexTest
from output.models.ms_data.datatypes.unsigned_short_xsd.unsigned_short import Root
from output.models.ms_data.datatypes.unsigned_short_xsd.unsigned_short import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=1
    ),
    simple_test=SimpleTest(
        value=1
    )
)
