from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-length-2-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-length-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-length-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 11,
        },
    )
