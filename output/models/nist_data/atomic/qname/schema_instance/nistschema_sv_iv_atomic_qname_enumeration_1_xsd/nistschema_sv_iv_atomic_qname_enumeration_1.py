from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-1-NS"


class NistschemaSvIvAtomicQnameEnumeration1Type(Enum):
    """
    :cvar CENGINE:
    :cvar FOR_BE_PROVIDE_RELAT:
    :cvar RINFLUENCE_CREATE_INFORMATION_REVIEWED_AS_RE:
    :cvar THOSE_TO_BUSINESS_AND_ISSUES_DATA_FOR:
    :cvar WSPECIFICATIONS_EMERGING_THAT_AND_IS:
    :cvar ALSO_TO_T_PVOCABULARIES_ANY_PROMI:
    """
    CENGINE = QName("{http://www.nist.gov/xsdNS}cengine")
    FOR_BE_PROVIDE_RELAT = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-1-NS}_for.be_provide_relat")
    RINFLUENCE_CREATE_INFORMATION_REVIEWED_AS_RE = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-1-NS}rinfluence-create_information_reviewed_as.re")
    THOSE_TO_BUSINESS_AND_ISSUES_DATA_FOR = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-1-NS}_those-to_business_and.issues-data.for")
    WSPECIFICATIONS_EMERGING_THAT_AND_IS = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-1-NS}wspecifications.emerging.that_and.is_")
    ALSO_TO_T_PVOCABULARIES_ANY_PROMI = QName("{http://www.nist.gov/xsdNS}pvocabularies_any-promi")


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
