from output.models.ms_data.complex_type.ct_i034_xsd.ct_i034 import MyType
from output.models.ms_data.complex_type.ct_i034_xsd.ct_i034 import Root


obj = Root(
    foo_test=MyType(
        foo_ele1="len4",
        foo_ele2=26,
        foo_ele3=None,
        other_attributes={
            "{http://www.w3.org/2001/XMLSchema-instance}type": "myType",
        }
    )
)
