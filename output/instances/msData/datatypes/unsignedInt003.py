from output.models.ms_data.datatypes.unsigned_int_xsd.unsigned_int import ComplexTest
from output.models.ms_data.datatypes.unsigned_int_xsd.unsigned_int import Root
from output.models.ms_data.datatypes.unsigned_int_xsd.unsigned_int import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=SimpleTest(
        value=0
    )
)
