from dataclasses import dataclass, field

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1*",
        },
    )
