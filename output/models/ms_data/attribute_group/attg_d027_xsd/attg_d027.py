from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar foo:
    :ivar foo_attributes:
    """
    class Meta:
        name = "attRef"

    foo: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    foo_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="foo"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
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
