from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ctype:
    class Meta:
        name = "ctype"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Ctype2(Ctype):
    class Meta:
        name = "ctype2"

    val2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Tabletype:
    class Meta:
        name = "tabletype"

    c: Ctype = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
