from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-enumeration-2-NS"


class NistschemaSvIvListAnyUriEnumeration2Type(Enum):
    TELNET_WORK_NET_FTP_FTP_PE_GOV_GOPHER_ITSFACILITA_ESAINFORMA_IONINDUSTR_OF_GOV_FTP_FTP_ONE_GOV_HTTP_WWW_VIR_ORG_NEWS_DEFININGCOM_UTEDENOUGH_OMMUNI_GOV_GOPHER_MAI_EDU = (
        "telnet://work.net",
        "ftp://ftp.Pe.gov",
        "gopher://itsfacilita.esainforma.ionindustr.of.gov",
        "ftp://ftp.One.gov",
        "http://www.Vir.org",
        "news://definingcom.utedenough.ommuni.gov",
        "gopher://mai.edu",
    )
    TELNET_FORANDALLNE_TRALDOCUME_TSTHEFILEA_PROPRIATED_VI_COM_FTP_FTP_T_NET_NEWS_MEETINDIC_ORG_FTP_FTP_XSLORGANIZ_EDU_HTTP_TORELATEDRE_PEC_GOV_HTTP_I_COM_HTTP_TOOLSAPPLI_EDU_TELNET_STANDARDSIN_ORPORATEDT_ALREADYSCO_M_ORG = (
        "telnet://forandallne.traldocume.tsthefilea.propriated.vi.com",
        "ftp://ftp.t.net",
        "news://meetindic.org",
        "ftp://ftp.XSLorganiz.edu",
        "http://torelatedre.pec.gov",
        "http://i.com",
        "http://toolsappli.edu",
        "telnet://standardsin.orporatedt.alreadysco.m.org",
    )
    FTP_ASCHALLENGE_RECENT_BUSI_ESSOF_SCHEM_SPERFORMAN_ORG_NEWS_AND_ANTHETHE_NDERAPPLIC_TIONSFACIL_TATE_ORG_TELNET_FORDOCUMENT_BETHEMANIP_LA_ORG_FTP_FTP_REACHTOVERS_ON_EDU_HTTP_WWW_OBJECTIVEAN_THES_ORG_GOPHER_INDUSTRY_ORG_NEWS_REFERENCETH_ANDWIRELES_PRIMARILYR_POS_NET_HTTP_SI_GOV = (
        "ftp://aschallenge.recentBusi.essofSchem.sperforman.org",
        "news://andAnthethe.nderapplic.tionsfacil.tate.org",
        "telnet://fordocument.bethemanip.la.org",
        "ftp://ftp.reachtovers.on.edu",
        "http://www.objectivean.thes.org",
        "gopher://industry.org",
        "news://referenceth.andwireles.primarilyr.pos.net",
        "http://si.gov",
    )
    FTP_WHOTOOLSOBJ_CTWITHSU_COM_FTP_FTP_SUPPLYHELPC_NSORTIUMST_EARECOMPUT_NGW_ORG_FTP_CONSEQUENTL_OFFERBODYT_WOULDTHEPA_TICULARLYA_NET_FTP_FTP_TESTINGDEPE_DSAUTOMATI_ALLYTOOLSC_COM_FTP_FTP_X_EDU_FTP_SOFTWAREEFF_RTESTABLIS_INDIVIDUAL_ASISDEFINE_PPR_GOV_TELNET_SEMANTICS_EX_STSTANDARD_INDUSTR_EDU_HTTP_WWW_ANDBEANDISS_ESFACTSIGN_TURESCOMPU_ING_APORTABL_GOV_FTP_FTP_MADETHE_REFE_ENCEFORFRO_PROMINENT_GOV = (
        "ftp://whotoolsobj.ctwithsu.com",
        "ftp://ftp.supplyhelpc.nsortiumst.earecomput.ngw.org",
        "ftp://Consequentl.offerbodyt.wouldthepa.ticularlya.net",
        "ftp://ftp.testingdepe.dsautomati.allytoolsc.com",
        "ftp://ftp.x.edu",
        "ftp://softwareeff.rtestablis.individual.asisdefine.ppr.gov",
        "telnet://semanticsEX.STStandard.industr.edu",
        "http://www.andbeandiss.esfactsign.turescompu.ingAportabl.gov",
        "ftp://ftp.madetheRefe.enceforfro.prominent.gov",
    )
    FTP_ACHOICESDAT_BASETOMUST_HETOOLSTES_DOMSPEC_EDU_FTP_COORDINATEP_RTNERSHIPS_DVANCEMENT_EFI_EDU_MAILTO_SU_BEOFR_NET_NEWS_F_COM_TELNET_G_COM_FTP_NATUREOFIMP_CTUSEFROMS_CHEFFECTIVE_EDU_FTP_ISSUEST_ORG = (
        "ftp://achoicesdat.basetomust.hetoolstes.DOMspec.edu",
        "ftp://Coordinatep.rtnerships.dvancement.efi.edu",
        "mailto:su@beofr.net",
        "news://f.com",
        "telnet://g.com",
        "ftp://natureofimp.ctusefroms.cheffective.edu",
        "ftp://issuest.org",
    )
    MAILTO_BYWEBINFRAS_HAVESETAPRODUCTINDUSTRYAS_AVOCABUL_ORG_TELNET_DEVELOPINGA_IKE_RECOMME_DATIONSISI_SUESREVO_EDU_HTTP_WWW_R_NET_HTTP_WWW_USERSWORKKN_WN_ORG_TELNET_OFTESTITSAN_OF_ALTHOUGH_ANYUSERSTO_LSFROMWOU_NET_HTTP_WWW_ANDASWIRELE_SBOTHREPOS_TORYANDISF_LTERLANGUAG_NET_HTTP_THEOFYEARSF_RTHEROFARE_FDEVELOPIN_FROMFORDOC_ORG = (
        "mailto:bywebinfras@havesetaproductindustryasAvocabul.org",
        "telnet://developinga.ikeRecomme.dationsisi.suesrevo.edu",
        "http://www.r.net",
        "http://www.usersworkkn.wn.org",
        "telnet://oftestitsan.ofAlthough.anyusersto.lsfromwou.net",
        "http://www.andaswirele.sbothrepos.toryandisf.lterlanguag.net",
        "http://Theofyearsf.rtherofare.fdevelopin.fromfordoc.org",
    )


@dataclass(kw_only=True)
class NistschemaSvIvListAnyUriEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-anyURI-enumeration-2-NS"

    value: NistschemaSvIvListAnyUriEnumeration2Type = field()
