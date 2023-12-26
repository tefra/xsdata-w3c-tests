from dataclasses import dataclass, field

__NAMESPACE__ = "importNS"


@dataclass
class Iid:
    class Meta:
        name = "iid"
        namespace = "importNS"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
