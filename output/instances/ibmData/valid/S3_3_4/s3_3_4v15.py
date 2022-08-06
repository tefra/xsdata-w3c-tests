from output.models.ibm_data.valid.s3_3_4.s3_3_4v15_xsd.s3_3_4v15 import Root
from output.models.ibm_data.valid.s3_3_4.s3_3_4v15_xsd.s3_3_4v15 import Wrapper


obj = Wrapper(
    root=Root(
        value=[
            "b1",
            "b2",
            "b3",
        ],
        idref_attr="b2"
    )
)
