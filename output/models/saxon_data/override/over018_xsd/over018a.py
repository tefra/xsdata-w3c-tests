from dataclasses import dataclass, field

__NAMESPACE__ = "http://example.com/over018"


@dataclass
class Para:
    class Meta:
        name = "para"
        namespace = "http://example.com/over018"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
