from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e2:
    :ivar e3:
    """
    class Meta:
        name = "base"

    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc:
    """
    :ivar e2:
    :ivar e3:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
