from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Id:
    class Meta:
        name = "ID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Idref:
    class Meta:
        name = "IDREF"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Idrefs:
    class Meta:
        name = "IDREFS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class DataTypes:
    id: list[Id] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    idref: list[Idref] = field(
        default_factory=list,
        metadata={
            "name": "IDREF",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    idrefs: list[Idrefs] = field(
        default_factory=list,
        metadata={
            "name": "IDREFS",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class Root:
    data_types: list[DataTypes] = field(
        default_factory=list,
        metadata={
            "name": "DataTypes",
            "type": "Element",
        },
    )
