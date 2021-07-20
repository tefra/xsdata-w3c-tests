from dataclasses import dataclass, field

__NAMESPACE__ = "b"


@dataclass
class B1:
    class Meta:
        name = "b1"
        namespace = "b"

    value: str = field(
        default="b1"
    )


@dataclass
class B2:
    class Meta:
        name = "b2"
        namespace = "b"

    value: str = field(
        init=False,
        default="b2"
    )
