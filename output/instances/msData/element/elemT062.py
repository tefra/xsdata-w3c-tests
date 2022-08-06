from output.models.ms_data.element.elem_t062_xsd.elem_t062 import A
from output.models.ms_data.element.elem_t062_xsd.elem_t062 import Root
from output.models.ms_data.element.elem_t062_xsd.elem_t062 import Sa2


obj = Root(
    sa3=[],
    sa2=[
        Sa2(
            value=A.VALUE_1,
            att=123
        ),
    ],
    sa1=[],
    test1=[],
    test2=None,
    test3=None,
    test4=None,
    test5=None
)
