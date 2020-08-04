from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class B:
    """
    :ivar target003_com_attributes:
    """
    target003_com_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.target003.com/"
        )
    )


@dataclass
class R(B):
    """
    :ivar att:
    """
    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.target003.com/"
        )
    )


@dataclass
class Parent(R):
    class Meta:
        name = "parent"
