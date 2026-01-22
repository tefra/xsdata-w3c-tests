from output.models.ms_data.datatypes.int_xsd.int_mod import ComplexTest
from output.models.ms_data.datatypes.int_xsd.int_mod import Root
from output.models.ms_data.datatypes.int_xsd.int_mod import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1
    ),
    simple_test=SimpleTest(
        value=-1
    )
)
