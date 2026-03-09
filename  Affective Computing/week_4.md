# Affective Computing

## Week 4 : Assignment 4 — Detailed Solution

---

### Question 1

**Which input modality is considered the most informative and non-intrusive for Facial Emotion Recognition (FER)?**

- A. EMG
- **B. Camera ✅**
- C. EEG
- D. Earables

**Answer: B — Camera**

**Explanation:** Cameras are the most informative and non-intrusive modality for FER because they capture rich visual data (facial geometry, texture, motion) without requiring any sensors to be attached to the participant. This makes them ideal for naturalistic and scalable emotion recognition.

---

### Question 2

**Dynamic FER generally outperforms static FER because it:**

- A. Uses more sensors
- B. Ignores temporal variations
- **C. Captures expression transitions over time ✅**
- D. Removes noise from peak frames

**Answer: C — Captures expression transitions over time**

**Explanation:** Dynamic FER analyzes video sequences rather than single frames, allowing it to capture **expression transitions and temporal dynamics** — such as onset, apex, and offset of an expression. This temporal information provides richer cues for distinguishing between emotions than a single static snapshot.

---

### Question 3

**The first step in conventional FER pipelines typically involves:**

- A. Expression classification
- B. Texture smoothing
- **C. Face and facial component detection ✅**
- D. Motion estimation

**Answer: C — Face and facial component detection**

**Explanation:** The first step in a conventional FER pipeline is **face detection and facial component localization** (eyes, nose, mouth, etc.). Before any features can be extracted or expressions classified, the system must identify and isolate the face region and its key landmarks from the input image or video frame.

---

### Question 4

**Deep-learning-based FER systems reduce reliance on:**

- **A. Face-physics-based models and preprocessing ✅**
- B. Landmark detectors
- C. Data augmentation
- D. GPU resources

**Answer: A — Face-physics-based models and preprocessing**

**Explanation:** Deep learning–based FER systems learn features directly from raw data through end-to-end training, significantly reducing the need for **handcrafted face-physics-based models** and extensive **preprocessing pipelines** (such as manual feature engineering, geometric normalization, or physics-based muscle models).

---

### Question 5

**Macro expressions typically last:**

- A. Less than 1/2 second
- B. 5–10 seconds
- C. Longer than 10 seconds
- **D. Between 1/2 and 4 seconds ✅**

**Answer: D — Between 1/2 and 4 seconds**

**Explanation:** **Macro expressions** are full, deliberate facial expressions that typically last between **0.5 and 4 seconds**. They are easily observable and represent the standard expressions studied in most FER research. This distinguishes them from **micro expressions**, which last less than 0.5 seconds.

---

### Question 6

**Micro expressions are difficult to detect because they:**

- A. Last longer than macro expressions
- B. Are consciously controlled
- **C. Are brief and often involuntary ✅**
- D. Do not involve facial muscles

**Answer: C — Are brief and often involuntary**

**Explanation:** **Micro expressions** are extremely difficult to detect because they are **very brief** (typically lasting less than 1/2 second) and occur **involuntarily**, often when a person is trying to suppress or conceal their true emotions. Their fleeting nature makes them challenging for both humans and automated systems to recognize.

---

### Question 7

**Facial Action Coding System (FACS) is based on:**

- **A. Facial muscle movements ✅**
- B. Wrinkle depth measurements
- C. Tracking head pose only
- D. Eye aperture changes exclusively

**Answer: A — Facial muscle movements**

**Explanation:** **FACS**, developed by Ekman and Friesen (1978), is an anatomically-based system that describes facial expressions in terms of **Action Units (AUs)** — each AU corresponds to the movement of one or more underlying facial muscles. It provides an objective, comprehensive framework for coding any facial expression.

---

### Question 8

**Which appearance-based feature descriptor is sensitive to lighting variations?**

- A. SIFT
- **B. Raw pixel intensity values ✅**
- C. Gabor filters
- D. HOG

**Answer: B — Raw pixel intensity values**

**Explanation:** **Raw pixel intensity values** are highly sensitive to changes in **lighting conditions** because they directly represent the brightness at each pixel without any normalization or invariance. Engineered descriptors like SIFT, HOG, and Gabor filters are specifically designed to be more robust to illumination changes.

---

### Question 9

**Optical flow is primarily used to extract:**

- A. Static shape features
- B. Texture gradients
- **C. Motion-based features ✅**
- D. High-resolution appearance cues

**Answer: C — Motion-based features**

**Explanation:** **Optical flow** computes the apparent motion of pixels between consecutive video frames, producing a vector field that represents the direction and magnitude of movement. In FER, it is used to extract **motion-based features** that capture the dynamics of facial expressions — such as muscle contractions, eyebrow raises, and lip movements.

---

### Question 10

**Geometric features alone are sometimes insufficient because different AUs can produce similar landmark changes.**

- **A. True ✅**
- B. False

**Answer: True**

**Explanation:** Different **Action Units (AUs)** can produce similar shifts in facial landmark positions, making geometric features alone ambiguous for distinguishing between certain AUs or expressions. For example, both smiling and grimacing may move mouth landmarks similarly. This is why combining geometric features with **appearance-based features** (texture, intensity patterns) improves FER accuracy.

---

## Summary Table

| Q#  | Topic                         | Correct Answer                                        |
| :-: | ----------------------------- | ----------------------------------------------------- |
|  1  | FER Input Modality            | B — Camera (most informative, non-intrusive)          |
|  2  | Dynamic vs Static FER         | C — Captures expression transitions over time         |
|  3  | Conventional FER Pipeline     | C — Face and facial component detection               |
|  4  | Deep Learning FER Advantage   | A — Reduces reliance on physics-based models          |
|  5  | Macro Expression Duration     | D — Between 1/2 and 4 seconds                         |
|  6  | Micro Expression Detection    | C — Brief and involuntary                             |
|  7  | FACS Basis                    | A — Facial muscle movements                           |
|  8  | Lighting-Sensitive Feature    | B — Raw pixel intensity values                        |
|  9  | Optical Flow Usage            | C — Motion-based features                             |
| 10  | Geometric Features Limitation | True — Different AUs produce similar landmark changes |

---

_Reference: Affective Computing — Week 4 Lecture Materials_
