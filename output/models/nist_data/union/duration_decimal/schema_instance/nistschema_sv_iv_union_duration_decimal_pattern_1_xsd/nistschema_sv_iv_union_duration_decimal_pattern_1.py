from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-1"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\-\.\d{5}",
        }
    )
