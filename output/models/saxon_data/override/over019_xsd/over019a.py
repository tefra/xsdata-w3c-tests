from dataclasses import dataclass, field

__NAMESPACE__ = "http://example.com/over019"


@dataclass
class Para:
    class Meta:
        name = "para"
        namespace = "http://example.com/over019"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
