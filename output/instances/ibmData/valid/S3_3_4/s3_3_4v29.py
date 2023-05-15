from output.models.ibm_data.valid.s3_3_4.s3_3_4v29_xsd.s3_3_4v29 import Ids
from output.models.ibm_data.valid.s3_3_4.s3_3_4v29_xsd.s3_3_4v29 import Root


obj = Root(
    multiple_ids=Ids(
        idref_element1="abc",
        idref_element2="xyz"
    )
)
