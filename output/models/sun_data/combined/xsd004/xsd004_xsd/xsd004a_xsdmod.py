from dataclasses import dataclass, field

__NAMESPACE__ = "bar"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "bar"

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
        namespace = "bar"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "bar"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
