from output.models.saxon_data.wild.wild075_xsd.wild075 import B
from output.models.saxon_data.wild.wild075_xsd.wild075 import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    a=23,
    local_element=B(
        value=XmlDate(2010, 10, 16)
    )
)
