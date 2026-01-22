from decimal import Decimal
from output.models.ms_data.attribute.att_q014_xsd.att_q014 import Doc
from output.models.ms_data.attribute.att_q014_xsd.att_q014 import InternationalPrice


obj = Doc(
    international_price=InternationalPrice(
        value=Decimal('423.46'),
        currency='EUR'
    )
)
