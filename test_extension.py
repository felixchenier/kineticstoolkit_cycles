#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 AUTHORNAME

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Unit tests, to be run using pytest."""


__author__ = "AUTHORNAME"
__copyright__ = "Copyright (C) YEAR AUTHORNAME"
__email__ = "AUTHOREMAIL"
__license__ = "Apache 2.0"


import sys
import os
import kineticstoolkit as ktk


# Add this extension to the path, for testing before the extension is
# distributed and installed via pip.
if os.path.dirname(__file__) not in sys.path:
    sys.path.append(os.path.dirname(__file__))

ktk.import_extensions()


def test_function1():
    """Test function 1. Placeholder. Delete me."""
    assert ktk.ext.EXTENSIONNAME.function1() == "I am function1"


def test_function2():
    """Test function 2. Placeholder. Delete me."""
    assert ktk.ext.EXTENSIONNAME.function2() == "I am function2"


if __name__ == "__main__":
    # You can either run this file directly, or run 'pytest test_extension.py' in
    # a terminal.
    import pytest

    pytest.main([__file__])
