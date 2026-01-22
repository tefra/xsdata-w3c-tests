from output.models.ibm_data.valid.s3_12.s3_12v04_xsd.s3_12v04 import FloatType
from output.models.ibm_data.valid.s3_12.s3_12v04_xsd.s3_12v04 import Root


obj = Root(
    elem1=[
        FloatType(
            value=1e+104,
            type_value='float'
        ),
        FloatType(
            value=float("inf"),
            type_value='double'
        ),
    ]
)
