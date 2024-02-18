from output.models.ms_data.element.elem_t030_xsd.elem_t030 import A
from output.models.ms_data.element.elem_t030_xsd.elem_t030 import Root
from output.models.ms_data.element.elem_t030_xsd.elem_t030 import Test


obj = Root(
    s_a_or_test=Test(
        value=A.VALUE_1
    )
)
