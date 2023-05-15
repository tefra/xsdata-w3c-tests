from output.models.sun_data.combined.identity.identity_test_suite.pkg_002.test_xsd.test import Root
from xml.etree.ElementTree import QName
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    key_or_ref=[
        QName("{abc}abc"),
        DerivedElement(
            qname="{foo}ref",
            value=QName("{abc}abc")
        ),
    ]
)
