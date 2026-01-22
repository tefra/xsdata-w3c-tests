from output.models.ms_data.element.elem_t071_xsd.elem_t071 import Root
from output.models.ms_data.element.elem_t071_xsd.elem_t071 import Test
from output.models.ms_data.element.elem_t071_xsd.elem_t071 import UnionA


obj = Root(
    test=[
        Test(
            value=UnionA.VALUE_3
        ),
        Test(
            value=UnionA.VALUE_2
        ),
    ]
)
