from decimal import Decimal
from output.models.sun_data.combined.identity.identity_test_suite.pkg_003.test_xsd.test import Root


obj = Root(
    key_or_ref=[
        Root.Key(
            id=Decimal("0")
        ),
        Decimal("-0"),
    ]
)
