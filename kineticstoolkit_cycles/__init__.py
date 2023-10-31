#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright Félix Chénier 2023

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Development module for kineticstoolkit.cycles.

This module is an experimental workspace for developing functions that may or
may not be transferred at completion to kineticstoolkit.cycles.
"""

__author__ = "Félix Chénier"
__copyright__ = "Copyright (C) 2023 Félix Chénier"
__email__ = "chenier.felix@uqam.ca"
__license__ = "Apache 2.0"


import kineticstoolkit as ktk
from scipy.signal import find_peaks as _find_peaks


def detect_phase(
    ts: ktk.TimeSeries,
    signal_name: str,
    treshold: float,
    *,
    event_names: tuple[str] = ["begin", "end"],
    min_time: float = 0.0,
    invert: bool = False,
) -> ktk.TimeSeries:
    """
    Find a reccuring phase in a TimeSeries based on a treshold analysis.

    This function analyzes a signal that has a baseline, and detects
    non-baseline portions based on a treshold and an optional minimal duration.
    For instance, this function can be used to detect stance and swing phases
    in gait using a force plate, or the ankle height.

    Parameters
    ----------
    ts
        The input TimeSeries.
    signal_name
        The name of the signal to analyse in TimeSeries.data.
    treshold
        The treshold over which the phase is defined.
    event_names
        Optional. Name of the begin and end events to be added on each phase.
        The default is ["begin", "end"].
    min_time
        Optional. Minimal time (in seconds) required to register a phase. Use
        to avoid identifying false in noisy data. The default is 0.0.

    Returns
    -------
    TimeSeries
        A copy of the input TimeSeries with the added events.

    """
    signal = ts.data[signal_name]

    if not invert:
        is_on = signal > treshold
    else:
        is_on = signal <= treshold

    is_on[0] = 0
    is_on[-1] = 0
    ret = _find_peaks(is_on, plateau_size=min_time * ts.get_sample_rate())

    for i in ret[1]["left_edges"]:
        ts.add_event(ts.time[i], event_names[0], in_place=True)
    for i in ret[1]["right_edges"]:
        ts.add_event(ts.time[i], event_names[1], in_place=True)

    ts.sort_events(in_place=True)
    return ts


"""
The section below is optional. If you put code examples in your docstring,
then running this file will test that your examples give the correct results.
Please check https://docs.python.org/3/library/doctest.html for details.
"""
if __name__ == "__main__":  # pragma: no cover
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
