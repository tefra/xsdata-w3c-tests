from dataclasses import dataclass, field


@dataclass
class X:
    class Meta:
        name = "x"

    value: str = field(default="")
