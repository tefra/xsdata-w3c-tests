from output.models.ms_data.complex_type.ct_g031_xsd.ct_g031 import MyType
from output.models.ms_data.complex_type.ct_g031_xsd.ct_g031 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3=MyType.MyElement1(
        value='test data'
    ),
    my_attr1='test attribute'
)
