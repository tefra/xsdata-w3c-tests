from dataclasses import dataclass, field


@dataclass
class Message:
    class Meta:
        name = "message"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 25,
        },
    )
