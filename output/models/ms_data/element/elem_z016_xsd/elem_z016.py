from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DataTypes:
    """
    :ivar id:
    :ivar idref:
    :ivar idrefs:
    """
    id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    idref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "IDREF",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    idrefs: List[List[str]] = field(
        default_factory=list,
        metadata={
            "name": "IDREFS",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
            "tokens": True,
        }
    )


@dataclass
class Id:
    """
    :ivar value:
    """
    class Meta:
        name = "ID"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Idref:
    """
    :ivar value:
    """
    class Meta:
        name = "IDREF"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Idrefs:
    """
    :ivar value:
    """
    class Meta:
        name = "IDREFS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class Root:
    """
    :ivar data_types:
    """
    data_types: List[DataTypes] = field(
        default_factory=list,
        metadata={
            "name": "DataTypes",
            "type": "Element",
        }
    )
