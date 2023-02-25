from output.models.ms_data.complex_type.ct_g034_xsd.ct_g034 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG034.xsd",
    },
    my_attr="test attribute",
    my_attr2="second attribute"
)
