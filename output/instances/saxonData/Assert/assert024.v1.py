from output.models.saxon_data.assert_pkg.assert024_xsd.assert024 import Test
from xml.etree.ElementTree import QName


obj = Test(
    rule=[
        Test.Rule(
            name=QName("{http://www.w3.org/2001/XMLSchema}element")
        ),
    ]
)
