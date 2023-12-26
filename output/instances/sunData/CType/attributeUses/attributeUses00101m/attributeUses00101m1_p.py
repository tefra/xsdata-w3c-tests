from output.models.sun_data.ctype.attribute_uses.attribute_uses00101m.attribute_uses00101m1_xsd.attribute_uses00101m1 import A
from xsdata.models.datatype import XmlDate


obj = A(
    value=123,
    attr1='abc',
    attr2=XmlDate(2002, 4, 9)
)
