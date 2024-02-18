from output.models.ms_data.element.elem_t073_xsd.elem_t073 import Root
from output.models.ms_data.element.elem_t073_xsd.elem_t073 import Test
from output.models.ms_data.element.elem_t073_xsd.elem_t073 import UnionAb


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
