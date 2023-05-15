from output.models.ms_data.complex_type.ct_g046_xsd.ct_g046 import Root


obj = Root(
    my_element1="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG046.xsd",
    },
    my_attr="test attribute",
    my_attr2="second attribute"
)
