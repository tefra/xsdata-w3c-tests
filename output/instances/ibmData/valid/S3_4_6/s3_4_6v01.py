from output.models.ibm_data.valid.s3_4_6.s3_4_6v01_xsd.s3_4_6v01 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=1,
    any_element=[
        AnyElement(
            qname="wildcard",
            text="1"
        ),
        AnyElement(
            qname="wildcard2",
            text="hi.123"
        ),
        AnyElement(
            qname="wildcard3",
            text="",
            children=[
                AnyElement(
                    qname="hello",
                    text="&#10;   moo&#10;  "
                ),
            ]
        ),
    ]
)
