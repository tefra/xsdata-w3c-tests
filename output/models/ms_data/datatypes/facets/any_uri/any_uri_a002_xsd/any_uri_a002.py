from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

__NAMESPACE__ = "あ"


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "あ"

    attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "あ",
        }
    )


class St(Enum):
    VALUE_1 = "あ1"
    VALUE_2 = "ぃ2"
    VALUE_3 = "い3"


@dataclass
class Bar:
    class Meta:
        name = "bar"
        namespace = "あ"

    value: Optional[St] = field(
        default=None
    )
