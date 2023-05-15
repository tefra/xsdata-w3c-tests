from output.models.ibm_data.valid.s3_10_1.s3_10_1v01_xsd.s3_10_1v01 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="{a}notDefinedInSchema",
            text="hi"
        ),
        AnyElement(
            qname="{b}a",
            text="hihi"
        ),
    ]
)
