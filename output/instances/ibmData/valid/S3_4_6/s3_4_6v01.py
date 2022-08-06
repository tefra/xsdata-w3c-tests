from output.models.ibm_data.valid.s3_4_6.s3_4_6v01_xsd.s3_4_6v01 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=1,
    any_element=[
        AnyElement(
            qname="wildcard",
            text="1",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="wildcard2",
            text="hi.123",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="wildcard3",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="hello",
                    text="&#10;   moo&#10;  ",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
    ]
)
