from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="http://www.w3.org/XML/Group/xmlschema-current/datatypes/datatypes.html#uriReference"
    ),
    simple_test="http://www.w3.org/XML/Group/xmlschema-current/datatypes/datatypes.html#uriReference"
)