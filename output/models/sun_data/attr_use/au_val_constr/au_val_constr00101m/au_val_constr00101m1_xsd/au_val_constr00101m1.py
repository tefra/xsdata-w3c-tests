from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrUse/valConstr"


@dataclass
class ElementWithAttr:
    """
    :ivar number:
    """
    class Meta:
        name = "elementWithAttr"
        namespace = "AttrUse/valConstr"

    number: int = field(
        init=False,
        default=12,
        metadata=dict(
            type="Attribute",
            namespace="AttrUse/valConstr"
        )
    )


@dataclass
class Root:
    """
    :ivar element_with_attr:
    """
    class Meta:
        name = "root"
        namespace = "AttrUse/valConstr"

    element_with_attr: Optional[ElementWithAttr] = field(
        default=None,
        metadata=dict(
            name="elementWithAttr",
            type="Element",
            required=True
        )
    )
