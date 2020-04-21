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

    e1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    e2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Testing:
    """
    :ivar e1:
    :ivar e2:
    """
    class Meta:
        name = "testing"

    e1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    e2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc(Testing):
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"
