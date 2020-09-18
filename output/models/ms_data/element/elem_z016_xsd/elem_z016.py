from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Id:
    """
    :ivar value:
    """
    class Meta:
        name = "ID"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
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
        metadata=dict(
            required=True
        )
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
        metadata=dict(
            required=True,
            tokens=True
        )
    )


@dataclass
class DataTypes:
    """
    :ivar id:
    :ivar idref:
    :ivar idrefs:
    """
    id: List[Id] = field(
        default_factory=list,
        metadata=dict(
            name="ID",
            type="Element",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    idref: List[Idref] = field(
        default_factory=list,
        metadata=dict(
            name="IDREF",
            type="Element",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    idrefs: List[Idrefs] = field(
        default_factory=list,
        metadata=dict(
            name="IDREFS",
            type="Element",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )


@dataclass
class Root:
    """
    :ivar data_types:
    """
    data_types: List[DataTypes] = field(
        default_factory=list,
        metadata=dict(
            name="DataTypes",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
