from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "1"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "1"

    value_2_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "2",
        },
    )


class St(Enum):
    VALUE_2 = "2"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "1"

    value: St = field()
