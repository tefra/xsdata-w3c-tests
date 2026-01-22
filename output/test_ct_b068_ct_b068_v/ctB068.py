from output.models.ms_data.complex_type.ct_b068_xsd.ct_b068 import FooType
from output.models.ms_data.complex_type.ct_b068_xsd.ct_b068 import Root


obj = Root(
    my_element_or_my_ele2=FooType.MyElement(
        value='all field'
    ),
    attr_test='attribute1',
    attr_test2='attribute2'
)
