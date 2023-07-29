from output.models.ms_data.element.elem_z010_xsd.elem_z010 import Root
from output.models.ms_data.element.elem_z010_xsd.elem_z010_a import A
from output.models.ms_data.element.elem_z010_xsd.elem_z010_b import B
from output.models.ms_data.element.elem_z010_xsd.elem_z010_c import C
from output.models.ms_data.element.elem_z010_xsd.elem_z010_d import D


obj = Root(
    a=A(
        d=D(

        ),
        c=C(

        ),
        b=B(

        ),
        a=A(

        )
    )
)
