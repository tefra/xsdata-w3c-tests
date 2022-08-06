from output.models.ms_data.complex_type.ct_h001_xsd.ct_h001 import Root


obj = Root(
    my_element1="test data",
    my_element2="test data",
    my_element3="test data",
    local_attributes={
        "myAttr": "test attribute",
    },
    my_element="test data"
)
