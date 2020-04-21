from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar c1:
    :ivar c2:
    """
    class Meta:
        name = "base"

    c1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    c2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc(Base):
    """
    :ivar g1:
    :ivar g2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    g1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    g2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
