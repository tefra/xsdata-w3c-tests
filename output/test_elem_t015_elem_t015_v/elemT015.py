from output.models.ms_data.element.elem_t015_xsd.elem_t015 import FooTest
from output.models.ms_data.element.elem_t015_xsd.elem_t015 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_test=FooTest(
        any_element=AnyElement(
            text='1',
            attributes={
                '{http://www.w3.org/2001/XMLSchema-instance}type': 'myList',
            }
        )
    )
)
