from output.models.saxon_data.wild.wild082_xsd.wild082 import A
from output.models.saxon_data.wild.wild082_xsd.wild082 import Root
from output.models.saxon_data.wild.wild082_xsd.wild082 import Zz


obj = Root(
    a=Zz(
        value="42",
        type_value=1
    ),
    local_element=A(
        value="93.7",
        type_value=2
    )
)
