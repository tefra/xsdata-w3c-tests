from decimal import Decimal
from output.models.sun_data.combined.identity.identity_test_suite.pkg_001.test_xsd.test import Root


obj = Root(
    key_or_ref=[
        Root.Key(
            value=Decimal('5')
        ),
        Root.Ref(
            value=Decimal('5.0')
        ),
    ]
)
