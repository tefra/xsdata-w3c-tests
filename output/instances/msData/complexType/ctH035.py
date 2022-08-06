from output.models.ms_data.complex_type.ct_h035_xsd.ct_h035 import Root


obj = Root(
    my_element1=None,
    my_element2="test data",
    my_element3=None,
    local_attributes={
        "local": "local attribute",
    },
    my_element4="test data",
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctH035.xsd",
        "{http://tempuri.org/xmlschema}myAttr": "next attribute",
    }
)
