from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-pattern-4-NS"


@dataclass
class NistschemaSvIvListNmtokenPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-pattern-4"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{35} \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}",
            "tokens": True,
        },
    )
