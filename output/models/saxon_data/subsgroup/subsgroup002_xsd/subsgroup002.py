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
        metadata=dict(
            required=True
        )
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
        metadata=dict(
            required=True
        )
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
        metadata=dict(
            required=True
        )
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

    appendix_content: List[AppendixContent] = field(
        default_factory=list,
        metadata=dict(
            name="appendixContent",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=18446744073709551614
        )
    )
    chap_content: List[ChapContent] = field(
        default_factory=list,
        metadata=dict(
            name="chapContent",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
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

    appendix_content: List[AppendixContent] = field(
        default_factory=list,
        metadata=dict(
            name="appendixContent",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=18446744073709551614
        )
    )
    chap_content: List[ChapContent] = field(
        default_factory=list,
        metadata=dict(
            name="chapContent",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
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
        metadata=dict(
            type="Element",
            required=True
        )
    )
    back: Optional[Back] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
