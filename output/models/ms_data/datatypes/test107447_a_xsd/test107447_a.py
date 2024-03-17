from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    token: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    language: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ncname: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    idref: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    idrefs: List[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
    nmtoken: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    nmtokens: List[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
