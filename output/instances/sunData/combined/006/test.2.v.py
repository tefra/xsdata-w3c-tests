from output.models.sun_data.combined.pkg_006.test_xsd.test import De
from output.models.sun_data.combined.pkg_006.test_xsd.test import Dee
from output.models.sun_data.combined.pkg_006.test_xsd.test import Der
from output.models.sun_data.combined.pkg_006.test_xsd.test import Dr
from output.models.sun_data.combined.pkg_006.test_xsd.test import Dre
from output.models.sun_data.combined.pkg_006.test_xsd.test import Drr
from output.models.sun_data.combined.pkg_006.test_xsd.test import EB
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDe
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDee
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDer
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDr
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDre
from output.models.sun_data.combined.pkg_006.test_xsd.test import EDrr
from output.models.sun_data.combined.pkg_006.test_xsd.test import Empty
from output.models.sun_data.combined.pkg_006.test_xsd.test import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        EB(
            foo=Empty(

            )
        ),
        EB(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname="{foo}eB",
            value=Dr(
                foo=Empty(

                )
            ),
            type="{foo}Dr"
        ),
        DerivedElement(
            qname="{foo}eB",
            value=De(
                foo=Empty(

                )
            ),
            type="{foo}De"
        ),
        DerivedElement(
            qname="{foo}eB",
            value=Drr(
                foo=Empty(

                )
            ),
            type="{foo}Drr"
        ),
        DerivedElement(
            qname="{foo}eB",
            value=Dre(
                foo=Empty(

                )
            ),
            type="{foo}Dre"
        ),
        DerivedElement(
            qname="{foo}eB",
            value=Der(
                foo=Empty(

                )
            ),
            type="{foo}Der"
        ),
        DerivedElement(
            qname="{foo}eB",
            value=Dee(
                foo=Empty(

                )
            ),
            type="{foo}Dee"
        ),
        EDr(
            foo=Empty(

            )
        ),
        EDr(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname="{foo}eDr",
            value=Drr(
                foo=Empty(

                )
            ),
            type="{foo}Drr"
        ),
        DerivedElement(
            qname="{foo}eDr",
            value=Dre(
                foo=Empty(

                )
            ),
            type="{foo}Dre"
        ),
        EDe(
            foo=Empty(

            )
        ),
        EDe(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname="{foo}eDe",
            value=Der(
                foo=Empty(

                )
            ),
            type="{foo}Der"
        ),
        DerivedElement(
            qname="{foo}eDe",
            value=Dee(
                foo=Empty(

                )
            ),
            type="{foo}Dee"
        ),
        EDrr(
            foo=Empty(

            )
        ),
        EDrr(
            foo=Empty(

            )
        ),
        EDre(
            foo=Empty(

            )
        ),
        EDre(
            foo=Empty(

            )
        ),
        EDer(
            foo=Empty(

            )
        ),
        EDer(
            foo=Empty(

            )
        ),
        EDee(
            foo=Empty(

            )
        ),
        EDee(
            foo=Empty(

            )
        ),
    ]
)
