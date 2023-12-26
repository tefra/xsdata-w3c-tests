from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-3-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-3"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\-\d{10}\.\d{3}",
        },
    )
