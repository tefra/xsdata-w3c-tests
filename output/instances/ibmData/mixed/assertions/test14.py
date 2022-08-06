from output.models.ibm_data.mixed.assertions.test14_xsd.test14 import Example
from output.models.ibm_data.mixed.assertions.test14_xsd.test14 import XType


obj = Example(
    x=[
        XType(
            value=101,
            a=210
        ),
        XType(
            value=100,
            a=410
        ),
        XType(
            value=2001,
            a=640
        ),
    ]
)
