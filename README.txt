Introduction
============

This module try to achive an inplace viewing mode inside topics. In fact we
use collection to get back items inside other sections. 

The use case
============

Let say you have a tree like this:

+ My Plone site
| - documents (excluded from nav)
| - news (excluded from nav)
| - events (excluded from nav)
| + mysection (a folder)
| | -  mytopic


This module lets you have url like "http://MyPloneSite/mysection/mysubsection/documents/adocument"
in the mytopic listing. In that case adocument is rendered in the context of mytopic

Notes
=====

Some skins use context to create new design (by changing the color for example).

This module override default topic views by using acquisition to obtain this behaviour.

But some UI stuff in Plone are not acquisition aware. For this reason this add-on use a
browser layer to override some UI parts of Plone like

* breadcrumb (parents are not taken with acquisition)
* portlet rendering (inheritance do not respect acquisition)

.. contents::

Credits
======================================
|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


