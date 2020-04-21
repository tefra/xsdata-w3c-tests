from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"


class NistschemaSvIvAtomicQnameEnumeration1Type(Enum):
    """
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_CENGINE:
    :cvar QNAME_HTTP_WWW_NIST_GOV_XSD_NS_PVOCABULARIES_ANY_PROMI:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_FOR_BE_PROVIDE_RELAT:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_THOSE_TO_BUSINESS_AND_ISSUES_DATA_FOR:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_RINFLUENCE_CREATE_INFORMATION_REVIEWED_AS_RE:
    :cvar QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_WSPECIFICATIONS_EMERGING_THAT_AND_IS:
    """
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_CENGINE = QName("http://www.nist.gov/xsdNS", "cengine")
    QNAME_HTTP_WWW_NIST_GOV_XSD_NS_PVOCABULARIES_ANY_PROMI = QName("http://www.nist.gov/xsdNS", "pvocabularies_any-promi")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_FOR_BE_PROVIDE_RELAT = QName("NISTSchema-SV-IV-atomic-QName-enumeration-1-NS", "_for.be_provide_relat")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_THOSE_TO_BUSINESS_AND_ISSUES_DATA_FOR = QName("NISTSchema-SV-IV-atomic-QName-enumeration-1-NS", "_those-to_business_and.issues-data.for")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_RINFLUENCE_CREATE_INFORMATION_REVIEWED_AS_RE = QName("NISTSchema-SV-IV-atomic-QName-enumeration-1-NS", "rinfluence-create_information_reviewed_as.re")
    QNAME_NISTSCHEMA_SV_IV_ATOMIC_QNAME_ENUMERATION_1_NS_WSPECIFICATIONS_EMERGING_THAT_AND_IS = QName("NISTSchema-SV-IV-atomic-QName-enumeration-1-NS", "wspecifications.emerging.that_and.is_")


@dataclass
class TypeForBeProvideRelat:
    """
    :ivar value:
    """
    class Meta:
        name = "_for.be_provide_relat"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeThoseToBusinessAndIssuesDataFor:
    """
    :ivar value:
    """
    class Meta:
        name = "_those-to_business_and.issues-data.for"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RinfluenceCreateInformationReviewedAsRe:
    """
    :ivar value:
    """
    class Meta:
        name = "rinfluence-create_information_reviewed_as.re"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class WspecificationsEmergingThatAndIs:
    """
    :ivar value:
    """
    class Meta:
        name = "wspecifications.emerging.that_and.is_"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
