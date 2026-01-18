from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"


class NistschemaSvIvAtomicIdEnumeration1Type(Enum):
    ITEMPLATES_RESOURCE = "itemplates.resource_"
    HORGANIZ = "horganiz"
    WORK_OF_IS_DOCUMENTS_RELATIONSHIPS_OF_AT_OBJECT = (
        "_work-of-is-documents_relationships-of_at.object"
    )
    MACCOMPLISH_VERSIONS_CARE_DEFINE_AND_PR = (
        "maccomplish.versions.care.define-and.pr"
    )
    DALLOW_SUCCESS_OF_DEVICES_ENOUGH_THE_RETRIEVE = (
        "dallow-success-of_devices_enough_the.retrieve"
    )
    MANUFACTURERS_INFORMATION_WORLD_TH = "_manufacturers_information.world_th"
    HDOCUMENTS_IMPACT = "hdocuments-impact"


@dataclass(kw_only=True)
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIdEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-1-NS"

    value: NistschemaSvIvAtomicIdEnumeration1Type = field(
        metadata={
            "required": True,
        }
    )
