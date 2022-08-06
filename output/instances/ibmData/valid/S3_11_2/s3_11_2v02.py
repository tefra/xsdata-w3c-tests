from output.models.ibm_data.valid.s3_11_2.s3_11_2v02_xsd.s3_11_2v02 import Numtype
from output.models.ibm_data.valid.s3_11_2.s3_11_2v02_xsd.s3_11_2v02 import Root


obj = Root(
    number=[
        Numtype(
            value=3,
            id_1=2,
            id_2="a"
        ),
        Numtype(
            value=2,
            id_1=2,
            id_2="c"
        ),
    ]
)
