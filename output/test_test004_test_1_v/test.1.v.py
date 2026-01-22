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
        Root.Item1(
            foo=Empty(

            )
        ),
        Root.Item1(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname='{foo}item1',
            value=Dr(
                foo=Empty(

                )
            ),
            type='{foo}Dr'
        ),
        DerivedElement(
            qname='{foo}item1',
            value=De(
                foo=Empty(

                )
            ),
            type='{foo}De'
        ),
        DerivedElement(
            qname='{foo}item1',
            value=Drr(
                foo=Empty(

                )
            ),
            type='{foo}Drr'
        ),
        DerivedElement(
            qname='{foo}item1',
            value=Dre(
                foo=Empty(

                )
            ),
            type='{foo}Dre'
        ),
        DerivedElement(
            qname='{foo}item1',
            value=Der(
                foo=Empty(

                )
            ),
            type='{foo}Der'
        ),
        DerivedElement(
            qname='{foo}item1',
            value=Dee(
                foo=Empty(

                )
            ),
            type='{foo}Dee'
        ),
        Root.Item2(
            foo=Empty(

            )
        ),
        Root.Item2(
            foo=Empty(

            )
        ),
        DerivedElement(
            qname='{foo}item2',
            value=Dr(
                foo=Empty(

                )
            ),
            type='{foo}Dr'
        ),
        DerivedElement(
            qname='{foo}item2',
            value=Drr(
                foo=Empty(

                )
            ),
            type='{foo}Drr'
        ),
    ]
)
