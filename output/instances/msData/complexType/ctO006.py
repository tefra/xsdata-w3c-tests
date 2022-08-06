from output.models.ms_data.complex_type.ct_o006_xsd.ct_o006 import Root


obj = Root(
    my_ele1="string data",
    my_ele2=132456,
    my_ele3=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctO006.xsd",
        "{http://tempuri.org/xmlschema}myAttr": "restriction attribute",
    },
    other_attributes={}
)
