from output.models.ms_data.datatypes.unsigned_byte007_xsd.unsigned_byte007 import ComplexTest
from output.models.ms_data.datatypes.unsigned_byte007_xsd.unsigned_byte007 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            254,
        ]
    ),
    simple_test=[
        254,
    ]
)
