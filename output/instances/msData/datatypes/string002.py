from output.models.ms_data.datatypes.string_xsd.string import ComplexTest
from output.models.ms_data.datatypes.string_xsd.string import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='a_?>'
    ),
    simple_test='a_?>'
)
