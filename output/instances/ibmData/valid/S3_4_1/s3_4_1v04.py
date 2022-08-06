from output.models.ibm_data.valid.s3_4_1.s3_4_1v04_xsd.s3_4_1v04 import C
from output.models.ibm_data.valid.s3_4_1.s3_4_1v04_xsd.s3_4_1v04 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=C(
        x=1,
        y=2,
        any_element=AnyElement(
            qname="z",
            text="sdf9873",
            tail=None,
            children=[],
            attributes={}
        )
    ),
    any_element=None
)
