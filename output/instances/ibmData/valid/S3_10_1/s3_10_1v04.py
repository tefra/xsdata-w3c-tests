from output.models.ibm_data.valid.s3_10_1.s3_10_1v04_xsd.s3_10_1v04 import Root
from output.models.ibm_data.valid.s3_10_1.s3_10_1v04_xsd.s3_10_1v04 import Z


obj = Root(
    z=1,
    any_element=Z(
        value=1
    )
)
