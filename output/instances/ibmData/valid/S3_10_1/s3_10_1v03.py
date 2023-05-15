from output.models.ibm_data.valid.s3_10_1.s3_10_1v03_xsd.s3_10_1v03 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    q_element=AnyElement(
        qname="{q}wildcard",
        text="1"
    )
)
