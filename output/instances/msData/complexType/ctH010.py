from output.models.ms_data.complex_type.ct_h010_xsd.ct_h010 import Root


obj = Root(
    my_element1='test data',
    my_element2='test data',
    my_element3='test data',
    local_attributes={
        'myAttr': 'test attribute',
    },
    my_element='test data',
    my_attr1='another attribute',
    my_attr2='last group 1 attribute',
    my_attr3='another attribute',
    my_attr4='last group2 attribute'
)
