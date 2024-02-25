from output.models.sun_data.combined.identity.identity_test_suite.pkg_002.test_xsd.test import Root
from xml.etree.ElementTree import QName


obj = Root(
    key_or_ref=[
        Root.Key(
            value=QName("{abc}abc")
        ),
        Root.Ref(
            value=QName("{abc}abc")
        ),
    ]
)
