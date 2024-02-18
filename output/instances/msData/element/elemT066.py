from output.models.ms_data.element.elem_t066_xsd.elem_t066 import RA
from output.models.ms_data.element.elem_t066_xsd.elem_t066 import Root
from output.models.ms_data.element.elem_t066_xsd.elem_t066 import Sa1


obj = Root(
    choice=[
        Sa1(
            value=RA.VALUE_1
        ),
    ]
)
