from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLanguagePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-language-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"([a-zA-Z]{2}|[iI]-[a-zA-Z]+|[xX]-[a-zA-Z]{1,8})(-[a-zA-Z]{3})*",
        },
    )
