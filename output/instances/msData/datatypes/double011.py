from output.models.ms_data.datatypes.double_xsd.double import ComplexTest
from output.models.ms_data.datatypes.double_xsd.double import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1.0
    ),
    simple_test=-1.0
)
