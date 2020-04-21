from decimal import Decimal
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://simple003.ly/"


@dataclass
class Chap:
    """
    :ivar section:
    """
    class Meta:
        name = "chap"

    section: List["Chap.Section"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://simple003.ly/",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Section:
        """
        :ivar value:
        :ivar nr:
        :ivar ref:
        """
        value: Optional[str] = field(
            default=None,
        )
        nr: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )
        ref: Optional[Decimal] = field(
            default=None,
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Doc:
    """
    :ivar chap:
    :ivar appx:
    :ivar date:
    """
    class Meta:
        name = "doc"
        namespace = "http://simple003.ly/"

    chap: List[Chap] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    appx: List[Chap] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"2012.*"
        )
    )
