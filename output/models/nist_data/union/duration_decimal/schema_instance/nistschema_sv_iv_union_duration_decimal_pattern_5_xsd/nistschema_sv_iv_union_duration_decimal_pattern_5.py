from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-duration-decimal-pattern-5-NS"


@dataclass
class NistschemaSvIvUnionDurationDecimalPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-duration-decimal-pattern-5"
        namespace = "NISTSchema-SV-IV-union-duration-decimal-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\-\d{1}",
        },
    )
