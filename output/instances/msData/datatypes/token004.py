from output.models.ms_data.datatypes.token_xsd.token import ComplexTest
from output.models.ms_data.datatypes.token_xsd.token import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="a&#10;b"
    ),
    simple_test="a&#10;b"
)