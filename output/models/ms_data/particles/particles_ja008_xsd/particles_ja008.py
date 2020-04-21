from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar any_element:
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class R(B):
    """
    :ivar e1:
    """
    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            min_occurs=2,
            max_occurs=2
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

    elem: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
