from output.models.ibm_data.valid.d4_3_15.d4_3_15v13_xsd.d4_3_15v13 import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    date_ele=XmlDate(2000, 12, 12)
)
