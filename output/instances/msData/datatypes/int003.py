from output.models.ms_data.datatypes.int_xsd.int_mod import ComplexTest
from output.models.ms_data.datatypes.int_xsd.int_mod import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=0
)
