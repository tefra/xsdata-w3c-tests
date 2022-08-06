from output.models.ibm_data.valid.s3_10_1.s3_10_1v06_xsd.s3_10_1v06 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    d=None,
    b=1,
    any_element=[
        AnyElement(
            qname="{a}x",
            text="1",
            tail=None,
            children=[],
            attributes={}
        ),
    ],
    c=1
)
