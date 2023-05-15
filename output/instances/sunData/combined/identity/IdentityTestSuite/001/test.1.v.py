from decimal import Decimal
from output.models.sun_data.combined.identity.identity_test_suite.pkg_001.test_xsd.test import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    key_or_ref=[
        Decimal("5"),
        DerivedElement(
            qname="{foo}ref",
            value=Decimal("5.0")
        ),
    ]
)
