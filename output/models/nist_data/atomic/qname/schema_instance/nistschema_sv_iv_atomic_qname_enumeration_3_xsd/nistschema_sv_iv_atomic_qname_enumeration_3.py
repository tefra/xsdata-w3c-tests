from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"


class NistschemaSvIvAtomicQnameEnumeration3Type(Enum):
    KDOMAINS_AS_AUTOMATIC_ACADEMIA_WORK_ENSURE_TES = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-3-NS}kdomains-as.automatic-academia_work-ensure_tes")
    LFINE_D_VCOMPUTING_OF_AS = QName("{http://www.nist.gov/xsdNS}vcomputing.of-as_")
    LANGUAGES_AND_TRANSFORMING_TECHNOLOGIES_IS_IMPA = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-3-NS}_languages-and-transforming.technologies.is_impa")
    XSTANDARD_FILE_USE_EA = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-3-NS}xstandard-file_use-ea")
    LAN_IAND_MUST_EFFECTI = QName("{http://www.nist.gov/xsdNS}iand-must.effecti")
    TON_AND_ITS_T = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-3-NS}ton.and_its.t")
    YINVOLVED_E_EFFOR = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-3-NS}yinvolved.e-effor")
    Q_TTHE_WITH = QName("{http://www.nist.gov/xsdNS}tthe.with-")


@dataclass
class LanguagesAndTransformingTechnologiesIsImpa:
    class Meta:
        name = "_languages-and-transforming.technologies.is_impa"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class KdomainsAsAutomaticAcademiaWorkEnsureTes:
    class Meta:
        name = "kdomains-as.automatic-academia_work-ensure_tes"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TonAndItsT:
    class Meta:
        name = "ton.and_its.t"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class XstandardFileUseEa:
    class Meta:
        name = "xstandard-file_use-ea"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class YinvolvedEEffor:
    class Meta:
        name = "yinvolved.e-effor"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
