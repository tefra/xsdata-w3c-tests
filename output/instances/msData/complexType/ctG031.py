from output.models.ms_data.complex_type.ct_g031_xsd.ct_g031 import Root


obj = Root(
    my_element1="test data",
    my_element2=None,
    my_element3=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG031.xsd",
    },
    my_attr1="test attribute"
)
