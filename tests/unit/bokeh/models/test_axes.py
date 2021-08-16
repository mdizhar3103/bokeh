#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from bokeh.models import FixedTicker, MathText, PlainText

# Module under test
import bokeh.models.axes as bma # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def test_ticker_accepts_number_sequences() -> None:
    a = bma.Axis(ticker=[-10, 0, 10, 20.7])
    assert isinstance(a.ticker, FixedTicker)
    assert a.ticker.ticks == [-10, 0, 10, 20.7]

    a = bma.Axis()
    a.ticker = [-10, 0, 10, 20.7]
    assert isinstance(a.ticker, FixedTicker)
    assert a.ticker.ticks == [-10, 0, 10, 20.7]

def test_axis_label_accepts_math_text_with_dollar_signs_and_no_declaration() -> None:
    a = bma.Axis(axis_label=r"$\sin(x+1)$")
    assert isinstance(a.axis_label, MathText)
    assert a.axis_label.text == r"\sin(x+1)"

def test_axis_label_accepts_math_text_with_declaration() -> None:
    a = bma.Axis(axis_label=MathText(text=r"\sin(x+2)"))
    assert isinstance(a.axis_label, MathText)
    assert a.axis_label.text == r"\sin(x+2)"

def test_axis_label_accepts_math_text_with_declaration_and_dollar_signs() -> None:
    a = bma.Axis(axis_label=MathText(text=r"$\sin(x+3)$"))
    assert isinstance(a.axis_label, MathText)
    assert a.axis_label.text == r"\sin(x+3)"

def test_axis_label_accepts_math_text_with_constructor_arg() -> None:
    a = bma.Axis(axis_label=MathText(r"\sin(x+4)"))
    assert isinstance(a.axis_label, MathText)
    assert a.axis_label.text == r"\sin(x+4)"

def test_axis_label_accepts_math_text_with_constructor_arg_and_dollar_signs() -> None:
    a = bma.Axis(axis_label=MathText(r"$\sin(x+5)$"))
    assert isinstance(a.axis_label, MathText)
    assert a.axis_label.text == r"\sin(x+5)"

def test_axis_label_accepts_string_with_dollar_signs() -> None:
    a = bma.Axis(axis_label=PlainText(r"$\sin(x+6)$"))
    assert isinstance(a.axis_label, str)
    assert a.axis_label == r"$\sin(x+6)$"


#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
