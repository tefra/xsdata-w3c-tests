from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Idrefs:
    class Meta:
        name = "idrefs"

    idref_subelement: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    idref1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idref2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    idref_element: list[Idrefs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    id1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(Ids):
    class Meta:
        name = "root"
