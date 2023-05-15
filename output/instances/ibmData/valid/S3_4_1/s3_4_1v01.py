from output.models.ibm_data.valid.s3_4_1.s3_4_1v01_xsd.s3_4_1v01 import C
from output.models.ibm_data.valid.s3_4_1.s3_4_1v01_xsd.s3_4_1v01 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=C(
        any_element=AnyElement(
            qname="a",
            text="1"
        )
    )
)
