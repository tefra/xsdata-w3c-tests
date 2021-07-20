from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DataTypes:
    id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    idref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "IDREF",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    idrefs: List[List[str]] = field(
        default_factory=list,
        metadata={
            "name": "IDREFS",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
            "tokens": True,
        }
    )


@dataclass
class Id:
    class Meta:
        name = "ID"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Idref:
    class Meta:
        name = "IDREF"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Idrefs:
    class Meta:
        name = "IDREFS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Root:
    data_types: List[DataTypes] = field(
        default_factory=list,
        metadata={
            "name": "DataTypes",
            "type": "Element",
        }
    )
