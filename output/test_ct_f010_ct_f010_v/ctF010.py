from output.models.ms_data.complex_type.ct_f010_xsd.ct_f010 import MyType
from output.models.ms_data.complex_type.ct_f010_xsd.ct_f010 import Root


obj = Root(
    my_element_or_my_element2=MyType.MyElement(
        value='test data'
    ),
    my_attr='test attribute'
)
