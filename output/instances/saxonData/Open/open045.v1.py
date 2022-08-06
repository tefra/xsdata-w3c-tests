from output.models.saxon_data.open.open045_xsd.open045 import Beta
from output.models.saxon_data.open.open045_xsd.open045 import Doc
from output.models.saxon_data.open.open045_xsd.open045x import Alpha
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    w3_org_xml_1998_namespace_attributes={},
    content=[
        DerivedElement(
            qname="a",
            value=Alpha(

            ),
            type="alpha"
        ),
        DerivedElement(
            qname="b",
            value=Beta(
                w3_org_xml_1998_namespace_attributes={}
            ),
            type="beta"
        ),
    ]
)
