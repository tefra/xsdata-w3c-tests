from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{45} \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}",
            "tokens": True,
        },
    )
