from output.models.ms_data.datatypes.token_xsd.token import ComplexTest
from output.models.ms_data.datatypes.token_xsd.token import Root
from output.models.ms_data.datatypes.token_xsd.token import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=''
    ),
    simple_test=SimpleTest(

    )
)
