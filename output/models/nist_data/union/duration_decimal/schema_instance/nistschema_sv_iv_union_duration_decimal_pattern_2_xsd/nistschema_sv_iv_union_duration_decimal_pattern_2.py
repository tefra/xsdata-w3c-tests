from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-2-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-2"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{9}",
        }
    )
