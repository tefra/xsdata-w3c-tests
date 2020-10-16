from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AppendixContent:
    """
    :ivar value:
    """
    class Meta:
        name = "appendixContent"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ChapContent:
    """
    :ivar value:
    """
    class Meta:
        name = "chapContent"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Content:
    """
    :ivar any_element:
    """
    class Meta:
        name = "content"

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
    """
    :ivar value:
    """
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
    """
    :ivar appendix_content:
    :ivar para:
    :ivar chap_content:
    :ivar content:
    """
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
    """
    :ivar appendix_content:
    :ivar para:
    :ivar chap_content:
    :ivar content:
    """
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
    """
    :ivar body:
    :ivar back:
    """
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
