from output.models.ms_data.complex_type.ct_h069_xsd.ct_h069 import Root


obj = Root(
    my_element2="test data",
    local_attributes={
        "local": "extension attribute",
    },
    my_attr1="extension group attribute",
    my_attr2="extension group second attribute",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctH069.xsd",
    }
)
