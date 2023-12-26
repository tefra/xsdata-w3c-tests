from output.models.ms_data.element.elem_t058_xsd.elem_t058 import A
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import ECa
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import RCa
from output.models.ms_data.element.elem_t058_xsd.elem_t058 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    sa_or_test1=A.VALUE_1,
    test2=A.VALUE_1,
    test3=A.VALUE_1,
    test4=DerivedElement(
        qname='test4',
        value=RCa(
            x=[
                '',
            ]
        ),
        type='R-CA'
    ),
    test5=DerivedElement(
        qname='test5',
        value=ECa(
            x=[
                '',
            ],
            y='',
            z=''
        ),
        type='E-CA'
    )
)
