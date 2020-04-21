from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://simple001.ly/"


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
            namespace="http://simple001.ly/",
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
        nr: float = field(
            default=float('inf'),
            metadata=dict(
                type="Attribute"
            )
        )
        ref: float = field(
            init=False,
            default=float('inf'),
            metadata=dict(
                type="Attribute"
            )
        )


@dataclass
class Doc:
    """
    :ivar chap:
    :ivar appx:
    """
    class Meta:
        name = "doc"
        namespace = "http://simple001.ly/"

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
