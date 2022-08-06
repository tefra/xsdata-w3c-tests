from output.models.ms_data.complex_type.ct_h058_xsd.ct_h058 import Root


obj = Root(
    my_element1=None,
    my_element2="test data",
    my_element3=None,
    local_attributes={
        "local": "extension local attribute",
    },
    my_attr="extension attribute",
    local_target_namespace_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctH058.xsd",
    }
)
