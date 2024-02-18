from output.models.ms_data.element.elem_t016_xsd.elem_t016 import A
from output.models.ms_data.element.elem_t016_xsd.elem_t016 import Root
from output.models.ms_data.element.elem_t016_xsd.elem_t016 import Test


obj = Root(
    s_a_or_test=Test(
        value=A.VALUE_1
    )
)
