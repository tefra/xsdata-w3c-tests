from dataclasses import dataclass, field

__NAMESPACE__ = "ST_baseTD"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_baseTD"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
