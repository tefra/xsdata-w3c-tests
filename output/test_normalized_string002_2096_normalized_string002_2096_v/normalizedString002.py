from output.models.ms_data.datatypes.normalized_string_xsd.normalized_string import ComplexTest
from output.models.ms_data.datatypes.normalized_string_xsd.normalized_string import Root
from output.models.ms_data.datatypes.normalized_string_xsd.normalized_string import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='test line'
    ),
    simple_test=SimpleTest(
        value='test line'
    )
)
