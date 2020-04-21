from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Chap:
    """
    :ivar de:
    :ivar lang:
    :ivar fr:
    """
    class Meta:
        name = "chap"

    de: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    fr: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Part:
    """
    :ivar chap:
    :ivar lang:
    """
    class Meta:
        name = "part"

    chap: List[Chap] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar part:
    :ivar lang:
    """
    class Meta:
        name = "doc"

    part: List[Part] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
