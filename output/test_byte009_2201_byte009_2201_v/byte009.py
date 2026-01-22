from output.models.ms_data.datatypes.byte009_xsd.byte009 import ComplexTest
from output.models.ms_data.datatypes.byte009_xsd.byte009 import Root
from output.models.ms_data.datatypes.byte009_xsd.byte009 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            127,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            127,
        ]
    )
)
