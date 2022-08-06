from output.models.ms_data.datatypes.string_xsd.string import ComplexTest
from output.models.ms_data.datatypes.string_xsd.string import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="a_?&gt;"
    ),
    simple_test="a_?&gt;"
)
