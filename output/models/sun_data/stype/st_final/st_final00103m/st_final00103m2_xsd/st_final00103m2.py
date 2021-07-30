from dataclasses import dataclass, field

__NAMESPACE__ = "ST_final"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1",
        }
    )
