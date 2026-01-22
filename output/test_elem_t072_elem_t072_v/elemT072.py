from output.models.ms_data.element.elem_t072_xsd.elem_t072 import Root
from output.models.ms_data.element.elem_t072_xsd.elem_t072 import Test
from output.models.ms_data.element.elem_t072_xsd.elem_t072 import UnionAb


obj = Root(
    test=[
        Test(
            value=UnionAb.VALUE_3
        ),
        Test(
            value=UnionAb.VALUE_2
        ),
    ]
)
