from output.models.ms_data.element.elem_t062_xsd.elem_t062 import A
from output.models.ms_data.element.elem_t062_xsd.elem_t062 import Root
from output.models.ms_data.element.elem_t062_xsd.elem_t062 import Sa2


obj = Root(
    choice=[
        Sa2(
            value=A.VALUE_1,
            att=123
        ),
    ]
)
