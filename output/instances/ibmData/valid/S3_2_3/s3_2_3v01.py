from output.models.ibm_data.valid.s3_2_3.s3_2_3v01_xsd.s3_2_3v01 import Root
from output.models.ibm_data.valid.s3_2_3.s3_2_3v01_xsd.s3_2_3v01 import Type1


obj = Root(
    element1=Type1(
        attr1=123,
        attr2=456
    )
)
