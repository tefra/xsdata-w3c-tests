from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ValueConstraint(Enum):
    ASD = "asd"


@dataclass(kw_only=True)
class Idrefs:
    class Meta:
        name = "idrefs"

    idref: ValueConstraint = field(
        default=ValueConstraint.ASD,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    a: Ids = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: Idrefs = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
