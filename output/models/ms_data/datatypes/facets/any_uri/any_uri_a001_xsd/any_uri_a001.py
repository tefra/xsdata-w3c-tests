from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

__NAMESPACE__ = "1"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "1"

    value_2_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "2",
        }
    )


class St(Enum):
    VALUE_2 = "2"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "1"

    value: Optional[St] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
