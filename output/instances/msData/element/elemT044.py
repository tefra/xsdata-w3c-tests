from output.models.ms_data.element.elem_t044_xsd.elem_t044 import A
from output.models.ms_data.element.elem_t044_xsd.elem_t044 import Root
from output.models.ms_data.element.elem_t044_xsd.elem_t044 import Test


obj = Root(
    sa_or_test=Test(
        value=A.VALUE_1
    )
)
