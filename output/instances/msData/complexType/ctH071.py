from output.models.ms_data.complex_type.ct_h071_xsd.ct_h071 import Root


obj = Root(
    my_element2="test data",
    local_attributes={
        "local": "extension attribute",
    },
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctH071.xsd",
    }
)
