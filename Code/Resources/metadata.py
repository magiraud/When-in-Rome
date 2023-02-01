# -*- coding: utf-8 -*-
"""

NAME:
===============================
Metadata (metadata.py)

BY:
===============================
Mark Gotham

LICENCE:
===============================
Creative Commons Attribution-ShareAlike 4.0 International License
https://creativecommons.org/licenses/by-sa/4.0/

ABOUT:
===============================
Stores initial information about metadata for the sub-corpora and
uses this to initialises sub-directories of When in Rome.

We create individual files so that
1) the information is easily accessible, e.g., from the analysis file in the same dir;
and
2) each sub-corpus can store the slightly different information that is relevant
(e.g., different catalogue names etc.).

Dict keys as consistent as possible, including
All:
    "path_within_WiR": "When-in-Rome/Corpus/<x>"
    "items": itemised lists. NB: format varies
    "item_keys": explanation for the items.
    "analysis_source": the source of the included "analysis.txt" file
Some:
    "analysis<_identifier>.txt" > "analysis<_identifier>_source" for any additional analyses
    "score_source": where a local "score.mxl" is included
    "remote_score_<format>": where a remote score is available.

URLs are initialised here with the base and extended when created.
"""


# ------------------------------------------------------------------------------

from .. import raw_git

chorales = dict(
    path_within_WiR=["Early_Choral", "Bach,_Johann_Sebastian", "Chorales"],
    item_keys="Riemenschneider",
    items=371,
    analysis_source="Bach Chorales",  # NB no public listing, so relative path only
    remote_score_mxl=raw_git + "MarkGotham/Chorale-Corpus/Bach,_Johann_Sebastian/Chorales/"
    )

madrigals = dict(
    path_within_WiR=["Early_Choral", "Monteverdi,_Claudio"],
    item_keys=("Book", "Number"),
    items=(
        (3, 20),  # "Madrigals_Book_3"
        (4, 20),
        (5, 8)
        ),
    analysis_source="Monteverdi",
    remote_score_mxl=raw_git + "cuthbertLab/music21/master/music21/corpus/monteverdi/"
    )

tempered = dict(
    path_within_WiR=["Keyboard_Other", "Bach,_Johann_Sebastian", "The_Well-Tempered_Clavier_I"],
    items=24,
    analysis_source="New"
    )

chopin_commit = "ad38f0a82e5c50740b1d70a41c84924562bdf9f2"

chopin = dict(
    repo_name="chopin_mazurkas",
    path_within_WiR=["Keyboard_Other", "Chopin,_Frédéric", "Mazurkas"],
    item_keys=("Brown Catalogue", "Opus"),  # No sub-movements
    items=(

        ((16, 1), (None, None)),
        ((16, 2), (None, None)),

        ((18, None), (68, 2)),
        ((34, None), (68, 3)),
        ((38, None), (68, 1)),

        ((60, 1), (6, 1)),
        ((60, 2), (6, 2)),
        ((60, 3), (6, 3)),
        ((60, 4), (6, 4)),

        ((61, 1), (7, 1)),
        ((61, 2), (7, 2)),
        ((61, 3), (7, 3)),
        ((61, 4), (7, 4)),
        ((61, 5), (7, 5)),

        ((71, None), (None, None)),
        ((73, None), (None, None)),

        ((77, 1), (17, 1)),
        ((77, 2), (17, 2)),
        ((77, 3), (17, 3)),
        ((77, 4), (17, 4)),

        ((85, None), (None, None)),

        ((89, 1), (24, 1)),
        ((89, 2), (24, 2)),
        ((89, 3), (24, 3)),
        ((89, 4), (24, 4)),

        ((93, 1), (67, 1)),
        ((93, 2), (67, 3)),

        ((105, 2), (30, 2)),
        ((105, 3), (30, 3)),
        ((105, 4), (30, 4)),

        ((115, 1), (33, 1)),
        ((115, 2), (33, 2)),
        ((115, 3), (33, 3)),
        ((115, 4), (33, 4)),

        ((122, None), (41, 2)),

        ((126, 1), (41, 4)),
        ((126, 3), (41, 1)),
        ((126, 4), (41, 3)),

        ((134, None), (None, None)),
        ((140, None), (None, None)),

        ((145, 1), (50, 1)),
        ((145, 2), (50, 2)),
        ((145, 3), (50, 3)),

        ((153, 1), (56, 1)),
        ((153, 2), (56, 2)),
        ((153, 3), (56, 3)),

        ((157, 1), (59, 1)),
        ((157, 2), (59, 2)),
        ((157, 3), (59, 3)),

        ((162, 1), (63, 1)),
        ((162, 2), (63, 2)),
        ((162, 3), (63, 3)),

        ((163, None), (67, 4)),
        ((167, None), (67, 2)),
        ((168, None), (68, 4)),
        ),
    analysis_source=raw_git + f"DCMLab/chopin_mazurkas/{chopin_commit}/harmonies/",
    remote_score_mscx=raw_git + f"DCMLab/chopin_mazurkas/{chopin_commit}/MS3/",
    analysis_DT_source="Chopin",  # NB no public listing, so relative path only
    remote_score_krn=raw_git + "craigsapp/chopin-mazurkas/master/kern/",
    )
