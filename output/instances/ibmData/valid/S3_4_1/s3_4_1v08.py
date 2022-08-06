from output.models.ibm_data.valid.s3_4_1.s3_4_1v08_xsd.s3_4_1v08 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v08_xsd.s3_4_1v08 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=D(
        x=1,
        y=2,
        any_element=AnyElement(
            qname="asd",
            text="asd",
            tail=None,
            children=[],
            attributes={}
        ),
        z=0
    )
)
