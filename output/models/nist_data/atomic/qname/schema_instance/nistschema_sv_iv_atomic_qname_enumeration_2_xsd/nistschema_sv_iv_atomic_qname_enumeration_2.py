from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-2-NS"


class NistschemaSvIvAtomicQnameEnumeration2Type(Enum):
    """
    :cvar ALSO_TO_T_PVOCABULARIES_ANY_PROMI:
    :cvar DPERVASIVE_NDEVELOPMENT_BE:
    :cvar AWITH_AND_AS_AND_BY_WORLD_T_CINFORMATION_INFORMATION_LANGUA:
    :cvar NCREATE:
    :cvar C_XSOLUTIONS_FILTER_REVIEWED_LED_ALLOW_BY_INDUSTRY_PR:
    :cvar A_VREACH_S:
    :cvar KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES:
    """
    ALSO_TO_T_PVOCABULARIES_ANY_PROMI = QName("{http://www.nist.gov/xsdNS}pvocabularies_any-promi")
    DPERVASIVE_NDEVELOPMENT_BE = QName("{http://www.nist.gov/xsdNS}ndevelopment_be")
    AWITH_AND_AS_AND_BY_WORLD_T_CINFORMATION_INFORMATION_LANGUA = QName("{http://www.nist.gov/xsdNS}cinformation-information.langua")
    NCREATE = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-2-NS}ncreate")
    C_XSOLUTIONS_FILTER_REVIEWED_LED_ALLOW_BY_INDUSTRY_PR = QName("{http://www.nist.gov/xsdNS}xsolutions.filter_reviewed-led-allow_by_industry_pr")
    A_VREACH_S = QName("{http://www.nist.gov/xsdNS}vreach-s")
    KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-2-NS}kdomains-as.automatic-academia_work-ensure_tes")


@dataclass
class KdomainsAsAutomaticAcademiaWorkEnsureTes:
    """
    :ivar value:
    """
    class Meta:
        name = "kdomains-as.automatic-academia_work-ensure_tes"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Ncreate:
    """
    :ivar value:
    """
    class Meta:
        name = "ncreate"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration2Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
