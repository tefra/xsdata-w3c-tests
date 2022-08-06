from output.models.ms_data.datatypes.unsigned_short007_xsd.unsigned_short007 import ComplexTest
from output.models.ms_data.datatypes.unsigned_short007_xsd.unsigned_short007 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            65530,
        ]
    ),
    simple_test=[
        65530,
    ]
)
