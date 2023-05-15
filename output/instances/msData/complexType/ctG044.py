from output.models.ms_data.complex_type.ct_g044_xsd.ct_g044 import Root


obj = Root(
    my_element1="test data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG044.xsd",
    },
    my_attr1="test attribute",
    my_attr2="second test attribute"
)
