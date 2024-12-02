from dataclasses import dataclass, field


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
    idrefs: list[str] = field(
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
    nmtokens: list[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
