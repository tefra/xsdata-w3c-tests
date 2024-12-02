from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-2-NS"


@dataclass
class NistschemaSvIvListBooleanPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-2"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[1]{1} true [1]{1} false [1]{1} false",
            "tokens": True,
        },
    )
