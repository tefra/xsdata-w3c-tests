from dataclasses import dataclass, field

__NAMESPACE__ = "ST_final"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"1|2",
            "tokens": True,
        },
    )
