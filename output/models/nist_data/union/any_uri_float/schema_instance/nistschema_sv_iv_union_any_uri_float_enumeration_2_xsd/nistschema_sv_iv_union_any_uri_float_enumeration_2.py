from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration2Type(Enum):
    NEWS_THEANDINDUS_RYESTABLIS_PERMITTING_SOFIN_ORG = "news://theandindus.ryestablis.permitting.sofin.org"
    VALUE_1_5462377_E_25 = 1.5462377e-25
    NEWS_AR_ORG = "news://ar.org"
    FTP_MATCHDISPLA_NISTOURTHE_SFILEAK_ORG = "ftp://matchdispla.NISTourthe.sfileak.org"
    VALUE_1_7554835_E_36 = 1.7554835e-36


@dataclass
class NistschemaSvIvUnionAnyUriFloatEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionAnyUriFloatEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
