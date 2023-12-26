from output.models.ms_data.complex_type.ct_h011_xsd.ct_h011 import Root


obj = Root(
    my_element1='test data',
    my_element2='test data',
    my_element3='test data',
    local_attributes={
        'myAttr': 'test attribute',
    },
    my_element='test data',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctH011.xsd',
        '{http://tempuri.org/xmlschema}myAttr1': 'another attribute',
    }
)
