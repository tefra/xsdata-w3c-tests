from output.models.ms_data.complex_type.ct_g033_xsd.ct_g033 import MyType
from output.models.ms_data.complex_type.ct_g033_xsd.ct_g033 import Root


obj = Root(
    my_element1_or_my_element2_or_my_element3=MyType.MyElement1(
        value='test data'
    ),
    my_attr='test attribute'
)
