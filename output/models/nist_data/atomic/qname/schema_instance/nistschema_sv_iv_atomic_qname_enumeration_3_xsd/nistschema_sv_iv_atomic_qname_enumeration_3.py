from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"


class NistschemaSvIvAtomicQnameEnumeration3Type(Enum):
    """
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_IAND_MUST_EFFECTI:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_LANGUAGES_AND_TRANSFORMING_TECHNOLOGIES_IS_IMPA:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_VCOMPUTING_OF_AS:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_TTHE_WITH:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_TON_AND_ITS_T:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_XSTANDARD_FILE_USE_EA:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_YINVOLVED_E_EFFOR:
    """
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_IAND_MUST_EFFECTI = QName("http://www.nist.gov/xsdNS", "iand-must.effecti")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_LANGUAGES_AND_TRANSFORMING_TECHNOLOGIES_IS_IMPA = QName("NISTSchema-SV-IV-atomic-QName-enumeration-3-NS", "_languages-and-transforming.technologies.is_impa")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES = QName("NISTSchema-SV-IV-atomic-QName-enumeration-3-NS", "kdomains-as.automatic-academia_work-ensure_tes")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_VCOMPUTING_OF_AS = QName("http://www.nist.gov/xsdNS", "vcomputing.of-as_")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_TTHE_WITH = QName("http://www.nist.gov/xsdNS", "tthe.with-")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_TON_AND_ITS_T = QName("NISTSchema-SV-IV-atomic-QName-enumeration-3-NS", "ton.and_its.t")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_XSTANDARD_FILE_USE_EA = QName("NISTSchema-SV-IV-atomic-QName-enumeration-3-NS", "xstandard-file_use-ea")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_3_NS_YINVOLVED_E_EFFOR = QName("NISTSchema-SV-IV-atomic-QName-enumeration-3-NS", "yinvolved.e-effor")


@dataclass
class TypeLanguagesAndTransformingTechnologiesIsImpa:
    """
    :ivar value:
    """
    class Meta:
        name = "_languages-and-transforming.technologies.is_impa"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class KdomainsAsAutomaticAcademiaWorkEnsureTes:
    """
    :ivar value:
    """
    class Meta:
        name = "kdomains-as.automatic-academia_work-ensure_tes"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TonAndItsT:
    """
    :ivar value:
    """
    class Meta:
        name = "ton.and_its.t"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XstandardFileUseEa:
    """
    :ivar value:
    """
    class Meta:
        name = "xstandard-file_use-ea"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class YinvolvedEEffor:
    """
    :ivar value:
    """
    class Meta:
        name = "yinvolved.e-effor"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
