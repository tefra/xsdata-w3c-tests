from output.models.ms_data.element.elem_t040_xsd.elem_t040 import Root
from output.models.ms_data.element.elem_t040_xsd.elem_t040 import Test2
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    test2=Test2(
        any_element=AnyElement(
            text="1",
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        )
    )
)
