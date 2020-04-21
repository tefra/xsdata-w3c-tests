from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    """
    :ivar e3:
    """
    class Meta:
        name = "base"

    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar e3:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    e3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
