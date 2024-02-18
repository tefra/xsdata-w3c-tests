from output.models.ms_data.datatypes.double_xsd.double import ComplexTest
from output.models.ms_data.datatypes.double_xsd.double import Root
from output.models.ms_data.datatypes.double_xsd.double import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0.0
    ),
    simple_test=SimpleTest(
        value=0.0
    )
)
