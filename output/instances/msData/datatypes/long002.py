from output.models.ms_data.datatypes.long_xsd.long import ComplexTest
from output.models.ms_data.datatypes.long_xsd.long import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-1
    ),
    simple_test=-1
)