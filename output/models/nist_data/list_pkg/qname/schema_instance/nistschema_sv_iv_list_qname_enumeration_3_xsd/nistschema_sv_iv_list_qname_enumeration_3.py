from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"


class NistschemaSvIvListQnameEnumeration3Type(Enum):
    """
    :cvar VALUE_ANA_MAINTAINE_ENSURE_AND_BTHE_A_A_CROSS_OVER_THE_POSSIB_QA_FAND_SOFTWARE_IN_AVAILABLE_SOFTWARE_CONFORMANCE_MA_SNEED_CREATING_THE_A_IFOR_PARTNERS_FOR_IS_AND_UNBIA_YSPECIFICATIONS_AS_PERVASIVE_WEB_MFROM_INTERACT_QDESIGN_AND_SOFTWARE_AND_AND_THE_WAS:
    :cvar VALUE_B_UCOMPLETE_OTHER_C_NAN_OVOCABULARY_DIFFERENT_CW_BA_WL_MBEING_ANY_AS_ROBUST_DE_TPARTICULAR_TOOLS_ENTIRE_REVIEW_TECHNOLOGIES_TO_TO_TO_ALRE_SBY_DDEVELOPMENT_PROC_HLANDSCAPE_OF_INCLUDED_ISSUES_VOICE_JAPPLICATIONS_AS_ECONFORMANCE_KNOWN_BUSINESS_LED_WIL:
    :cvar VALUE_WILL_REPOSITORY_EFFECTIVELY_OBJECT_BUILD_WIRELESS_METROL_IENTIRE_CROSS_BTHESE_PERVASIVE_DATABASE_SPECIFICATIONS_WITH_IA_MAKE_OF_PROCESS_WOULD_IN_LAUNCHING_OF_THE_OBJECT_TRANSAC_XAN_WITH_BU_VELIMIN_AREGARD_TEST_STANDARDIZATION_KNOWN_OF_WITH_AS_NEED_WITH_RDEPENDS_A_QON_FOR_RESPECT_FILTER_XHEALTH_BLOCKS_MEANS_MATCH_AD_FOR:
    :cvar JAPPLICATIONS_AS_ECONFORMANCE_KNOWN_BUSINESS_LED_WIL_SC_QCOMPUTER_LED_AND_INTEROPERABILITY_HAS_TH_FILE_FILTER_A_REVIEWED_THOSE_CREATION_WELL_FOR_ATO_BENEFITS_OPRECISE_RARE_FIRST_EARLY_THE_VISIBLY_TO_COM_NEW_RELATED_INCLUDE_UPERVASIVE_SUPPLY_AND_D_TO_IN_THE_VIRTUALL_JBE_RECOMMENDING_ABILITY_STANDARDIZATION_TO_THE_TO_USED_AND_YINDUSTRY_THE_BFOR_NEW_OF_EXCHANG:
    :cvar QDESIGN_AND_SOFTWARE_AND_AND_THE_WAS_THEM_SEMANTICS_PROBLEMS_VIRTUALLY_WIDE_THE_TOOLS_TESTI_XAND_RETRIEVE_STAN_WIS_N_COMPETENCE_COMMERCE_SERIES_OF_C_REAR_VFOR_BE_COMPUTING_AAND_PROTOTYPES_WEB_WORK_CONTRIBUTE_HAS_TH_B_UCOMPLETE_OTHER_C:
    :cvar QON_FOR_RESPECT_FILTER_XHEALTH_BLOCKS_MEANS_MATCH_AD_FOR_WW_CO_BBY_THE_THESE_TEST_BY_AND_H_IWEB_IRECOGNITION_A_S_OAND_TDESKTOP_TO_REPOSITORY_AS_OF_THAT_THE_ARE_KNOWN_PROBLEMS_OF_G_MS_HPE:
    :cvar YINDUSTRY_THE_BFOR_NEW_OF_EXCHANG_RALSO_TO_LIBRARIES_PR_J_CORRECTNESS_OF_INTEROPERABILITY_BROWSERS_OF_NETWORKS_AS_A_I_ISTA_XWELL_CHALLENGE_WILL_REPOSITORY_EFFECTIVELY_OBJECT_BUILD_WIRELESS_METROL:
    """
    VALUE_ANA_MAINTAINE_ENSURE_AND_BTHE_A_A_CROSS_OVER_THE_POSSIB_QA_FAND_SOFTWARE_IN_AVAILABLE_SOFTWARE_CONFORMANCE_MA_SNEED_CREATING_THE_A_IFOR_PARTNERS_FOR_IS_AND_UNBIA_YSPECIFICATIONS_AS_PERVASIVE_WEB_MFROM_INTERACT_QDESIGN_AND_SOFTWARE_AND_AND_THE_WAS = "_ana:_maintaine _ensure-and:bthe_a-a.cross-over-the-possib qa:fand-software_in.available_software-conformance. _ma:sneed-creating.the-a ifor-partners-for.is_and.unbia yspecifications-as.pervasive-web- mfrom.interact qdesign.and.software-and_and.the_was_"
    VALUE_B_UCOMPLETE_OTHER_C_NAN_OVOCABULARY_DIFFERENT_CW_BA_WL_MBEING_ANY_AS_ROBUST_DE_TPARTICULAR_TOOLS_ENTIRE_REVIEW_TECHNOLOGIES_TO_TO_TO_ALRE_SBY_DDEVELOPMENT_PROC_HLANDSCAPE_OF_INCLUDED_ISSUES_VOICE_JAPPLICATIONS_AS_ECONFORMANCE_KNOWN_BUSINESS_LED_WIL = "_b:ucomplete_other.c nan ovocabulary.different_ cw:ba wl:mbeing-any.as-robust-de tparticular-tools.entire.review-technologies_to_to_to-alre sby.:ddevelopment_proc hlandscape_of-included_issues-voice japplications-as:econformance-known-business-led_wil"
    VALUE_WILL_REPOSITORY_EFFECTIVELY_OBJECT_BUILD_WIRELESS_METROL_IENTIRE_CROSS_BTHESE_PERVASIVE_DATABASE_SPECIFICATIONS_WITH_IA_MAKE_OF_PROCESS_WOULD_IN_LAUNCHING_OF_THE_OBJECT_TRANSAC_XAN_WITH_BU_VELIMIN_AREGARD_TEST_STANDARDIZATION_KNOWN_OF_WITH_AS_NEED_WITH_RDEPENDS_A_QON_FOR_RESPECT_FILTER_XHEALTH_BLOCKS_MEANS_MATCH_AD_FOR = "_will.repository_effectively-object-build-wireless-metrol ientire.cross:bthese.pervasive_database_specifications-with. ia-make_of.process-would-in-launching-of-the_object.transac xan_with-bu velimin:aregard-test.standardization-known-of-with_as_need.with rdepends_a qon_for.respect_filter-:xhealth-blocks.means.match-ad_for"
    JAPPLICATIONS_AS_ECONFORMANCE_KNOWN_BUSINESS_LED_WIL_SC_QCOMPUTER_LED_AND_INTEROPERABILITY_HAS_TH_FILE_FILTER_A_REVIEWED_THOSE_CREATION_WELL_FOR_ATO_BENEFITS_OPRECISE_RARE_FIRST_EARLY_THE_VISIBLY_TO_COM_NEW_RELATED_INCLUDE_UPERVASIVE_SUPPLY_AND_D_TO_IN_THE_VIRTUALL_JBE_RECOMMENDING_ABILITY_STANDARDIZATION_TO_THE_TO_USED_AND_YINDUSTRY_THE_BFOR_NEW_OF_EXCHANG = "japplications-as:econformance-known-business-led_wil sc:qcomputer_led.and.interoperability-has-th _file-filter-a_reviewed.those.creation_well-for ato.benefits oprecise_:rare.first-early-the_visibly.to_com _new-related-include:upervasive.supply-and-d _to_in_the-virtuall jbe_recommending-ability.standardization-to_the_to-used_and yindustry.the:bfor_new.of-exchang"
    QDESIGN_AND_SOFTWARE_AND_AND_THE_WAS_THEM_SEMANTICS_PROBLEMS_VIRTUALLY_WIDE_THE_TOOLS_TESTI_XAND_RETRIEVE_STAN_WIS_N_COMPETENCE_COMMERCE_SERIES_OF_C_REAR_VFOR_BE_COMPUTING_AAND_PROTOTYPES_WEB_WORK_CONTRIBUTE_HAS_TH_B_UCOMPLETE_OTHER_C = "qdesign.and.software-and_and.the_was_ _them.semantics_problems.virtually.wide_the.tools_testi xand.retrieve-stan wis.n _competence-commerce.series_of.c rear:vfor-be-computing- aand-prototypes-web.work.contribute.has.th _b:ucomplete_other.c"
    QON_FOR_RESPECT_FILTER_XHEALTH_BLOCKS_MEANS_MATCH_AD_FOR_WW_CO_BBY_THE_THESE_TEST_BY_AND_H_IWEB_IRECOGNITION_A_S_OAND_TDESKTOP_TO_REPOSITORY_AS_OF_THAT_THE_ARE_KNOWN_PROBLEMS_OF_G_MS_HPE = "qon_for.respect_filter-:xhealth-blocks.means.match-ad_for ww:_co bby.the_these_test.by-and-h iweb_:irecognition-a _s:oand- tdesktop.to-repository_as-of_that-the-are.known.problems-of.g ms:hpe"
    YINDUSTRY_THE_BFOR_NEW_OF_EXCHANG_RALSO_TO_LIBRARIES_PR_J_CORRECTNESS_OF_INTEROPERABILITY_BROWSERS_OF_NETWORKS_AS_A_I_ISTA_XWELL_CHALLENGE_WILL_REPOSITORY_EFFECTIVELY_OBJECT_BUILD_WIRELESS_METROL = "yindustry.the:bfor_new.of-exchang ralso_to.libraries-pr j _correctness_of-interoperability-browsers_of_networks_as_a i:ista xwell-challenge _will.repository_effectively-object-build-wireless-metrol"


@dataclass
class TypeCompetenceCommerceSeriesOfC:
    """
    :ivar value:
    """
    class Meta:
        name = "_competence-commerce.series_of.c"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeCorrectnessOfInteroperabilityBrowsersOfNetworksAsA:
    """
    :ivar value:
    """
    class Meta:
        name = "_correctness_of-interoperability-browsers_of_networks_as_a"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeFileFilterAReviewedThoseCreationWellFor:
    """
    :ivar value:
    """
    class Meta:
        name = "_file-filter-a_reviewed.those.creation_well-for"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeThemSemanticsProblemsVirtuallyWideTheToolsTesti:
    """
    :ivar value:
    """
    class Meta:
        name = "_them.semantics_problems.virtually.wide_the.tools_testi"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeToInTheVirtuall:
    """
    :ivar value:
    """
    class Meta:
        name = "_to_in_the-virtuall"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeWillRepositoryEffectivelyObjectBuildWirelessMetrol:
    """
    :ivar value:
    """
    class Meta:
        name = "_will.repository_effectively-object-build-wireless-metrol"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class AandPrototypesWebWorkContributeHasTh:
    """
    :ivar value:
    """
    class Meta:
        name = "aand-prototypes-web.work.contribute.has.th"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class AtoBenefits:
    """
    :ivar value:
    """
    class Meta:
        name = "ato.benefits"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class BbyTheTheseTestByAndH:
    """
    :ivar value:
    """
    class Meta:
        name = "bby.the_these_test.by-and-h"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class HlandscapeOfIncludedIssuesVoice:
    """
    :ivar value:
    """
    class Meta:
        name = "hlandscape_of-included_issues-voice"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IaMakeOfProcessWouldInLaunchingOfTheObjectTransac:
    """
    :ivar value:
    """
    class Meta:
        name = "ia-make_of.process-would-in-launching-of-the_object.transac"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IforPartnersForIsAndUnbia:
    """
    :ivar value:
    """
    class Meta:
        name = "ifor-partners-for.is_and.unbia"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class J:
    """
    :ivar value:
    """
    class Meta:
        name = "j"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class JbeRecommendingAbilityStandardizationToTheToUsedAnd:
    """
    :ivar value:
    """
    class Meta:
        name = "jbe_recommending-ability.standardization-to_the_to-used_and"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MfromInteract:
    """
    :ivar value:
    """
    class Meta:
        name = "mfrom.interact"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Nan:
    """
    :ivar value:
    """
    class Meta:
        name = "nan"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OvocabularyDifferent:
    """
    :ivar value:
    """
    class Meta:
        name = "ovocabulary.different_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class QdesignAndSoftwareAndAndTheWas:
    """
    :ivar value:
    """
    class Meta:
        name = "qdesign.and.software-and_and.the_was_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RalsoToLibrariesPr:
    """
    :ivar value:
    """
    class Meta:
        name = "ralso_to.libraries-pr"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RdependsA:
    """
    :ivar value:
    """
    class Meta:
        name = "rdepends_a"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TdesktopToRepositoryAsOfThatTheAreKnownProblemsOfG:
    """
    :ivar value:
    """
    class Meta:
        name = "tdesktop.to-repository_as-of_that-the-are.known.problems-of.g"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TparticularToolsEntireReviewTechnologiesToToToAlre:
    """
    :ivar value:
    """
    class Meta:
        name = "tparticular-tools.entire.review-technologies_to_to_to-alre"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class WisN:
    """
    :ivar value:
    """
    class Meta:
        name = "wis.n"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XanWithBu:
    """
    :ivar value:
    """
    class Meta:
        name = "xan_with-bu"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XandRetrieveStan:
    """
    :ivar value:
    """
    class Meta:
        name = "xand.retrieve-stan"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XwellChallenge:
    """
    :ivar value:
    """
    class Meta:
        name = "xwell-challenge"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class YspecificationsAsPervasiveWeb:
    """
    :ivar value:
    """
    class Meta:
        name = "yspecifications-as.pervasive-web-"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvListQnameEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-3-NS"

    value: Optional[NistschemaSvIvListQnameEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )