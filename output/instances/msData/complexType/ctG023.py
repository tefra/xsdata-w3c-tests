from output.models.ms_data.complex_type.ct_g023_xsd.ct_g023 import Root


obj = Root(
    my_element1="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG023.xsd",
        "localAttr": "test attribute",
    }
)
