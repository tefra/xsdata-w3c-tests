from output.models.ibm_data.valid.s3_3_4.s3_3_4v01_xsd.s3_3_4v01 import AnyAttr
from output.models.ibm_data.valid.s3_3_4.s3_3_4v01_xsd.s3_3_4v01 import Root


obj = Root(
    a=AnyAttr(
        id1="qwe"
    ),
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "s3_3_4v01.xsd",
        "globalAttr": "asd",
    }
)
