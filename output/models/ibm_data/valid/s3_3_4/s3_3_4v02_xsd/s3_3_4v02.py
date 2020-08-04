from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class AnyAttr:
    """
    :ivar id1:
    :ivar any_attributes:
    """
    class Meta:
        name = "anyAttr"

    id1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Root:
    """
    :ivar a:
    """
    class Meta:
        name = "root"

    a: Optional[AnyAttr] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
