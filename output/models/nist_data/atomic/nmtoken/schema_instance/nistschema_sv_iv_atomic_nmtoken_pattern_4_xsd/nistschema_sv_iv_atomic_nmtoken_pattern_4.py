from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{33}",
        }
    )
