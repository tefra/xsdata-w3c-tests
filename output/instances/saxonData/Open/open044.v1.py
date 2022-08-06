from output.models.saxon_data.open.open044_xsd.open044 import Beta
from output.models.saxon_data.open.open044_xsd.open044 import Doc
from output.models.saxon_data.open.open044_xsd.open044x import Alpha
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
                other_attributes={
                    "{http://www.w3.org/XML/1998/namespace}lang": "jp",
                },
                w3_org_xml_1998_namespace_attributes={}
            ),
            type="beta"
        ),
    ]
)
