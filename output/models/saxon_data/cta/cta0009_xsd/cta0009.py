from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Chap:
    """
    :ivar de:
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
    fr: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar chap:
    :ivar lang:
    """
    class Meta:
        name = "doc"

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
