from output.models.ibm_data.valid.s3_10_6.s3_10_6v01_xsd.s3_10_6v01 import Root
from output.models.ibm_data.valid.s3_10_6.s3_10_6v01_xsd.s3_10_6v01 import T


obj = Root(
    e1=T.E1(
        any_attributes={
            "{b}asd": "1",
        }
    ),
    e2=T.E2(
        any_attributes={
            "asd": "1",
        }
    )
)
