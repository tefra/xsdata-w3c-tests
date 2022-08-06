from output.models.ibm_data.valid.s3_10_1.s3_10_1v07_xsd.s3_10_1v07 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_element=AnyElement(
        qname="{a}xx",
        text="2",
        tail=None,
        children=[],
        attributes={}
    )
)
