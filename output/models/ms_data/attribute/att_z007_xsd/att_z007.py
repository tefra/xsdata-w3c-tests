from dataclasses import dataclass, field
from typing import Optional


@dataclass
class One:
    """
    :ivar elem1:
    :ivar elem2:
    :ivar att1:
    :ivar att2:
    """
    elem1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    elem2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Two(One):
    pass


@dataclass
class Three(Two):
    """
    :ivar att1:
    """
    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar e1:
    :ivar e2:
    :ivar e3:
    """
    class Meta:
        name = "doc"

    e1: Optional[One] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e2: Optional[Two] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    e3: Optional[Three] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
