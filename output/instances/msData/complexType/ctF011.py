from output.models.ms_data.complex_type.ct_f011_xsd.ct_f011 import MyType
from output.models.ms_data.complex_type.ct_f011_xsd.ct_f011 import Root


obj = Root(
    my_element_or_my_element2=MyType.MyElement(
        value='test data'
    ),
    my_attr='test attribute',
    my_element3='first sequence data',
    my_element4='second sequence data'
)
