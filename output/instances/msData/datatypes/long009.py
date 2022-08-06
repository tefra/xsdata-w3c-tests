from output.models.ms_data.datatypes.long009_xsd.long009 import ComplexTest
from output.models.ms_data.datatypes.long009_xsd.long009 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            9223372036854775,
        ]
    ),
    simple_test=[
        9223372036854775,
    ]
)
