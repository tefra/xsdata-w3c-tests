from dataclasses import dataclass, field

__NAMESPACE__ = "ST_name"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_name"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1|2|3",
        },
    )
