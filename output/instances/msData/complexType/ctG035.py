from output.models.ms_data.complex_type.ct_g035_xsd.ct_g035 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG035.xsd",
        "{http://tempuri.org/xmlschema}myAttr": "test attribute",
    },
    other_attributes={}
)
