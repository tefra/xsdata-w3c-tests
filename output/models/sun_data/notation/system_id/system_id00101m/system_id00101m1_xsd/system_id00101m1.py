from dataclasses import dataclass, field

__NAMESPACE__ = "systemId"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "systemId"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
