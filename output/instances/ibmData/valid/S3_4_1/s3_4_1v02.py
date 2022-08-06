from output.models.ibm_data.valid.s3_4_1.s3_4_1v02_xsd.s3_4_1v02 import C
from output.models.ibm_data.valid.s3_4_1.s3_4_1v02_xsd.s3_4_1v02 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v02_xsd.s3_4_1v02 import E
from output.models.ibm_data.valid.s3_4_1.s3_4_1v02_xsd.s3_4_1v02 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=None,
    p=C(
        any_element=AnyElement(
            qname="qwe",
            text="s",
            tail=None,
            children=[],
            attributes={}
        ),
        x=1
    ),
    q=D(
        any_element=AnyElement(
            qname="wer",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="g",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        z=2
    ),
    r=E(
        any_element=AnyElement(
            qname="lj",
            text="we",
            tail=None,
            children=[],
            attributes={}
        ),
        y=1
    )
)
