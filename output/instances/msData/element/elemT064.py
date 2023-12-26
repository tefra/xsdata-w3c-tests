from output.models.ms_data.element.elem_t064_xsd.elem_t064 import Root
from output.models.ms_data.element.elem_t064_xsd.elem_t064 import Sa3
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    choice=[
        Sa3(
            any_element=AnyElement(
                text='1'
            )
        ),
    ]
)
