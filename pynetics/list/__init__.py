# ======================================================================
# pynetics: a simple yet powerful evolutionary computation library
# Copyright (C) 2020 Alberto Díaz-Álvarez
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# “Software”), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ======================================================================
"""Implementations of specific operators for list based representations.

This includes genotypes, operations and so. Note that not all the
implementations work together. For example, there are operators for
integer representation that are no suitable for real or binary
representations and vice versa. Even between the same gene kind (e.g.
integer), there may be problems depending on the problem (e.g. a
"Knapsack problem" and a "Travelling Salesman Problem" use a completely
different set of operators with the exception, maybe, the mutation
schema).
"""
