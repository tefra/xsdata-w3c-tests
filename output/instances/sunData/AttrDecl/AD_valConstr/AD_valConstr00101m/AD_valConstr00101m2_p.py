from decimal import Decimal
from output.models.sun_data.attr_decl.ad_val_constr.ad_val_constr00101m.ad_val_constr00101m_xsd.ad_val_constr00101m import ElementWithAttr
from output.models.sun_data.attr_decl.ad_val_constr.ad_val_constr00101m.ad_val_constr00101m_xsd.ad_val_constr00101m import Root


obj = Root(
    element_with_attr=ElementWithAttr(
        number=12,
        price=Decimal("12.3")
    )
)
