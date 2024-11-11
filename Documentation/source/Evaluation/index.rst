Evaluation
====================================================


.. toctree::
    :maxdepth: 2
    :caption: Contents:

    Evaluation Process
    ==================

    We evaluated the models as they were created in every step of the process, always producing a report with the results. Every evaluation report is available at `Reports/Evaluation <https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Reports/Evaluation>`_. The evaluation process was done using the following metrics:

    Evaluation Metrics
    ------------------

    - **Accuracy**: Measure of correctly predicted instances.
    - **ROC-AUC**: Area under the Receiver Operating Characteristic curve.
    - **F1 Score**: Balances precision and recall, especially useful for imbalanced classes.
    - **Recall**: For poisonous class. Measure of actual positive instances that were correctly predicted.

    All Models Evaluation
    =====================

    At first, we created 7 models in total and evaluated them to determine which were the 3 best models. The figure ahead shows the evaluation results for all models.

    .. image:: https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/ModelEvaluation.png
    :alt: All models evaluation
    :align: center

    Then we used the Friedman test and post-hoc Nemenyi test to determine the best models. The figure ahead shows the results of the tests.

    .. image:: https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/Nemenyi-Friedman-Posthoc.png
    :alt: Friedman and Nemenyi tests
    :align: center

    Hyperparametrized Models Evaluation
    ===================================

    After determining the best models, we hyperparametrized them to improve their performance. The figure ahead shows the evaluation results for the hyperparametrized models.

    .. image:: https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/HyperparametrizedModelEvaluation.png
    :alt: Hyperparametrized models evaluation
    :align: center
