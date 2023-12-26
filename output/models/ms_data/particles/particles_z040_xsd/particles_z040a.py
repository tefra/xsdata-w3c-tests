from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class A1:
    class Meta:
        name = "a1"
        namespace = "a"

    value: str = field(
        init=False,
        default="a1",
        metadata={
            "required": True,
        },
    )


@dataclass
class A2:
    class Meta:
        name = "a2"
        namespace = "a"

    value: str = field(
        default="a2",
        metadata={
            "required": True,
        },
    )
