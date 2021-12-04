from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Back:
    class Meta:
        name = "back"

    appendix_content: List[str] = field(
        default_factory=list,
        metadata={
            "name": "appendixContent",
            "type": "Element",
        }
    )
    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    chap_content: List[str] = field(
        default_factory=list,
        metadata={
            "name": "chapContent",
            "type": "Element",
        }
    )


@dataclass
class Body:
    class Meta:
        name = "body"

    appendix_content: List[str] = field(
        default_factory=list,
        metadata={
            "name": "appendixContent",
            "type": "Element",
        }
    )
    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    chap_content: List[str] = field(
        default_factory=list,
        metadata={
            "name": "chapContent",
            "type": "Element",
        }
    )


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    back: Optional[Back] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
