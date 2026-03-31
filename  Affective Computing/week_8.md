# Affective Computing

## Week 8 : Assignment 8 — Detailed Solution

---

### Question 1

**Skin Conductance (GSR/EDA) measures changes primarily due to:**

- **A. Sweat gland activity ✅**
- B. Body temperature
- C. Blood pressure
- D. Respiration depth

**Answer: A — Sweat gland activity**

**Explanation:** **Galvanic Skin Response (GSR)**, also known as **Electrodermal Activity (EDA)**, measures changes in the **electrical conductance of the skin** that are primarily driven by **sweat gland activity**. The eccrine sweat glands — particularly those on the palms and fingertips — are innervated by the **sympathetic nervous system** and respond to emotional arousal by secreting sweat, which increases the skin's electrical conductivity. GSR does not measure body temperature, blood pressure, or respiration directly.

---

### Question 2

**In GSR signals, the fast, event-related component is called:**

- A. SCL (Skin Conductance Level)
- B. EDL (Electrodermal Level)
- **C. SCR (Skin Conductance Response) ✅**
- D. ERV (Emotional Response Value)

**Answer: C — SCR (Skin Conductance Response)**

**Explanation:** GSR/EDA signals are decomposed into two main components: the **tonic component** called **SCL (Skin Conductance Level)**, which reflects the slowly-varying baseline conductance, and the **phasic component** called **SCR (Skin Conductance Response)**, which captures **fast, event-related changes** triggered by discrete stimuli or emotional events. SCRs are the rapid, transient peaks superimposed on the slower SCL baseline and are the primary measure of interest in emotion detection experiments.

---

### Question 3

**GSR can reveal whether the emotional state is positive or negative.**

- A. True
- **B. False ✅**

**Answer: False**

**Explanation:** **GSR (Galvanic Skin Response)** is a reliable indicator of **emotional arousal** — the intensity or activation level of an emotional state — but it **cannot distinguish between positive and negative emotions** (valence). Both excitement (positive, high arousal) and fear (negative, high arousal) produce similar increases in skin conductance. To determine valence, additional modalities such as facial expressions, EEG, or self-reports are required.

---

### Question 4

**Skin conductance responses (SCR) correspond to:**

- A. Slow tonic changes in conductivity
- **B. Rapid, event-related changes triggered by stimuli ✅**
- C. Changes due to respiration cycles
- D. Variations caused only by temperature

**Answer: B — Rapid, event-related changes triggered by stimuli**

**Explanation:** **Skin Conductance Responses (SCRs)** are the **phasic** (fast, transient) components of the electrodermal signal. They are **rapid increases in skin conductance** that occur in response to **discrete stimuli** — such as an emotional image, a startling sound, or a stressful event. SCRs typically peak within 1–5 seconds after stimulus onset and reflect the momentary activation of the sympathetic nervous system. They are distinct from the **tonic** SCL, which represents the slow-moving baseline level of conductance.

---

### Question 5

**The most emotionally reactive sweat glands are located on:**

- A. Forehead
- B. Knees
- **C. Palms and soles ✅**
- D. Back

**Answer: C — Palms and soles**

**Explanation:** The **eccrine sweat glands** located on the **palms of the hands and soles of the feet** are the most **emotionally reactive** sweat glands in the body. Unlike thermoregulatory sweat glands found elsewhere on the body, these palmar and plantar glands are primarily controlled by **emotional and psychological stimuli** rather than temperature. This is why GSR/EDA sensors are typically placed on the fingers or palm — these locations provide the strongest and most reliable emotional arousal signals.

---

### Question 6

**In EEG signals, alpha-band power has what relationship with cortical activity?**

- A. Direct (more alpha = more activity)
- **B. Inverse (more alpha = less activity) ✅**
- C. No relationship
- D. Only positive emotions change alpha

**Answer: B — Inverse (more alpha = less activity)**

**Explanation:** **Alpha waves** (8–13 Hz) in EEG are associated with a state of **relaxed wakefulness** and **cortical idling**. There is an **inverse relationship** between alpha-band power and cortical activity: **higher alpha power** indicates **less cortical activation** (the brain region is relatively idle), while **lower alpha power** (alpha suppression or desynchronization) indicates **greater cortical engagement and processing**. This principle is fundamental to EEG-based emotion and cognitive state recognition in affective computing.

---

### Question 7

**In multimodal emotion recognition, early fusion requires:**

- A. Combining classifier decisions
- B. Using only a single modality
- C. Late-stage hypothesis selection
- **D. Synchronizing signals before concatenation ✅**

**Answer: D — Synchronizing signals before concatenation**

**Explanation:** **Early fusion** (also called feature-level fusion) in multimodal emotion recognition involves **combining feature vectors from different modalities into a single unified feature vector** before feeding it to a classifier. This approach **requires temporal synchronization** of all modality signals — since features from audio, video, and physiological signals must be aligned in time before they can be concatenated. This is in contrast to **late fusion** (decision-level fusion), which combines the output decisions of separate per-modality classifiers.

---

### Question 8

**Slow fusion is beneficial because it:**

- A. Avoids all redundancy across modalities
- B. Assumes strict independence of cues
- **C. Exploits correlations while relaxing synchronization requirements ✅**
- D. Works only with visual cues

**Answer: C — Exploits correlations while relaxing synchronization requirements**

**Explanation:** **Slow fusion** is an intermediate strategy between early and late fusion. It integrates information from different modalities **gradually over time**, allowing the model to **exploit cross-modal correlations and temporal dependencies** without requiring the strict frame-level synchronization demanded by early fusion. This makes it more practical and robust for real-world affective computing applications, where perfect temporal alignment across modalities (e.g., audio, video, physiological signals) is often difficult to achieve.

---

### Question 9

**The SEMAINE project aims to train a system that:**

- **A. Engages in multimodal social interaction as a Sensitive Artificial Listener ✅**
- B. Predicts emotional valence using only speech
- C. Detects emotions using physiological sensors alone
- D. Generates emotional facial expressions automatically

**Answer: A — Engages in multimodal social interaction as a Sensitive Artificial Listener**

**Explanation:** The **SEMAINE project** (Sustained Emotionally coloured Machine-human Interaction using Nonverbal Expression) is a major multimodal affective computing project that developed the concept of a **Sensitive Artificial Listener (SAL)**. The system is designed to engage in **multimodal social interactions** with human users by perceiving and responding to emotional cues from multiple channels — including facial expressions, speech prosody, and head gestures — simulating emotionally appropriate conversational behavior.

---

### Question 10

**A challenge in multimodal affect data collection is:**

- A. Too many synchronized datasets exist
- B. Overabundance of annotated corpora
- C. Lack of available audio signals
- **D. Getting spontaneous, subtle expressions with aligned modalities ✅**

**Answer: D — Getting spontaneous, subtle expressions with aligned modalities**

**Explanation:** One of the greatest challenges in multimodal affective computing is **collecting naturalistic data** that captures **spontaneous, subtle emotional expressions** across multiple modalities with proper **temporal alignment**. Most existing datasets contain exaggerated, acted emotions that do not reflect real-world affect. Collecting genuine, spontaneous expressions is difficult because they are fleeting and subtle, and ensuring all modalities (audio, video, physiological signals) are properly synchronized adds significant technical complexity.

---

## Summary Table

| Q#  | Topic                                     | Correct Answer                                              | Score |
| :-: | ----------------------------------------- | ----------------------------------------------------------- | :---: |
|  1  | GSR/EDA Primary Measure                   | A — Sweat gland activity                                    |  1/1  |
|  2  | Fast GSR Component                        | C — SCR (Skin Conductance Response)                         |  1/1  |
|  3  | GSR & Valence                             | False — GSR cannot reveal positive vs. negative             |  1/1  |
|  4  | SCR Characteristics                       | B — Rapid, event-related changes triggered by stimuli       |  1/1  |
|  5  | Emotionally Reactive Sweat Glands         | C — Palms and soles                                         |  1/1  |
|  6  | EEG Alpha-Band & Cortical Activity        | B — Inverse (more alpha = less activity)                    |  1/1  |
|  7  | Early Fusion Requirement                  | D — Synchronizing signals before concatenation              |  1/1  |
|  8  | Slow Fusion Benefit                       | C — Exploits correlations, relaxes synchronization          |  1/1  |
|  9  | SEMAINE Project Goal                      | A — Sensitive Artificial Listener                           |  1/1  |
| 10  | Multimodal Data Collection Challenge      | D — Getting spontaneous, subtle expressions with alignment  |  1/1  |

**Total Score: 10/10**

---

_Reference: Affective Computing — Week 8 Lecture Materials_
