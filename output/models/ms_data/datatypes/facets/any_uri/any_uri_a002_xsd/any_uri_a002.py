from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "あ"


@dataclass
class Foo:
    """
    :ivar attributes:
    """
    class Meta:
        name = "foo"
        namespace = "あ"

    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="あ"
        )
    )


class St(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    """
    VALUE_1 = "あ1"
    VALUE_2 = "ぃ2"
    VALUE_3 = "い3"


@dataclass
class Bar:
    """
    :ivar value:
    """
    class Meta:
        name = "bar"
        namespace = "あ"

    value: Optional[St] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
