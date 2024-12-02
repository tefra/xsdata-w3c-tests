from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{1} \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}",
            "tokens": True,
        },
    )
