from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class TypeAbstract:
    class Meta:
        name = "typeAbstract"


@dataclass(kw_only=True)
class Elt1(TypeAbstract):
    class Meta:
        name = "elt1"


@dataclass(kw_only=True)
class TypeA(TypeAbstract):
    class Meta:
        name = "typeA"

    elt2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
