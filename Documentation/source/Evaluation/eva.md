## Evaluation process

We evaluated the models as they were created in every step of the process, always producing a report with the results. Every evaluation report is avaliable at [`Reports/Evaluation`](https://github.com/faendal/MushroomEdibilityPrediction/tree/main/Reports/Evaluation). The evaluation process was done using the following metrics:

### Evaluation Metrics
- **Accuracy**: Measure of correctly predicted instances.
- **ROC-AUC**: Area under the Receiver Operating Characteristic curve.
- **F1 Score**: Balances precision and recall, especially useful for imbalanced classes.
- **Recall**: For poisonous class. Measure of actual positive instances that were correctly predicted.

## All models evaluation

At first, we created 7 models in total and evaluated them to determine wich were the 3 best models. The figure ahead shows the evaluation results for all models.

![All models evaluation](https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/ModelEvaluation.png)

Then we used friedman test and post-hoc Nemenyi test to determine the best models. The figure ahead shows the results of the tests.

![Friedman and Nemenyi tests](https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/Nemenyi-Friedman-Posthoc.png)

## Hyperparametrized models evaluation

After determining the best models, we hyperparametrized them to improve their performance. The figure ahead shows the evaluation results for the hyperparametrized models.

![Hyperparametrized models evaluation](https://raw.githubusercontent.com/faendal/MushroomEdibilityPrediction/refs/heads/main/Reports/Evaluation/HyperparametrizedModelEvaluation.png)
