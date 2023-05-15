from decimal import Decimal
from output.models.ibm_data.mixed.type_alternatives.test2_xsd.test2 import Example
from output.models.ibm_data.mixed.type_alternatives.test2_xsd.test2 import XDecimal
from output.models.ibm_data.mixed.type_alternatives.test2_xsd.test2 import XInt
from output.models.ibm_data.mixed.type_alternatives.test2_xsd.test2 import XString


obj = Example(
    x=[
        XInt(
            value=10,
            kind="quantity"
        ),
        XDecimal(
            value=Decimal("10.5"),
            kind="price"
        ),
        XString(
            value="hello world",
            kind="mesg"
        ),
    ]
)
