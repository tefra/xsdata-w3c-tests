from output.models.ms_data.complex_type.ct_g011_xsd.ct_g011 import Root


obj = Root(
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctG011.xsd',
        'myAttr': 'test attribute',
    },
    my_element='test data'
)
