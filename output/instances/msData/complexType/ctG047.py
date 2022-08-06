from output.models.ms_data.complex_type.ct_g047_xsd.ct_g047 import Root


obj = Root(
    my_element1="test data",
    my_element2=None,
    my_element3=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG047.xsd",
        "{http://tempuri.org/xmlschema}myAttr": "test attribute",
    },
    other_attributes={}
)
