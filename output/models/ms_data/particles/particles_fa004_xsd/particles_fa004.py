from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "base"

    e1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            required=True
        )
    )
    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            required=True
        )
    )


@dataclass
class Doc(Base):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"