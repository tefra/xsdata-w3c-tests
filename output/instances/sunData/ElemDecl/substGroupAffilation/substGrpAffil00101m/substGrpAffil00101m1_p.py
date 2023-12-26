from output.models.sun_data.elem_decl.subst_group_affilation.subst_grp_affil00101m.subst_grp_affil00101m_xsd.subst_grp_affil00101m import Book
from output.models.sun_data.elem_decl.subst_group_affilation.subst_grp_affil00101m.subst_grp_affil00101m_xsd.subst_grp_affil00101m import BookStore
from output.models.sun_data.elem_decl.subst_group_affilation.subst_grp_affil00101m.subst_grp_affil00101m_xsd.subst_grp_affil00101m import Magazine
from xsdata.models.datatype import XmlPeriod


obj = BookStore(
    magazine_or_book=[
        Book(
            title='The Old Man and the Sea',
            author=[
                'Ernest Hemingway',
            ]
        ),
        Magazine(
            title="Men's Health",
            date=XmlPeriod("2002")
        ),
    ]
)
