from output.models.ibm_data.valid.s3_11_2.s3_11_2v04_xsd.s3_11_2v04 import Keyname
from output.models.ibm_data.valid.s3_11_2.s3_11_2v04_xsd.s3_11_2v04 import Root


obj = Root(
    number=[
        Keyname(
            numid=1,
            numname="a",
            id=100
        ),
        Keyname(
            numid=1,
            numname="ab",
            id=200
        ),
    ]
)
