from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class R:
    """
    :ivar www_target003_com_attributes:
    :ivar att:
    """
    www_target003_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.target003.com/"
        )
    )
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
