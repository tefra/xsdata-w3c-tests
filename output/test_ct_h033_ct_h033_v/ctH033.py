from output.models.ms_data.complex_type.ct_h033_xsd.ct_h033 import MyType
from output.models.ms_data.complex_type.ct_h033_xsd.ct_h033 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3=MyType.MyElement2(
        value='test data'
    ),
    local_attributes={
        'local': 'local attribute',
    },
    my_element4='test data',
    attr1='next attribute',
    attr2='second group attribute'
)
