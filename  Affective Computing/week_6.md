# Affective Computing

## Week 6 : Assignment 6 — Detailed Solution

---

### Question 1

**ANEW is a categorical lexicon used to label text with Ekman's six universal emotions.**

- A. True
- **B. False ✅**

**Answer: False**

**Explanation:** **ANEW (Affective Norms for English Words)** is a **dimensional** lexicon — it rates words along three dimensions: **Valence** (pleasure–displeasure), **Arousal** (excited–calm), and **Dominance** (controlled–in-control), following the **VAD (Valence-Arousal-Dominance)** model. It is **not** a categorical lexicon tied to Ekman's six universal emotions (anger, disgust, fear, happiness, sadness, surprise). Categorical emotion lexicons include resources like the NRC Emotion Lexicon (EmoLex).

---

### Question 2

**According to Poffenberger & Barrows (1924), upward-moving lines tend to evoke which feeling?**

- A. Calmness
- **B. Joy ✅**
- C. Fear
- D. Anger

**Answer: B — Joy**

**Explanation:** Poffenberger & Barrows (1924) conducted early studies on how visual line directions and shapes evoke emotional responses. They found that **upward-moving or ascending lines** tend to evoke feelings of **joy and happiness**, while downward-moving lines tend to evoke sadness. This research is foundational to understanding how visual form communicates affect — relevant to affective computing in typography and visual design.

---

### Question 3

**Juni & Gross (2008) found that articles were perceived as more satirical when written in:**

- A. Arial
- B. Georgia
- **C. Times New Roman ✅**
- D. Verdana

**Answer: C — Times New Roman**

**Explanation:** Juni & Gross (2008) demonstrated that **font choice influences the emotional and tonal interpretation of text**. Participants perceived articles written in **Times New Roman** as more satirical compared to other fonts. This highlights how typography is not merely aesthetic but carries **affective connotations** — a key insight for text-based affective computing, where even the visual presentation of text can influence perceived emotional tone.

---

### Question 4

**Relative Subjective Duration (RSD) experiments showed that good typography led participants to:**

- A. Underestimate reading time less
- B. Overestimate reading time greatly
- **C. Underestimate reading time more ✅**
- D. Read significantly slower

**Answer: C — Underestimate reading time more**

**Explanation:** **Relative Subjective Duration (RSD)** measures how participants perceive the passage of time while reading. Research showed that **good typography** (well-designed, readable text) caused participants to **underestimate reading time more** — meaning time seemed to pass faster when text was well-formatted. This "time flies" effect reflects the role of typography in producing a positive, engaging reading experience — a clear affective response to visual text properties.

---

### Question 5

**Why is positive/negative sentiment analysis often insufficient?**

- **A. Emotions with similar polarity (e.g., fear vs. anger) differ in relevance and meaning ✅**
- B. Most texts contain no sentiment
- C. It cannot detect sarcasm
- D. It is computationally expensive

**Answer: A — Emotions with similar polarity (e.g., fear vs. anger) differ in relevance and meaning**

**Explanation:** Binary **positive/negative sentiment analysis** collapses all negative emotions (fear, anger, disgust, sadness) into a single category and all positive emotions (joy, surprise, anticipation) into another. However, these emotions carry **very different meanings and have distinct real-world relevance** — for example, fear and anger are both negative but require entirely different responses. Fine-grained **emotion recognition** is therefore necessary for nuanced applications like mental health monitoring, customer experience analysis, and human-computer interaction.

---

### Question 6

**Implicit expressions of emotions (Lee, 2015) refer to:**

- A. Emotions directly stated via adjectives
- B. Physiological signals embedded in text
- C. Metaphors expressing emotional states
- **D. Emotion conveyed without explicit emotional words ✅**

**Answer: D — Emotion conveyed without explicit emotional words**

**Explanation:** Lee (2015) distinguishes between **explicit** and **implicit** emotional expressions in text. **Explicit expressions** directly state emotions using emotion words (e.g., "I am sad"). **Implicit expressions** convey emotion **without using explicit emotional vocabulary** — through descriptions of situations, actions, or outcomes that imply an emotional state (e.g., "She stared at the empty chair where he used to sit"). Detecting implicit emotions is significantly more challenging for automated systems and requires deeper semantic and contextual understanding.

---

### Question 7

**Metaphorical emotional expressions create challenges because:**

- **A. Their meaning cannot be inferred from literal text alone ✅**
- B. They are too rare to train on
- C. They cannot be represented in WordNet
- D. They always express anger

**Answer: A — Their meaning cannot be inferred from literal text alone**

**Explanation:** **Metaphorical emotional expressions** (e.g., "I'm drowning in grief," "She was on top of the world") convey emotion through figurative language. Their **meaning cannot be derived from the literal interpretation** of the words. Standard lexicon-based and bag-of-words approaches fail to capture these because the surface words may carry no intrinsic emotional valence. Resolving metaphors requires pragmatic and world knowledge, making them a significant challenge for automated text emotion recognition systems.

---

### Question 8

**The ISEAR database consists of reports from participants describing:**

- A. Metaphorical uses of emotional expressions
- **B. Situations where they experienced one of seven major emotions ✅**
- C. Annotated news headlines
- D. Product reviews labeled for polarity

**Answer: B — Situations where they experienced one of seven major emotions**

**Explanation:** The **ISEAR (International Survey on Emotion Antecedents and Reactions)** database was collected by Scherer & Wallbott (1994). Participants from diverse cultural backgrounds were asked to describe **situations in which they experienced one of seven major emotions**: joy, fear, anger, sadness, disgust, shame, and guilt. ISEAR is a key benchmark dataset for text-based emotion recognition, particularly useful because of its cross-cultural and narrative nature.

---

### Question 9

**SentiWordNet focuses primarily on:**

- A. Dimensional emotion modeling
- B. Detecting metaphors in textual data
- C. Context-sensitive emotional sequences
- **D. Polarity (positive, negative, objective) of terms ✅**

**Answer: D — Polarity (positive, negative, objective) of terms**

**Explanation:** **SentiWordNet** is a lexical resource built on top of **WordNet** that assigns three sentiment scores to each synset: **positive**, **negative**, and **objective** (neutral). It is primarily designed for **polarity-based sentiment analysis** rather than fine-grained emotion detection. Each synset entry has scores summing to 1.0 across these three dimensions. SentiWordNet is widely used in opinion mining and sentiment analysis but does not model dimensional affect (like ANEW) or categorical emotions (like NRC EmoLex).

---

### Question 10

**For unsupervised emotion recognition using lexicons, the text emotion is assigned by:**

- A. Counting how many emotional words appear
- **B. Finding the class with highest cosine similarity to the text vector ✅**
- C. Selecting the emotion with the highest frequency in ANEW
- D. Applying rule-based keyword matching only

**Answer: B — Finding the class with highest cosine similarity to the text vector**

**Explanation:** In **unsupervised lexicon-based emotion recognition**, each emotion class is represented as a vector (using the emotion words associated with that class from a lexicon). The input text is also represented as a vector. The text is then assigned to the **emotion class whose vector has the highest cosine similarity** to the text vector. This approach avoids the need for labeled training data and leverages the semantic structure encoded in emotion lexicons to perform classification in a fully unsupervised manner.

---

## Summary Table

| Q#  | Topic                                      | Correct Answer                                              | Score |
| :-: | ------------------------------------------ | ----------------------------------------------------------- | :---: |
|  1  | ANEW Lexicon Type                          | False — ANEW is dimensional, not categorical                |  1/1  |
|  2  | Poffenberger & Barrows (1924)              | B — Joy                                                     |  1/1  |
|  3  | Juni & Gross (2008) Font Study             | C — Times New Roman                                         |  1/1  |
|  4  | Relative Subjective Duration (RSD)         | C — Underestimate reading time more                         |  1/1  |
|  5  | Limitations of Positive/Negative Sentiment | A — Emotions of similar polarity differ in meaning          |  1/1  |
|  6  | Implicit Emotional Expressions (Lee, 2015) | D — Emotion without explicit emotional words                |  1/1  |
|  7  | Challenges of Metaphorical Expressions     | A — Meaning cannot be inferred from literal text            |  1/1  |
|  8  | ISEAR Database                             | B — Situations evoking seven major emotions                 |  1/1  |
|  9  | SentiWordNet Focus                         | D — Polarity (positive, negative, objective)                |  1/1  |
| 10  | Unsupervised Lexicon-Based Recognition     | B — Highest cosine similarity to text vector                |  1/1  |

**Total Score: 10/10**

---

_Reference: Affective Computing — Week 6 Lecture Materials_
