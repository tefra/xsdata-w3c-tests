from output.models.saxon_data.assert_pkg.assert006_xsd.assert006 import Derived
from output.models.saxon_data.assert_pkg.assert006_xsd.assert006 import Outer


obj = Outer(
    inner=[
        Derived(
            value=4
        ),
        Derived(
            value=20
        ),
        Derived(
            value=10
        ),
    ]
)
