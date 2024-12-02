from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[str] = field(
        init=False,
        default_factory=lambda: [
            "abcdefab",
        ],
        metadata={
            "tokens": True,
        },
    )
