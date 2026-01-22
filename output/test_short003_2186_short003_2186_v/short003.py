from output.models.ms_data.datatypes.short_xsd.short import ComplexTest
from output.models.ms_data.datatypes.short_xsd.short import Root
from output.models.ms_data.datatypes.short_xsd.short import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=0
    ),
    simple_test=SimpleTest(
        value=0
    )
)
