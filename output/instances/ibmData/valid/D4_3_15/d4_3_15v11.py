from output.models.ibm_data.valid.d4_3_15.d4_3_15v11_xsd.d4_3_15v11 import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    ele="hello",
    date=XmlDate(2000, 12, 12)
)
