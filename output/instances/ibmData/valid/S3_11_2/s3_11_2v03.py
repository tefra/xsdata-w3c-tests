from output.models.ibm_data.valid.s3_11_2.s3_11_2v03_xsd.s3_11_2v03 import Keyname
from output.models.ibm_data.valid.s3_11_2.s3_11_2v03_xsd.s3_11_2v03 import Root


obj = Root(
    number=[
        Keyname(
            numid=1,
            numname="a"
        ),
        Keyname(
            numid=1,
            numname="ab"
        ),
    ]
)
