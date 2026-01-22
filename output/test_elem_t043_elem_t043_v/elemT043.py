from output.models.ms_data.element.elem_t043_xsd.elem_t043 import Root
from output.models.ms_data.element.elem_t043_xsd.elem_t043 import Test2
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    test2=Test2(
        any_element=AnyElement(
            text='1 2 a 3',
            attributes={
                '{http://www.w3.org/2001/XMLSchema-instance}type': 'List-AB',
            }
        )
    )
)
