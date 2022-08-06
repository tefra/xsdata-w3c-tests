from output.models.ms_data.datatypes.name_xsd.name import ComplexTest
from output.models.ms_data.datatypes.name_xsd.name import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="_foo"
    ),
    simple_test="_foo"
)
