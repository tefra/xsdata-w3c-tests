from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar ca1:
    :ivar ca2:
    :ivar aga1:
    :ivar aga2:
    :ivar ga2:
    """
    class Meta:
        name = "attRef"

    ca1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    ca2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    aga1: str = field(
        default="abc",
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    aga2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    ga2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    :ivar ga1:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    ga1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
