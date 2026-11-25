---
type: example
status: established
title: "Stock Prediction Neural Network — SOLID ML App with Tkinter GUI"
domain: machine-learning
project: Stock-Prediction-Neural-Network
concepts: [neural-networks-linear-models, ml-model-training-evaluation, solid-and-design-patterns]
date: 2026-05-12
---

# Stock Prediction Neural Network

## What It Is
A desktop ML app (Tkinter) that tracks multiple stock symbols, trains a custom two-layer neural network per stock, and generates OHLCV price forecasts with Best/Average/Worst Case scenario bands. Includes accuracy scoring, model persistence, and live chart popups.

Data source: Yahoo Finance via `yfinance` (no API key required).

## Architecture — SOLID + Dependency Inversion
All high-level modules depend on abstract interfaces in `core/interfaces.py`. Concrete implementations are injected at `ui/app.py`.

```
core/interfaces.py   — IDataFetcher, IModelRepository, IHistoryRepository, ISymbolRepository
core/models.py       — ScoreResult, PredictionRecord (shared data models)
data/fetcher.py      — YahooFinanceFetcher (implements IDataFetcher)
data/indicators.py   — 12 technical indicator calculations
ml/network.py        — NeuralNetwork (forward/backward, Monte Carlo uncertainty)
ml/trainer.py        — Epoch training loop
ml/predictor.py      — Scenario generation (Best/Average/Worst)
scoring/scorer.py    — Composite 0–100 accuracy score
scoring/calibration.py — Band widening from historical residuals
services/trading_service.py — Data + ML orchestration
services/stock_registry.py  — Background thread workers, round-robin updates
storage/             — JSON weights, CSV history, JSON symbols, Excel exports
ui/                  — Tkinter tabs (Stock Manager, Edit Model, Chart popup)
launch.py            — Splash screen, dependency checker, entry point
```

## Neural Network Design

Custom two-layer, pure NumPy (no ML frameworks):

```
Input (lookback × 12 features) → Hidden (30, ReLU) → Output (5: OHLCV)
```

**12 features per time step:** Open, High, Low, Close, Volume, SMA-20, RSI(14), Volume Ratio, Volatility(20d σ), MACD, MACD Signal, Momentum(10d).

Key implementation choices:
- **He initialisation** (`np.sqrt(2 / fan_in)`) for ReLU layers
- **Adaptive LR**: halves one step when `std(last 10 losses) > 0.5 × mean` — avoids manual schedule
- **Monte Carlo uncertainty**: 100 noisy forward passes (Gaussian σ=0.02) → (mean, std) for confidence
- **Incremental update**: one forward+backward pass on new data → online learning without full retrain

## Accuracy Scoring (composite 0–100)

| Component | Weight | Metric |
|-----------|--------|--------|
| MAPE accuracy | 50% | Predicted vs actual close |
| Directional accuracy | 30% | Up/down correct? |
| Within-range accuracy | 20% | Actual inside best/worst band? |

Letter grades: A+ ≥93 … F <20.

**Band calibration**: when ≥5 matched predictions in `prediction_score.xlsx`, best/worst bands are auto-widened using historical residuals to target 75% in-range rate.

## Model Persistence Flow

```
Train:   restore weights (if saved & shape matches) → short retrain (~20% epochs)
         → save weights to stock_models.json + scaler params
         → save last-5 predictions to stock_models_history.csv

Predict: run inference → archive prediction → update stock_data.xlsx (authoritative actual-close source)
         → update prediction_score.xlsx
```

Shape mismatch (e.g. after feature count change) → warn + full retrain from scratch.

## Background Threading Pattern

All ML work runs in background threads. UI updates flow through a message queue (checked every 100 ms in `ui/app.py`) so the Tkinter main loop never blocks.

- Round-robin adaptive model updates across all tracked symbols
- Predictions refresh every 5 minutes
- `stock_data.xlsx` pull: on launch + every 15 minutes
- Excel exports: every 20 minutes

## Key Bugs Fixed During Development

| Commit | Issue |
|--------|-------|
| `46ef934` | Erroneous data values causing bad training samples |
| `00552e7` | Data parsing was inconsistent across runs — redone to be deterministic; was the root cause of occasionally wrong predictions |
| `620e7f7` | Duplicated utility functions and redundant variables removed |
