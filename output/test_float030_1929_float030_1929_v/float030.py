from output.models.ms_data.datatypes.float_xsd.float_mod import ComplexTest
from output.models.ms_data.datatypes.float_xsd.float_mod import Root
from output.models.ms_data.datatypes.float_xsd.float_mod import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=2.3e-38
    ),
    simple_test=SimpleTest(
        value=2.3e-38
    )
)
