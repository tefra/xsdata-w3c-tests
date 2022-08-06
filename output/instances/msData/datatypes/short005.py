from output.models.ms_data.datatypes.short_xsd.short import ComplexTest
from output.models.ms_data.datatypes.short_xsd.short import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=32767
    ),
    simple_test=32767
)
