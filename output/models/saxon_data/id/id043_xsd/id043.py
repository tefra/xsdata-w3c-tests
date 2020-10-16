from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://id043.ly/"


@dataclass
class Chap:
    """
    :ivar section:
    """
    class Meta:
        name = "chap"

    section: List["Chap.Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://id043.ly/",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Section:
        """
        :ivar value:
        :ivar nr:
        """
        value: Optional[str] = field(
            default=None,
        )
        nr: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class Doc:
    """
    :ivar chap:
    :ivar appx:
    """
    class Meta:
        name = "doc"
        namespace = "http://id043.ly/"

    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    appx: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
