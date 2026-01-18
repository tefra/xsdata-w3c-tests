from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "あ"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "あ"

    attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "あ",
        },
    )


class St(Enum):
    VALUE_1 = "あ1"
    VALUE_2 = "ぃ2"
    VALUE_3 = "い3"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "あ"

    value: St = field(
        metadata={
            "required": True,
        }
    )
