from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass
class BE1:
    class Meta:
        name = "b-e1"
        namespace = "ns-a"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 4,
        },
    )
