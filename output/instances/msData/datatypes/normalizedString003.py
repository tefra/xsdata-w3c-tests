from output.models.ms_data.datatypes.normalized_string_xsd.normalized_string import ComplexTest
from output.models.ms_data.datatypes.normalized_string_xsd.normalized_string import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="test&#10;line"
    ),
    simple_test="test&#10;line"
)