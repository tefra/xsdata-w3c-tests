from output.models.ms_data.element.elem_t058_xsd.elem_t058 import A
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import ECa
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import RCa
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import Root


obj = Root(
    sa=None,
    test1=A.VALUE_1,
    test2=A.VALUE_1,
    test3=A.VALUE_1,
    test4=RCa(
        x=[
            "",
        ],
        y=None
    ),
    test5=ECa(
        x=[
            "",
        ],
        y="",
        z=""
    )
)
