from dataclasses import dataclass, field
from typing import List, Optional


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
    :ivar para:
    :ivar appendix_content:
    """
    class Meta:
        name = "back"

    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    appendix_content: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="appendixContent",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Body:
    """
    :ivar para:
    :ivar chap_content:
    """
    class Meta:
        name = "body"

    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    chap_content: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="chapContent",
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
