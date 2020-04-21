from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "attrWildcard"


@dataclass
class A:
    """
    :ivar b:
    :ivar any_attributes:
    """
    b: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "attrWildcard"
