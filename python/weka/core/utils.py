# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# utils.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import javabridge
import logging
import weka.core.arrays as arrays

# logging setup
logger = logging.getLogger(__name__)


def split_options(cmdline):
    """
    Splits the commandline into a list of options.
    :param cmdline: the commandline string to split into individual options
    :rtype: list
    """
    return arrays.string_array_to_list(
        javabridge.static_call(
            "Lweka/core/Utils;", "splitOptions",
            "(Ljava/lang/String;)[Ljava/lang/String;",
            cmdline))


def join_options(options):
    """
    Turns the list of options back into a single commandline string.
    :param options: the list of options to process
    :rtype: str
    """
    return javabridge.static_call(
        "Lweka/core/Utils;", "joinOptions",
        "([Ljava/lang/String;)Ljava/lang/String;",
        options)
