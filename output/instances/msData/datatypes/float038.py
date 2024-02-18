from output.models.ms_data.datatypes.float038_xsd.float038 import ComplexTest
from output.models.ms_data.datatypes.float038_xsd.float038 import Root
from output.models.ms_data.datatypes.float038_xsd.float038 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            1.2345,
        ]
    ),
    simple_test=SimpleTest(
        value=[
            1.23456,
        ]
    )
)
