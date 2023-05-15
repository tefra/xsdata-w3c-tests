from output.models.ms_data.complex_type.ct_g022_xsd.ct_g022 import Root


obj = Root(
    my_element1="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG022.xsd",
    },
    local_attr="test attribute",
    my_attr="second test attribute",
    local_attr1="group2 attribute",
    my_attr1="second group2 attribute"
)
