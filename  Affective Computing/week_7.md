# Affective Computing

## Week 7 : Assignment 7 — Detailed Solution

---

### Question 1

**Physiological signals are especially valuable in affect detection because they:**

- **A. Cannot be voluntarily controlled and reflect pure emotional states ✅**
- B. Require full attention from the participant
- C. Are easier to fake than facial expressions
- D. Are unaffected by wearable technologies

**Answer: A — Cannot be voluntarily controlled and reflect pure emotional states**

**Explanation:** Unlike facial expressions or self-reports, **physiological signals** such as heart rate, galvanic skin response (GSR), and respiration are governed by the **autonomic nervous system** and are largely **involuntary**. This makes them highly valuable for affect detection because they are difficult to consciously fake or suppress, providing a more authentic window into a person's emotional state. This involuntary nature is precisely what gives physiological signals an advantage in affective computing applications.

---

### Question 2

**Which of the following is not a physiological measure?**

- A. Respiration
- B. Electrocardiogram
- C. Heart Rate
- **D. Eye-blink frequency ✅**

**Answer: D — Eye-blink frequency**

**Explanation:** **Respiration**, **Electrocardiogram (ECG)**, and **Heart Rate** are all direct physiological measures reflecting activity of the body's internal systems (cardiovascular, respiratory). **Eye-blink frequency**, while measurable and emotionally relevant, is a **behavioral/oculomotor measure** rather than a physiological one in the strict sense — it is observed externally and is more susceptible to voluntary control. It falls under the category of behavioral or facial/ocular signals rather than internal physiological signals.

---

### Question 3

**Heart rate is strongly associated with which dimension of emotion?**

- A. Valence
- **B. Arousal ✅**
- C. Dominance
- D. Surprise

**Answer: B — Arousal**

**Explanation:** Within the **dimensional model of emotion** (Russell's Circumplex Model; the VAD model), **heart rate** is most strongly associated with the **arousal dimension** — the degree of activation or excitation in an emotional state. High-arousal emotions (fear, excitement, anger) tend to increase heart rate, while low-arousal emotions (calm, relaxation, sadness) tend to lower it. Heart rate is a poor discriminator for **valence** (positive vs. negative) since both fear and excitement can raise heart rate similarly.

---

### Question 4

**A key advantage of PPG (Photo-Plethysmography) over ECG is that PPG:**

- A. Provides greater spatial resolution
- **B. Is quicker to attach and less intrusive ✅**
- C. Measures electrical pulses directly
- D. Requires medical-grade gel electrodes

**Answer: B — Is quicker to attach and less intrusive**

**Explanation:** **PPG (Photo-Plethysmography)** measures blood volume changes in the microvascular bed of tissue using light (typically via a fingertip or wrist sensor). Compared to **ECG**, which requires placement of multiple electrodes on the chest with conductive gel, PPG is **far easier to attach, less intrusive, and more comfortable** for everyday use — making it ideal for wearable affective computing applications. The trade-off is that PPG is more susceptible to motion artifacts and is an indirect measure of cardiac activity.

---

### Question 5

**Heart Rate Variability (HRV) measures:**

- A. The average heart rate over the day
- B. The electrical intensity of heart contractions
- **C. The variation in RR intervals between beats ✅**
- D. The number of peaks in each heartbeat waveform

**Answer: C — The variation in RR intervals between beats**

**Explanation:** **Heart Rate Variability (HRV)** refers to the **beat-to-beat variation in the time intervals between consecutive heartbeats** — specifically the **RR intervals** (the time between two successive R-peaks in the ECG waveform). HRV is a rich indicator of autonomic nervous system activity: high HRV generally indicates good autonomic flexibility and a relaxed state, while low HRV is associated with stress, fatigue, or high arousal. HRV is widely used as a biomarker for emotional and cognitive states in affective computing.

---

### Question 6

**A major limitation of ECG/PPG for affect recognition is that they:**

- A. Only measure emotional valence, not arousal
- B. Cannot measure changes over short intervals
- C. Are too invasive for most participants
- **D. Cannot distinguish positive from negative arousal ✅**

**Answer: D — Cannot distinguish positive from negative arousal**

**Explanation:** ECG and PPG both track **arousal-related changes** in the cardiovascular system well — elevated heart rate signals high arousal. However, they **cannot reliably distinguish between positive high-arousal states** (e.g., excitement, joy) **and negative high-arousal states** (e.g., fear, anger), because both produce similar cardiovascular signatures. This **valence ambiguity** is a fundamental limitation, often addressed by combining cardiac signals with other modalities like GSR, facial expressions, or EEG to achieve full emotional characterization.

---

### Question 7

**Physiological signals like HR and GSR are less likely to be consciously manipulated compared to facial expressions.**

- **A. True ✅**
- B. False

**Answer: True**

**Explanation:** **Heart Rate (HR)** and **Galvanic Skin Response (GSR)** are mediated by the **autonomic nervous system** — a system that operates largely below the threshold of conscious control. While trained individuals (e.g., through biofeedback) can exert limited influence over these signals, in general they are far **less susceptible to deliberate manipulation** than facial expressions, which involve voluntary muscles and can be consciously posed or suppressed. This is why physiological signals are considered more reliable ground-truth indicators of emotional states.

---

### Question 8

**ECG-based heart rate measurements are more accurate than PPG because:**

- **A. They measure electrical activity directly ✅**
- B. They require fewer sensors
- C. They work better at long distances
- D. They are less sensitive to motion artifacts

**Answer: A — They measure electrical activity directly**

**Explanation:** **ECG (Electrocardiogram)** directly measures the **electrical signals** generated by the heart's depolarization and repolarization cycles, producing a precise waveform (including the characteristic P-QRS-T complex). This direct electrical measurement provides a highly accurate representation of each heartbeat. **PPG**, by contrast, indirectly infers heart rate from **optical changes in blood volume** — making it slightly less precise and more vulnerable to motion artifacts and signal noise. ECG remains the gold standard for cardiac measurement in affective computing research.

---

### Question 9

**GSR can reveal whether the emotional state is positive or negative.**

- A. True
- **B. False ✅**

**Answer: False**

**Explanation:** **GSR (Galvanic Skin Response)**, also known as **Electrodermal Activity (EDA)** or **Skin Conductance Response (SCR)**, measures changes in the electrical conductance of the skin caused by sweat gland activity — which is modulated by sympathetic nervous system arousal. GSR is a sensitive indicator of **arousal level** (high arousal → increased GSR) but **cannot distinguish between positive and negative emotions** — both excitement (positive) and fear (negative) can produce identical GSR elevations. This is the same valence-ambiguity limitation shared by cardiac measures.

---

### Question 10

**Low HRV is typically associated with:**

- A. Relaxation
- **B. Strong stress or arousal ✅**
- C. Enhanced emotional control
- D. Deep sleep

**Answer: B — Strong stress or arousal**

**Explanation:** **Low Heart Rate Variability (HRV)** indicates that the time intervals between heartbeats are becoming more uniform and less variable — a signature of **heightened sympathetic nervous system activity** (the "fight-or-flight" response). This is typically observed during states of **stress, anxiety, or high arousal**, where the sympathetic system dominates and overrides the naturally variable, parasympathetically-driven rhythm. Conversely, **high HRV** is associated with relaxation, emotional regulation, and parasympathetic dominance — the opposite of what low HRV indicates.

---

## Summary Table

| Q#  | Topic                                     | Correct Answer                                              | Score |
| :-: | ----------------------------------------- | ----------------------------------------------------------- | :---: |
|  1  | Value of Physiological Signals            | A — Cannot be voluntarily controlled                        |  1/1  |
|  2  | Not a Physiological Measure               | D — Eye-blink frequency                                     |  1/1  |
|  3  | Heart Rate & Emotion Dimension            | B — Arousal                                                 |  1/1  |
|  4  | PPG Advantage over ECG                    | B — Quicker to attach, less intrusive                       |  1/1  |
|  5  | HRV Definition                            | C — Variation in RR intervals between beats                 |  1/1  |
|  6  | Limitation of ECG/PPG                     | D — Cannot distinguish positive from negative arousal       |  1/1  |
|  7  | HR & GSR vs. Facial Expressions           | True — Less susceptible to conscious manipulation           |  1/1  |
|  8  | ECG Accuracy over PPG                     | A — Measures electrical activity directly                   |  1/1  |
|  9  | GSR & Valence                             | False — GSR cannot reveal positive vs. negative emotion     |  1/1  |
| 10  | Low HRV Association                       | B — Strong stress or arousal                                |  1/1  |

**Total Score: 10/10**

---

_Reference: Affective Computing — Week 7 Lecture Materials_
