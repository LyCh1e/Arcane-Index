---
address: c-000058
type: concept
status: established
title: "Sensor Fusion and Edge Computing"
domain: embedded-systems
source: INF2004
complexity: high
tags: [embedded-systems, sensors, sensor-fusion, actuators, edge-computing, tinyml, inf2004]
---

# Sensor Fusion and Edge Computing

## Sensors

### Definition

A **sensor** is a device that receives a physical **stimulus** and responds with an **electrical signal** (voltage, current, or charge).

- **Stimulus** (input): motion, position, velocity, force, pressure, sound, temperature, light, chemical presence
- **Response** (output): electrical signal that can be amplified and processed by a microcontroller

Sensors are **energy translators** (transducers) — converting one form of energy to another. Some conversions are indirect (e.g. chemical → heat → electrical via thermopile).

### Physical Sensing Principles

| Principle | Example Sensor |
|-----------|---------------|
| Capacitance | Touchscreen, water-level sensor |
| Resistance | Thermistor (temperature) |
| Inductance / Magnetism | Hall-effect, compass |
| Piezoelectric effect | Microphone, accelerometer |
| Seebeck effect | Thermocouple |
| Light (photoelectric) | Photodiode, camera |

### Sensor System Architecture

```
Physical World
    │ stimulus
    ▼
Sensor (transducer)
    │ analogue signal
    ▼
Signal Conditioning (filter → zero → scale → linearise)
    │
    ▼
ADC
    │ digital samples
    ▼
Microcontroller (processing, sensor fusion)
    │ command
    ▼
DAC / GPIO
    │
    ▼
Actuator
```

---

## Signal Conditioning

Before reaching the ADC, the analogue signal is conditioned:

| Step | Purpose |
|------|---------|
| **Filter** | Remove frequencies outside the band of interest (noise) |
| **Remove DC offset (zeroing)** | Set baseline to zero so readings are centred |
| **Amplify / Attenuate (scaling)** | Match signal amplitude to ADC input range |
| **Linearise** | Convert non-linear sensor output to a linear relationship |
| **ADC conversion** | Translate analogue voltage to digital number |

---

## Signal Preprocessing

Preprocessing improves **signal-to-noise ratio (SNR)** before or after sampling.

| Focus | Method | Example |
|-------|--------|---------|
| Past → **Smoothing** | Average or blend previous readings | Moving average, Exponential Moving Average (EMA) |
| Present → **Filtering** | Shape/isolate frequency components | FIR, IIR low-pass / high-pass / notch filters |
| Future → **Prediction** | Estimate upcoming value or state | Kalman filter, linear extrapolation |

**Averaging improves SNR** via the Central Limit Theorem: averaging N independent samples reduces noise by √N.

### Kalman Filter

> *Predict → Measure → Correct → Repeat*

- Maintains a probabilistic estimate of the true state
- Balances prediction from a model against noisy measurement
- Optimal for linear systems with Gaussian noise

---

## Why Filtering Alone Is Not Enough

- Filters reduce noise but cannot correct **bias**, **drift**, or **missing information**
- A drifting gyroscope becomes a smoother drift — not a corrected one
- Some sensors react fast but are noisy; others are stable but slow — a single filter cannot balance both
- Filters are "earplugs for noise," not "truth detectors"

**Solution: Sensor Fusion** — combine data from multiple heterogeneous sensors to produce a better estimate than any single sensor alone.

---

## Complementary Filter

Fuses a fast-but-noisy sensor with a slow-but-stable sensor:

```
output = α × (fast sensor component) + (1 − α) × (slow sensor component)
```

**Distance fusion example:**
```
d_estimate = α × d_fast + (1 − α) × d_slow
```
- `d_fast` — ultrasonic sensor: reacts quickly but noisy
- `d_slow` — another sensor: smoother but delayed

**Angle fusion (IMU):**
```
θ_estimate = α × (θ_prev + gyro_rate × Δt) + (1 − α) × θ_accelerometer
```
- Gyro term: fast, predicts angle — but drifts over time
- Accelerometer term: stable long-term — but sensitive to vibration

---

## Sensor Fusion Classifications

### By Abstraction Level

| Level | Description |
|-------|-------------|
| **Data-level** | Raw data from homogeneous sensors combined before processing |
| **Feature-level** | Features extracted per sensor, then fused |
| **Decision-level** | Each sensor makes an independent decision; decisions are combined |

### By Centralisation Level

| Level | Description | Trade-off |
|-------|-------------|-----------|
| **Centralised** | All raw data sent to one hub | High accuracy; high bandwidth demand |
| **Distributed** | Each sensor pre-processes; summaries sent to hub | Low bandwidth; some accuracy loss |
| **Decentralised (Hybrid)** | Mix of both | High adaptability; highest system complexity |

### By Competition Level

| Type | Description | Example |
|------|-------------|---------|
| **Competitive (Redundancy)** | Multiple sensors cover the same target for fault tolerance | RADAR + LiDAR for pedestrian detection |
| **Complementary** | Sensors cover different aspects of the scene | Multi-camera panorama |
| **Coordinated** | Multiple sensors look at the same target from different positions | Stereo camera (depth from disparity) |

### Advantages of Sensor Fusion

- Robustness and reliability (graceful degradation on sensor failure)
- Extended spatial and temporal coverage
- Increased confidence in estimates
- Reduced ambiguity and uncertainty
- Improved resolution beyond any single sensor's capability

---

## Actuators

An **actuator** converts a controller command signal into a change in a physical parameter (usually mechanical).

| Type | Driving force | Example |
|------|--------------|---------|
| **Electrical** | Electromagnetism | DC motor, stepper motor, solenoid |
| **Hydraulic** | Hydraulic fluid pressure | Industrial robots, aircraft control surfaces |
| **Pneumatic** | Compressed air | Pneumatic cylinders, pneumatic valves |

**Servo motor** — uses **negative feedback** to control position or speed precisely. Sensor measures actual position; controller adjusts drive signal to minimise error. Used in CNC, telescope mirrors, RC vehicles.

| Dimension | Sensor | Actuator |
|-----------|--------|---------|
| Placed at | Input port | Output port |
| Direction | Physical world → MCU | MCU → Physical world |
| Output | Electrical signal | Heat, motion, force |

---

## Edge Computing

### Context: Cloud Limitations

| Challenge | Impact |
|-----------|--------|
| **Latency** | Unsuitable for time-sensitive applications |
| **Bandwidth** | Sending raw sensor data is expensive |
| **Privacy** | Off-premises storage poses regulatory risks |
| **Connectivity** | Cloud-dependent availability |

### Edge Computing Definition

> *"A distributed computing paradigm that brings computation and data storage closer to data sources such as sensors, devices, and end-users."* — NIST

**Core idea:** Process data where it is generated (at the device/edge) rather than sending everything to the cloud.

### Edge–Fog–Cloud Architecture

| Layer | Scale | Role |
|-------|-------|------|
| **Edge** | Billions of devices | Real-time sensing, local control, low latency |
| **Fog** | Millions of gateways | Aggregation, short-term analytics |
| **Cloud** | Thousands of servers | Long-term storage, model training, big analytics |

### Characteristics and Benefits

| Characteristic | Benefit |
|----------------|---------|
| Local data processing | Low latency for time-sensitive responses |
| Data stays on device | Improved privacy and security |
| Autonomous decisions | Immediate, context-aware action |
| Data filtering at source | Reduced bandwidth usage and cost |
| Resilience to connectivity loss | Continued operation offline |

---

## TinyML

**TinyML** (Tiny Machine Learning) — deploying trained ML models on resource-constrained devices (microcontrollers, embedded systems) for on-device inference.

### Key Properties

- **Low power** — operates within milliwatt budgets
- **Small model size** — tens to hundreds of kilobytes
- **On-device processing** — no cloud round-trip required
- **Real-time inference** — millisecond response

### Model Optimisation Techniques

| Technique | Description |
|-----------|-------------|
| **Quantisation** | Reduce weight precision from 32-bit float → 8-bit integer |
| **Pruning** | Remove low-significance weights or neurons |
| **Knowledge distillation** | Train a small "student" model to mimic a large "teacher" model |
| **Efficient architectures** | MobileNet, SqueezeNet (CNNs designed for low-resource inference) |

### Frameworks

| Framework | Description |
|-----------|-------------|
| **TensorFlow Lite for Microcontrollers** | TFLite subset optimised for MCUs |
| **CMSIS-NN** | ARM Cortex-M optimised NN kernels |
| **Edge Impulse** | End-to-end TinyML platform (collect → train → deploy) |
| **uTensor** | Lightweight inference library for MCUs |

### TinyML Applications

- Environmental monitoring (temperature/humidity regression)
- Anomaly detection in machinery (vibration analysis)
- Gesture recognition (accelerometer CNN)
- Voice activation (keyword spotting)
- Predictive maintenance (RNN vibration patterns)

### Constraints

- Models must fit in limited RAM and flash
- Integer-only arithmetic preferred (avoids FPU)
- Energy budget dictates inference frequency
- Model sizes typically 10s–100s KB

---

## Connections

- [[concepts/embedded-systems-fundamentals|Embedded Systems Fundamentals]] — hardware platform, real-time constraints
- [[concepts/embedded-io-and-interrupts|Embedded I/O and Interrupts]] — ADC used to digitise sensor signals
- [[concepts/ml-foundations|Machine Learning Foundations]] — ML algorithms deployed via TinyML
- [[concepts/clustering-and-dimensionality-reduction|Clustering & Dimensionality Reduction]] — unsupervised learning applicable at edge
- [[concepts/wireless-and-iot|Wireless Networking & IoT]] — edge nodes communicate via IoT protocols
