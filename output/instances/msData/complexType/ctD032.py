from output.models.ms_data.complex_type.ct_d032_xsd.ct_d032 import Root


obj = Root(
    value="&#10;&#9;any string&#10;",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctD032.xsd",
    },
    my_attr="group attribute",
    my_attr1="second group attribute"
)
