from output.models.ms_data.complex_type.ct_g032_xsd.ct_g032 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG032.xsd",
    },
    my_attr1="test attribute",
    my_attr2="second attribute"
)
