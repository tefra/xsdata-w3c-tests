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
        }
    )
    language: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    name: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    ncname: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    id: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    idref: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    idrefs: List[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        }
    )
    nmtoken: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        }
    )
    nmtokens: List[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        }
    )
