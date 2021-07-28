from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AppendixContent:
    class Meta:
        name = "appendixContent"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class ChapContent:
    class Meta:
        name = "chapContent"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Para:
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Back:
    class Meta:
        name = "back"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    appendix_content: List[AppendixContent] = field(
        default_factory=list,
        metadata={
            "name": "appendixContent",
            "type": "Element",
        }
    )


@dataclass
class Body:
    class Meta:
        name = "body"

    para: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    chap_content: List[ChapContent] = field(
        default_factory=list,
        metadata={
            "name": "chapContent",
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
