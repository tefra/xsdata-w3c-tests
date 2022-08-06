from output.models.ibm_data.valid.s3_12.s3_12v10_xsd.s3_12v10 import DimType
from output.models.ibm_data.valid.s3_12.s3_12v10_xsd.s3_12v10 import Shape


obj = Shape(
    dimension=[
        DimType(
            value="square",
            length="1.0",
            width="1"
        ),
        DimType(
            value="lrectangle",
            length="2.0",
            width="1.1"
        ),
        DimType(
            value="other",
            length="1",
            width="2"
        ),
    ]
)
