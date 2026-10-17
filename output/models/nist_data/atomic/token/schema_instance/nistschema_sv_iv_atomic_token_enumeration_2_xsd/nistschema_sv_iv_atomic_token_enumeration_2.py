from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"


class NistschemaSvIvAtomicTokenEnumeration2Type(StrEnum):
    MAINTAINED = "maintained"
    DEVELOP = "Develop"
    NETWORKS = "networks"
    FILE = "file"
    THE = "the"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-token-enumeration-2-NS"

    value: NistschemaSvIvAtomicTokenEnumeration2Type = field()
