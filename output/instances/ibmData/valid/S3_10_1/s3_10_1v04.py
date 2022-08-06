from output.models.ibm_data.valid.s3_10_1.s3_10_1v04_xsd.s3_10_1v04 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    z=1,
    any_element=AnyElement(
        qname="{a}z",
        text="1",
        tail=None,
        children=[],
        attributes={}
    )
)
