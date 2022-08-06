from output.models.ms_data.complex_type.ct_g021_xsd.ct_g021 import Root


obj = Root(
    my_element1="test data",
    my_element2=None,
    my_element3=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG021.xsd",
    },
    local_attr="test attribute",
    my_attr="second test attribute"
)
