from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union


@dataclass
class Appendix:
    class Meta:
        name = "appendix"

    value: Optional[Union[str, datetime]] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Chap:
    class Meta:
        name = "chap"

    value: Optional[Union[str, datetime]] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    appendix: List[Appendix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    chap: List[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
