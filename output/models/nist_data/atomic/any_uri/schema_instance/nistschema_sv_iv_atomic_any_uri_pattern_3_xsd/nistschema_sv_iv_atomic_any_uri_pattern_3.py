from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,7}\.){1,4}\c{3}",
        }
    )
