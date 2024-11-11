Data Understanding
====================================================


.. toctree::
    :maxdepth: 2
    :caption: Contents:

Data Sources
============

Original data could not be uploaded to GitHub due to its size. However, the links to the original data are available at:

- `Kaggle Playground Series S4E8 <https://www.kaggle.com/competitions/playground-series-s4e8/data>`_
- `Mushroom Dataset - UCI Machine Learning Repository <https://archive.ics.uci.edu/dataset/73/mushroom>`_

Data Dictionary
===============

.. list-table:: Data Dictionary

   * - **Feature**
     - **Description**
   * - cap-shape
     - Shape of the mushroom cap
   * - cap-color
     - Color of the mushroom cap
   * - gill-size
     - Size of the gills
   * - gill-color
     - Color of the gills
   * - ...
     - ...


For the complete list of features visit the `UCI Machine Learning Repository <https://archive.ics.uci.edu/dataset/73/mushroom>`_.

Initial Observations
====================

- The dataset contains mostly categorical features.
- Target variable: **edibility** (edible (e) or poisonous (p)).

Data Quality Issues
===================

- Some missing values in the color attributes.
- Possible class imbalance between edible and poisonous mushrooms.
