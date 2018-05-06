import unittest
import doctest

from .. import (widget, wimp, decoration, display_common, main_loop,
                monitored_list, numedit, raw_display, split_repr, util,
                signals, graphics)


def load_tests(loader, tests, ignore):
    module_doctests = [
        widget,
        wimp,
        decoration,
        display_common,
        main_loop,
        numedit,
        monitored_list,
        raw_display,
        split_repr, # override function with same name
        util,
        signals,
        graphics,
        ]
    for m in module_doctests:
        tests.addTests(doctest.DocTestSuite(m,
            optionflags=doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL))
    return tests
