from output.models.ms_data.datatypes.any_uri011_xsd.any_uri011 import ComplexTest
from output.models.ms_data.datatypes.any_uri011_xsd.any_uri011 import Root
from output.models.ms_data.datatypes.any_uri011_xsd.any_uri011 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            'C:/TestSuites/XSD%20Spec/CR-xmlschema-2-20001024.htm#dc-minInclusive',
        ]
    ),
    simple_test=SimpleTest(
        value=[
            'C:/TestSuites/XSD%20Spec/CR-xmlschema-2-20001024.htm#dc-minInclusive',
        ]
    )
)
