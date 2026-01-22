from output.models.ms_data.complex_type.ct_h035_xsd.ct_h035 import MyType
from output.models.ms_data.complex_type.ct_h035_xsd.ct_h035 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3=MyType.MyElement2(
        value='test data'
    ),
    local_attributes={
        'local': 'local attribute',
    },
    my_element4='test data',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctH035.xsd',
        '{http://tempuri.org/xmlschema}myAttr': 'next attribute',
    }
)
