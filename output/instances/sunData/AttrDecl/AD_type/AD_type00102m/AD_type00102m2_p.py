from decimal import Decimal
from output.models.sun_data.attr_decl.ad_type.ad_type00102m.ad_type00102m_xsd.ad_type00102m import ElementWithAttr
from output.models.sun_data.attr_decl.ad_type.ad_type00102m.ad_type00102m_xsd.ad_type00102m import Root


obj = Root(
    element_with_attr=ElementWithAttr(
        price=Decimal('1.1')
    )
)
