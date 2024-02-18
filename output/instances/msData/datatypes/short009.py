from output.models.ms_data.datatypes.short009_xsd.short009 import ComplexTest
from output.models.ms_data.datatypes.short009_xsd.short009 import Root
from output.models.ms_data.datatypes.short009_xsd.short009 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            -32765,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            -32765,
        ]
    )
)
