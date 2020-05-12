from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2-NS"


class NistschemaSvIvUnionAnyUriFloatEnumeration2Type(Enum):
    """
    :cvar FTP_MATCHDISPLA_NISTOURTHE_SFILEAK_ORG:
    :cvar NEWS_AR_ORG:
    :cvar NEWS_THEANDINDUS_RYESTABLIS_PERMITTING_SOFIN_ORG:
    :cvar VALUE_1_5462377_E_25:
    :cvar VALUE_1_7554835_E_36:
    """
    FTP_MATCHDISPLA_NISTOURTHE_SFILEAK_ORG = "ftp://matchdispla.NISTourthe.sfileak.org"
    NEWS_AR_ORG = "news://ar.org"
    NEWS_THEANDINDUS_RYESTABLIS_PERMITTING_SOFIN_ORG = "news://theandindus.ryestablis.permitting.sofin.org"
    VALUE_1_5462377_E_25 = "1.5462377E-25"
    VALUE_1_7554835_E_36 = "1.7554835E-36"


@dataclass
class NistschemaSvIvUnionAnyUriFloatEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-enumeration-2-NS"

    value: Optional[NistschemaSvIvUnionAnyUriFloatEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
