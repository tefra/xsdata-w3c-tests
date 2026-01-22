from decimal import Decimal
from output.models.sun_data.attr_decl.ad_type.ad_type00101m.ad_type00101m_xsd.ad_type00101m import ElementWithAttr
from output.models.sun_data.attr_decl.ad_type.ad_type00101m.ad_type00101m_xsd.ad_type00101m import Root


obj = Root(
    element_with_attr=ElementWithAttr(
        price=Decimal('12.3')
    )
)
