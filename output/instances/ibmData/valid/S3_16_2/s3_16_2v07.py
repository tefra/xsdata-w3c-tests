from output.models.ibm_data.valid.s3_16_2.s3_16_2v07_xsd.s3_16_2v07 import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    union_element=[
        28,
        33,
        "az",
        -123,
        XmlDate(1999, 12, 31),
    ]
)
