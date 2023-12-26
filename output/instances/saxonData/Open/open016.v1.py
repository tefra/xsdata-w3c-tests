from output.models.saxon_data.open.open016_xsd.open016 import Doc
from xsdata.models.datatype import XmlDate


obj = Doc(
    value=XmlDate(2009, 12, 12),
    evidence='none'
)
