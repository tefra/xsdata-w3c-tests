from output.models.sun_data.wildcard.ps_contents.ps_contents00101m.ps_contents00101m1_xsd.ps_contents00101m1 import A
from output.models.sun_data.wildcard.ps_contents.ps_contents00101m.ps_contents00101m1_xsd.ps_contents00101m1 import Date
from xsdata.models.datatype import XmlDate


obj = A(
    any_element=Date(
        value=XmlDate(2002, 4, 29)
    )
)
