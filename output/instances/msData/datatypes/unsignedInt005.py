from output.models.ms_data.datatypes.unsigned_int_xsd.unsigned_int import ComplexTest
from output.models.ms_data.datatypes.unsigned_int_xsd.unsigned_int import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=4294967295
    ),
    simple_test=4294967295
)
