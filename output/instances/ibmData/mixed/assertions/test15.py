from output.models.ibm_data.mixed.assertions.test15_xsd.test15 import Example
from output.models.ibm_data.mixed.assertions.test15_xsd.test15 import XType


obj = Example(
    x=[
        XType(
            value=2,
            a='val1'
        ),
        XType(
            value=4,
            a='val2'
        ),
        XType(
            value=6,
            a='val3'
        ),
    ],
    x_count=3
)
