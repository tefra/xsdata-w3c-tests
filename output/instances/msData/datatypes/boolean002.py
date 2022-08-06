from output.models.ms_data.datatypes.boolean_xsd.boolean import ComplexTest
from output.models.ms_data.datatypes.boolean_xsd.boolean import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=True
    ),
    simple_test=True
)
