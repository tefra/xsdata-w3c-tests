from output.models.sun_data.ctype.p_substitutions.p_substitutions00101m.p_substitutions00101m_xsd.p_substitutions00101m import B
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.models.datatype import XmlDate


obj = DerivedElement(
    qname='{pSubstitutions}e',
    value=B(
        c=[
            1,
        ],
        d=XmlDate(2002, 4, 15)
    ),
    type='{pSubstitutions}B'
)
