from dataclasses import dataclass, field

__NAMESPACE__ = "zot"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "zot"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "zot"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "zot"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
