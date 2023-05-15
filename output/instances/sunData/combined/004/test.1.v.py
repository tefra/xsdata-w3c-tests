from output.models.sun_data.combined.pkg_004.test_xsd.test import B
from output.models.sun_data.combined.pkg_004.test_xsd.test import De
from output.models.sun_data.combined.pkg_004.test_xsd.test import Dee
from output.models.sun_data.combined.pkg_004.test_xsd.test import Der
from output.models.sun_data.combined.pkg_004.test_xsd.test import Dr
from output.models.sun_data.combined.pkg_004.test_xsd.test import Dre
from output.models.sun_data.combined.pkg_004.test_xsd.test import Drr
from output.models.sun_data.combined.pkg_004.test_xsd.test import Empty
from output.models.sun_data.combined.pkg_004.test_xsd.test import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    item1_or_item2=[
        B(
            foo=Empty(

            )
        ),
        B(
            foo=Empty(

            )
        ),
        Dr(
            foo=Empty(

            )
        ),
        De(
            foo=Empty(

            )
        ),
        Drr(
            foo=Empty(

            )
        ),
        Dre(
            foo=Empty(

            )
        ),
        Der(
            foo=Empty(

            )
        ),
        Dee(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname="{foo}item2",
            value=B(
                foo=Empty(

                )
            )
        ),
        DerivedElement(
            qname="{foo}item2",
            value=B(
                foo=Empty(

                )
            ),
            type="{foo}B"
        ),
        DerivedElement(
            qname="{foo}item2",
            value=Dr(
                foo=Empty(

                )
            ),
            type="{foo}Dr"
        ),
        DerivedElement(
            qname="{foo}item2",
            value=Drr(
                foo=Empty(

                )
            ),
            type="{foo}Drr"
        ),
    ]
)
