from dataclasses import dataclass, field

__NAMESPACE__ = "compositor"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "compositor"
