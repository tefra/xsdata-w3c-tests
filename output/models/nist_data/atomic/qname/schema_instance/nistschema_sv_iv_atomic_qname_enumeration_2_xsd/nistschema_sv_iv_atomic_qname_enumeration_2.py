from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-2-NS"


class NistschemaSvIvAtomicQnameEnumeration2Type(Enum):
    """
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_VREACH_S:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_PVOCABULARIES_ANY_PROMI:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_CINFORMATION_INFORMATION_LANGUA:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_XSOLUTIONS_FILTER_REVIEWED_LED_ALLOW_BY_INDUSTRY_PR:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_NDEVELOPMENT_BE:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_2_NS_KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_2_NS_NCREATE:
    """
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_VREACH_S = QName("http://www.nist.gov/xsdNS", "vreach-s")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_PVOCABULARIES_ANY_PROMI = QName("http://www.nist.gov/xsdNS", "pvocabularies_any-promi")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_CINFORMATION_INFORMATION_LANGUA = QName("http://www.nist.gov/xsdNS", "cinformation-information.langua")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_XSOLUTIONS_FILTER_REVIEWED_LED_ALLOW_BY_INDUSTRY_PR = QName("http://www.nist.gov/xsdNS", "xsolutions.filter_reviewed-led-allow_by_industry_pr")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_NDEVELOPMENT_BE = QName("http://www.nist.gov/xsdNS", "ndevelopment_be")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_2_NS_KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES = QName("NISTSchema-SV-IV-atomic-QName-enumeration-2-NS", "kdomains-as.automatic-academia_work-ensure_tes")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_2_NS_NCREATE = QName("NISTSchema-SV-IV-atomic-QName-enumeration-2-NS", "ncreate")


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