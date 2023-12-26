from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,6}\.){1,2}\c{3}",
        },
    )
