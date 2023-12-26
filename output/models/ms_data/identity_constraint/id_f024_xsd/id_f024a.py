from dataclasses import dataclass, field

__NAMESPACE__ = "importNS"


@dataclass
class R:
    class Meta:
        name = "r"
        namespace = "importNS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
