from dataclasses import dataclass, field

__NAMESPACE__ = "ST_targetNS"


@dataclass
class Test:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1|2",
        },
    )
