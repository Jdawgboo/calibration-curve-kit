# Calibration Curve Kit

Compute reliability-bin summaries, Expected Calibration Error, and Brier score from probabilities and binary outcomes.

```bash
cat predictions.json | python tool.py
python -m unittest -v
```

ECE depends on binning choices. Use this for diagnostics, not as the only reliability decision criterion.
