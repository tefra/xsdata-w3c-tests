from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://id040.ly/"


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
            "namespace": "http://id040.ly/",
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
            }
        )


@dataclass
class Doc:
    """
    :ivar chap_or_appx:
    """
    class Meta:
        name = "doc"
        namespace = "http://id040.ly/"

    chap_or_appx: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "chap",
                    "type": Chap,
                },
                {
                    "name": "appx",
                    "type": Chap,
                },
            ),
        }
    )
