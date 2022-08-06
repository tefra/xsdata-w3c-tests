from output.models.ms_data.datatypes.float_xsd.float_mod import ComplexTest
from output.models.ms_data.datatypes.float_xsd.float_mod import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-3.14159
    ),
    simple_test=-3.14159
)
