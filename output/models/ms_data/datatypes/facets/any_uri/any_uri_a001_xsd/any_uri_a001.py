from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "1"


@dataclass
class Foo:
    """
    :ivar value_2_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "1"

    value_2_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="2"
        )
    )


class St(Enum):
    """
    :cvar VALUE_2:
    :cvar VALUE_4:
    :cvar VALUE_5:
    """
    VALUE_2 = "2"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass
class Bar:
    """
    :ivar value:
    """
    class Meta:
        name = "bar"
        namespace = "1"

    value: Optional[St] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
