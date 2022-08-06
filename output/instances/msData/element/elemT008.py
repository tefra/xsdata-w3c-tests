from output.models.ms_data.element.elem_t008_xsd.elem_t008 import MyType
from output.models.ms_data.element.elem_t008_xsd.elem_t008 import Root


obj = Root(
    foo_test=MyType(
        foo_ele1="string",
        foo_ele2=26,
        foo_ele3=True
    )
)
