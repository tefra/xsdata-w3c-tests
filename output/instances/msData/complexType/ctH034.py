from output.models.ms_data.complex_type.ct_h034_xsd.ct_h034 import MyType
from output.models.ms_data.complex_type.ct_h034_xsd.ct_h034 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3=MyType.MyElement2(
        value='test data'
    ),
    local_attributes={
        'local': 'local attribute',
    },
    my_element4='test data',
    attr1='group1 attribute',
    attr2='group1 second attribute',
    attr3='group2 attribute',
    attr4='group2 second attribute'
)
