from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Base:
    """
    :ivar att1:
    :ivar att2:
    :ivar any_attributes:
    """
    class Meta:
        name = "base"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
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
class Doc(Base):
    class Meta:
        name = "doc"
