# Affective Computing

## Week 5 : Assignment 5 — Detailed Solution

---

### Question 1

**Which of the following is not an application of speech in affective computing?**

- A. Driver safety monitoring
- B. Mobile communications
- C. Diagnostic tools for therapists
- **D. Face recognition unlocking ✅**

**Answer: D — Face recognition unlocking**

**Explanation:** Face recognition unlocking is a **visual biometric** application, not a speech-based one. Driver safety monitoring, mobile communications, and diagnostic tools for therapists all leverage speech and vocal cues for affect recognition.

---

### Question 2

**According to Borden et al. (1994), "how it is said" refers to:**

- A. The linguistic meaning of the words
- **B. Paralinguistic information reflecting emotional state ✅**
- C. Speaker identity characteristics
- D. Speech segmentation rules

**Answer: B — Paralinguistic information reflecting emotional state**

**Explanation:** Borden et al. distinguish between _what_ is said (linguistic content) and _how_ it is said. The "how" refers to **paralinguistic cues** — such as tone, pitch, rhythm, and intensity — that convey the speaker's emotional state beyond the literal meaning of the words.

---

### Question 3

**Natural emotional speech databases primarily include:**

- A. Speech from trained actors
- B. Emotionally synthesized speech
- **C. Spontaneous speech from real-world scenarios ✅**
- D. Scripted dialogues recorded in studios

**Answer: C — Spontaneous speech from real-world scenarios**

**Explanation:** Natural emotional speech databases collect **spontaneous, unscripted speech** from real-world situations (e.g., call center recordings, interviews, field recordings). This ensures high ecological validity, unlike acted databases which may contain exaggerated or artificial expressions.

---

### Question 4

**Positive emotions always produce lower variability in pitch.**

- **A. True ✅ (Correct Answer)**
- B. False ❌ (Wrong Answer)

**Answer: True**

> ⚠️ **Note:** The answer selected during the quiz was **False**, which was marked incorrect. The accepted answer is **True**.

**Explanation:** Research indicates that positive emotions tend to produce **lower variability in pitch (f0)** compared to negative emotions like anger or fear, which typically show higher pitch variability. Positive emotional states like contentment and calm happiness are associated with more stable, less variable pitch contours.

---

### Question 5

**The Berlin Emotional Speech Database contains recordings of:**

- A. Children interacting with robots
- **B. Professional actors producing emotional German sentences ✅**
- C. North American speakers producing neutral statements
- D. Patients and doctors in clinical settings

**Answer: B — Professional actors producing emotional German sentences**

**Explanation:** The **Berlin Emotional Speech Database (EMO-DB)** is one of the most widely used acted emotional speech datasets. It contains recordings of **10 professional German actors** producing sentences in seven emotional states: anger, boredom, disgust, fear, happiness, sadness, and neutral.

---

### Question 6

**Prosody features include:**

- A. MFCCs
- B. SIFT descriptors
- **C. Fundamental frequency and short-term energy ✅**
- D. Visual intensity curves

**Answer: C — Fundamental frequency and short-term energy**

**Explanation:** **Prosody features** capture the rhythm, intonation, and stress patterns of speech. Key prosodic features include **fundamental frequency (f0)** — which corresponds to perceived pitch — and **short-term energy** — which relates to loudness. MFCCs are spectral features, not prosodic ones.

---

### Question 7

**MFCCs are primarily used to represent:**

- **A. Resonant spectral characteristics ✅**
- B. Rhythm and intonation patterns
- C. Speaker identity features
- D. Amplitude variations across time

**Answer: A — Resonant spectral characteristics**

**Explanation:** **Mel-Frequency Cepstral Coefficients (MFCCs)** represent the **resonant spectral characteristics** of speech by modeling the shape of the vocal tract's spectral envelope on a perceptually-motivated mel frequency scale. They capture formant-related information critical for distinguishing both phonemes and emotional vocal qualities.

---

### Question 8

**Positive voices typically show which characteristic?**

- A. Low pitch and low formant frequencies
- B. Low speech rate
- C. Flat and monotone amplitude
- **D. High loudness variability and high formant frequencies ✅**

**Answer: D — High loudness variability and high formant frequencies**

**Explanation:** Research on vocal correlates of positive emotions shows that positive voices tend to exhibit **high loudness variability** (dynamic amplitude changes) and **higher formant frequencies**, reflecting more animated and energetic vocal production compared to neutral or sad speech.

---

### Question 9

**A key problem with global normalization of f0 across all speakers is that it:**

- **A. May blur emotional differences due to speaker-specific traits ✅**
- B. Reduces background noise
- C. Is too computationally expensive
- D. Requires manual annotation

**Answer: A — May blur emotional differences due to speaker-specific traits**

**Explanation:** Global normalization of fundamental frequency (f0) across all speakers can **blur emotional differences** because individual speakers have vastly different baseline pitch ranges. A high-pitched neutral voice for one speaker may overlap with an excited voice of another, causing speaker-specific emotional cues to be lost in the normalization process.

---

### Question 10

**One major open challenge in speech-based affect recognition is:**

- A. Oversupply of natural databases
- **B. Inter- and intra-speaker variability ✅**
- C. Perfect cross-lingual generalization
- D. Excessive real-time deployment success

**Answer: B — Inter- and intra-speaker variability**

**Explanation:** **Inter-speaker variability** (differences between speakers) and **intra-speaker variability** (differences within the same speaker across contexts) remain major open challenges. Different people express the same emotion differently, and the same person may vary their expression depending on context, making robust generalization difficult.

---

## Summary Table

| Q#  | Topic                            | Correct Answer                                          |   Score    |
| :-: | -------------------------------- | ------------------------------------------------------- | :--------: |
|  1  | Speech Applications              | D — Face recognition unlocking (not speech)             |    1/1     |
|  2  | "How it is said" (Borden et al.) | B — Paralinguistic information                          |    1/1     |
|  3  | Natural Speech Databases         | C — Spontaneous real-world speech                       |    1/1     |
|  4  | Positive Emotions & Pitch        | True — Lower pitch variability                          | **0/1** ❌ |
|  5  | Berlin Emotional Speech Database | B — German actors, emotional sentences                  |    1/1     |
|  6  | Prosody Features                 | C — Fundamental frequency and short-term energy         |    1/1     |
|  7  | MFCCs                            | A — Resonant spectral characteristics                   |    1/1     |
|  8  | Positive Voice Characteristics   | D — High loudness variability, high formant frequencies |    1/1     |
|  9  | Global f0 Normalization Problem  | A — Blurs emotional differences                         |    1/1     |
| 10  | Open Challenges                  | B — Inter- and intra-speaker variability                |    1/1     |

**Total Score: 9/10**

---

_Reference: Affective Computing — Week 5 Lecture Materials_
