from output.models.ms_data.complex_type.ct_i041_xsd.ct_i041 import MyType
from output.models.ms_data.complex_type.ct_i041_xsd.ct_i041 import Root


obj = Root(
    foo_test=MyType(
        foo_ele1="string",
        foo_ele2=26,
        foo_ele3=True
    )
)
