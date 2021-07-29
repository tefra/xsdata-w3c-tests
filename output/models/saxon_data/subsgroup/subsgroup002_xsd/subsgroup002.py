from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AppendixContent:
    class Meta:
        name = "appendixContent"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ChapContent:
    class Meta:
        name = "chapContent"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Content:
    class Meta:
        name = "content"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
    content: List[Content] = field(
        default_factory=list,
        metadata={
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
    content: List[Content] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
