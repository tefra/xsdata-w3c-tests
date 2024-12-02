from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4-NS"


@dataclass
class NistschemaSvIvListNmtokensPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{29} \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}",
            "tokens": True,
        },
    )
