from dataclasses import dataclass, field
from typing import List


@dataclass
class Id:
    class Meta:
        name = "ID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Idref:
    class Meta:
        name = "IDREF"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Idrefs:
    class Meta:
        name = "IDREFS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        },
    )


@dataclass
class DataTypes:
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    idref: List[Idref] = field(
        default_factory=list,
        metadata={
            "name": "IDREF",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    idrefs: List[Idrefs] = field(
        default_factory=list,
        metadata={
            "name": "IDREFS",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class Root:
    data_types: List[DataTypes] = field(
        default_factory=list,
        metadata={
            "name": "DataTypes",
            "type": "Element",
        },
    )
