from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-length-5-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-length-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-length-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 63,
        }
    )
