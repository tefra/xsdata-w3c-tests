from output.models.ms_data.datatypes.language_xsd.language import ComplexTest
from output.models.ms_data.datatypes.language_xsd.language import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="en"
    ),
    simple_test="en"
)
