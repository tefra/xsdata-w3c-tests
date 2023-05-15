from output.models.ms_data.complex_type.ct_g069_xsd.ct_g069 import Root


obj = Root(
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG069.xsd",
        "myAttr": "last attribute",
    },
    my_attr1="test attribute"
)
