from dataclasses import dataclass, field


@dataclass
class Example:
    value: list[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
