from output.models.ms_data.complex_type.ct_d030_xsd.ct_d030 import Root


obj = Root(
    value="&#10;&#9;any string&#10;",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctD030.xsd",
    },
    my_attr="test",
    my_attr2="second attribute"
)
