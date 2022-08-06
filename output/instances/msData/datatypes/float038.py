from output.models.ms_data.datatypes.float038_xsd.float038 import ComplexTest
from output.models.ms_data.datatypes.float038_xsd.float038 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            1.2345,
        ]
    ),
    simple_test=[
        1.23456,
    ]
)
