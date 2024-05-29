# coding=utf-8
"""
.. moduleauthor:: Shuhua Gao

This module :mod:`parser` provides functionality for compiling an individual (a chromosome) in GEP into an executable
lambda function in Python for subsequent fitness evaluation.

.. todo::
    Parse an individual into codes of other languages, such as C++/Java, for deployment in an industrial environment.
"""

import sys

def _compile_gene(g, pset):
    """
    Compile one gene *g* with the primitive set *pset*.
    :return: compiled program of a single gene
    """
    return str(g)

def compile_(individual, pset):
    """
    Compile the individual into a Python lambda expression.

    :param individual: :class:`Chromosome`, a chromosome
    :param pset: :class:`PrimitiveSet`, a primitive set
    :return: compiled program
    """
    return [_compile_gene(gene, pset) for gene in individual][0]

__all__ = ['compile_']
