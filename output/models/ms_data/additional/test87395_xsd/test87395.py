from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "foo"


class St(Enum):
    A = "a"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "foo"

    value: St = field()


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "foo"

    a: A = field(
        metadata={
            "type": "Element",
        }
    )
