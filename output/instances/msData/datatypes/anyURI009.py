from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo='file:///C:/TestSuites/XSD%20Spec/CR-xmlschema-2-20001024.htm#dc-minInclusive'
    ),
    simple_test='file:///C:/TestSuites/XSD%20Spec/CR-xmlschema-2-20001024.htm#dc-minInclusive'
)
