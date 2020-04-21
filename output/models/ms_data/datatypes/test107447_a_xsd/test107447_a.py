from dataclasses import dataclass, field


@dataclass
class Root:
    """
    :ivar token:
    :ivar language:
    :ivar name:
    :ivar ncname:
    :ivar id:
    :ivar idref:
    :ivar idrefs:
    :ivar nmtoken:
    :ivar nmtokens:
    """
    class Meta:
        name = "root"

    token: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    language: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    name: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    ncname: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    id: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    idref: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    idrefs: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nmtoken: str = field(
        init=False,
        default=" John    ",
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nmtokens: str = field(
        init=False,
        default="John",
        metadata=dict(
            type="Element",
            required=True
        )
    )
