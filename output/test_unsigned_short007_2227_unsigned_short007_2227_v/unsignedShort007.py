from output.models.ms_data.datatypes.unsigned_short007_xsd.unsigned_short007 import ComplexTest
from output.models.ms_data.datatypes.unsigned_short007_xsd.unsigned_short007 import Root
from output.models.ms_data.datatypes.unsigned_short007_xsd.unsigned_short007 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            65530,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            65530,
        ]
    )
)
