from output.models.ms_data.complex_type.ct_h082_xsd.ct_h082 import Root


obj = Root(
    my_element1="test data",
    my_element2="test data",
    my_element3="test data",
    local_attributes={
        "local": "extension attribute",
    },
    my_element="test data",
    local_target_namespace_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctH082.xsd",
    }
)
