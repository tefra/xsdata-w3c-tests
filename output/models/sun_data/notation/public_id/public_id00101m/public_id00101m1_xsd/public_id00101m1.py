from dataclasses import dataclass, field

__NAMESPACE__ = "publicId"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "publicId"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
