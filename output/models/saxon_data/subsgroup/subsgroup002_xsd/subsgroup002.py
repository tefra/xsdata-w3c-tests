from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Back:
    class Meta:
        name = "back"

    appendix_content_or_para_or_chap_content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "appendixContent",
                    "type": str,
                },
                {
                    "name": "para",
                    "type": str,
                },
                {
                    "name": "chapContent",
                    "type": str,
                },
            ),
        }
    )


@dataclass
class Body:
    class Meta:
        name = "body"

    appendix_content_or_para_or_chap_content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "appendixContent",
                    "type": str,
                },
                {
                    "name": "para",
                    "type": str,
                },
                {
                    "name": "chapContent",
                    "type": str,
                },
            ),
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
