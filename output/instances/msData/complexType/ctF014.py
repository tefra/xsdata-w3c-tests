from output.models.ms_data.complex_type.ct_f014_xsd.ct_f014 import MyType
from output.models.ms_data.complex_type.ct_f014_xsd.ct_f014 import Root


obj = Root(
    my_element_or_my_element2=MyType.MyElement(
        value='test data'
    ),
    my_attr='test attribute',
    my_element3='sequence test data'
)
