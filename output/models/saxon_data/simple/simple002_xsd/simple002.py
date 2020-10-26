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
        metadata={
            "type": "Element",
            "namespace": "http://simple001.ly/",
            "min_occurs": 1,
        }
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
            metadata={
                "type": "Attribute",
            }
        )
        ref: float = field(
            init=False,
            default=float('inf'),
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
        namespace = "http://simple001.ly/"

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
