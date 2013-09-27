# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals
from pkg_resources import resource_stream  # @UnresolvedImport


COUNTRIES = {}
with resource_stream('babelfish', 'data/iso-3166-1.txt') as f:
    f.readline()
    for l in f:
        (name, alpha2) = l.decode('utf-8').strip().split(';')
        COUNTRIES[alpha2] = name


class Country(object):
    """A country on Earth

    A country is represented by a two-letters code from the ISO-3166 standard

    :param string country: two-letters ISO-3166 country code

    """
    def __init__(self, country):
        if country not in COUNTRIES:
            raise ValueError('{} is not a valid country'.format(country))

        #: ISO-3166 two-letters country code
        self.alpha2 = country

    @property
    def name(self):
        """English name of the country"""
        return COUNTRIES[self.alpha2]

    def __hash__(self):
        return hash(self.alpha2)

    def __eq__(self, other):
        return self.alpha2 == other.alpha2

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return '<Country {}>'.format(self.name)
