from output.models.ms_data.datatypes.short_xsd.short import ComplexTest
from output.models.ms_data.datatypes.short_xsd.short import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=-32768
    ),
    simple_test=-32768
)
