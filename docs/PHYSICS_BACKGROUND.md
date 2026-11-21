# CERN Project — Physics Background & Personal Research Notes
# الخلفية الفيزيائية وملاحظاتي البحثية

This document contains my personal notes about the physics concepts behind my CERN Proton Collision Anomaly Detection project.

I use it as a reference to understand what my dataset represents, what its features mean physically, and why these features matter for anomaly detection.

**بالعربي:**

الملف ده عبارة عن ملاحظاتي الشخصية لكل المفاهيم الفيزيائية اللي بتقابلني أثناء شغلي على مشروع CERN.

بستخدمه كمرجع أرجعله كل ما أحتاج أفتكر معنى Feature معينة، أو أفهم هي بتمثل إيه فيزيائيًا، وإيه علاقتها بهدف المشروع.

مش لازم أكون متخصصة في Particle Physics، لكن مهم بالنسبة لي أفهم طبيعة البيانات اللي بشتغل عليها، بدل ما أتعامل مع الأرقام من غير ما أفهم معناها.

---

## 1. Understanding the Project

### 1.1 What Happens at CERN?

At CERN's Large Hadron Collider (LHC), high-energy protons collide with each other, producing various particles that travel in different directions.

Particle detectors, such as the CMS detector, record information about these collisions.

**بالعربي:**

عشان أفهم طبيعة الداتا اللي بشتغل عليها، لازم أفتكر الأول إيه اللي بيحصل في CERN.

البروتونات بتتصادم مع بعض بطاقة عالية جدًا داخل الـ LHC، والتصادم ده ممكن ينتج عنه جسيمات كتير بتتحرك في اتجاهات مختلفة.

الـ Detector بيرصد الجسيمات دي ويسجل خصائصها، زي الطاقة والاتجاه والزخم.

### 1.2 What Does My Dataset Represent?

Each row represents a collision event, while each column represents a physical or kinematic feature describing that event.

**بالعربي:**

الـ Dataset اللي بشتغل عليها عبارة عن جدول:

- Each Row = One Collision Event.
- Each Column = A Physical Feature.
- Each Value = The measured or reconstructed value of that feature.

يعني كل صف بيمثل تصادم واحد، وكل عمود بيوصف خاصية فيزيائية مرتبطة بالتصادم ده.

### 1.3 My Project Objective

My objective is to apply Unsupervised Machine Learning techniques to identify unusual collision events that may deserve further investigation.

**بالعربي:**

هدفي إني أستخدم Unsupervised Machine Learning عشان أكتشف الأحداث اللي سلوكها مختلف عن النمط المعتاد في البيانات.

لكن لازم أفتكر إن اكتشاف الـ Model لحدث غير معتاد مش معناه بالضرورة إني اكتشفت جسيم جديد.

أنا بحدد أحداث تستحق الدراسة والتحقيق، وبحاول أفهم سبب اختلافها.

---

## 2. Understanding MR (Razor Mass)

### 2.1 What is MR?

MR is a kinematic variable used in the Razor analysis framework in particle physics.

It is constructed using the momenta of two groups of reconstructed particles called Megajets.

It provides an estimate of the characteristic mass/momentum scale of a collision event.

**بالعربي:**

MR اختصار لمتغير اسمه Razor Mass.

لما البروتونات تتصادم، بتنتج جسيمات كتير، والعلماء بيجمعوا الـ Jets والأجسام المرصودة في مجموعتين اسمهم:

- Megajet 1
- Megajet 2

الـ MR بيستخدم معلومات الحركة والزخم بتاعة المجموعتين دول عشان يحدد مقياس فيزيائي مميز للتصادم.

ببساطة، MR بيديني فكرة عن الـ Mass/Energy Scale المرتبط بالتصادم.

### 2.2 Why is MR Important?

- It helps characterize the kinematic scale of collision events.
- Higher MR values may indicate events with a higher characteristic energy or momentum scale.
- It is useful in searches for new physics, including hypothetical heavy particles.

**بالعربي:**

أنا مهتمة بـ MR لأن بعض الظواهر الفيزيائية اللي العلماء بيدوروا عليها ممكن تنتج أحداث عندها Mass Scale مرتفع.

فلو لقيت أحداث عندها MR عالي، ده ممكن يكون مثير للاهتمام ويستحق التحقيق.

لكن لازم أفتكر إن مش كل MR عالي معناه وجود جسيم جديد.

### 2.3 MR in My Project

I analyze MR to:

- Understand its distribution.
- Identify extreme values.
- Investigate its skewness and long tails.
- Understand how unusual events are distributed across the MR range.

**بالعربي:**

حللت MR باستخدام Histogram وBoxplot عشان أفهم:

- أغلب التصادمات عندها MR كام؟
- هل فيه قيم مرتفعة جدًا؟
- هل التوزيع منحرف ناحية اليمين؟
- هل فيه Long Tail؟
- هل فيه Potential Outliers؟

---

## 3. Understanding Rsq (R Squared)

### 3.1 What is Rsq?

Rsq, commonly written as R², is a kinematic variable used in the Razor analysis framework.

\[
R^2 = \left(\frac{M_T^R}{M_R}\right)^2
\]

Where:

- \(M_R\): Razor mass variable.
- \(M_T^R\): Razor transverse mass variable.

**بالعربي:**

Rsq هو مربع متغير اسمه Razor R.

لازم أفتكر إني هنا مش بتكلم عن R-squared بتاع Regression أو Model Evaluation.

أنا بتكلم عن متغير فيزيائي بيستخدم في تحليل تصادمات الجسيمات.

المعادلة بتعبر عن نسبة بين متغيرين فيزيائيين، وبنربع النسبة دي.

### 3.2 What is Missing Transverse Momentum (MET)?

Missing Transverse Momentum represents an imbalance in the measured transverse momentum of particles produced in a collision.

This imbalance may indicate the presence of particles that escape direct detection.

**بالعربي:**

عشان أفهم Rsq، لازم أفتكر معنى Missing Transverse Momentum.

ممكن يكون فيه جسيمات ناتجة عن التصادم مش بنقدر نرصدها مباشرة.

بنستدل على وجودها من اختلال توازن الزخم في الاتجاه العرضي (Transverse Plane).

ممكن يكون السبب جسيمات زي Neutrinos أو جسيمات افتراضية بتتنبأ بيها بعض النظريات.

### 3.3 Why is Rsq Important?

- It incorporates information about missing transverse momentum.
- It helps characterize the kinematic structure of collision events.
- It is useful in searches for physics beyond the Standard Model, including Supersymmetry (SUSY).

**بالعربي:**

Rsq مهم لأنه بيدخل في حسابه معلومات عن الـ Missing Momentum.

وده بيساعد العلماء يدرسوا الاختلافات بين أنواع الأحداث.

بعض النظريات الفيزيائية، زي SUSY، بتتنبأ بجسيمات ممكن متظهرش مباشرة في الـ Detector.

عشان كده دراسة Rsq مهمة في عمليات البحث دي.

### 3.4 Rsq in My Project

I analyze Rsq to:

- Understand its distribution.
- Calculate statistical boundaries using IQR.
- Identify potential outliers.
- Investigate events with unusually high Rsq values.

**بالعربي:**

حللت Rsq باستخدام:

- Histogram.
- Boxplot.
- Q1 and Q3.
- IQR.
- Upper Fence.
- Potential Outliers.

وهدفي أفهم هل فيه أحداث عندها Rsq مختلف بشكل ملحوظ عن باقي الأحداث.

---

## 4. Understanding the Relationship Between MR and Rsq

MR and Rsq provide complementary information about collision events.

Together, they can be studied using a two-dimensional representation called the Razor Plane.

- X-axis: MR
- Y-axis: Rsq

**بالعربي:**

المتغيرين دول بيكملوا بعض:

| Feature | What does it tell me? |
|---|---|
| MR | Characteristic mass/momentum scale |
| Rsq | Relationship between transverse mass and Razor mass |

لما أرسم MR على المحور الأفقي وRsq على المحور الرأسي، بقدر أشوف توزيع الأحداث في مساحة اسمها Razor Plane.

وده بيساعدني أدرس الاختلاف بين الـ Standard Model Background والـ Potential New Physics Signals.

---

## 5. Important Physics Terminology

| English Term | الشرح بالعربي |
|---|---|
| Collision Event | عملية تصادم واحدة |
| Proton | بروتون، جسيم موجب الشحنة |
| Particle | جسيم |
| Jet | مجموعة جسيمات بتتحرك في اتجاه متقارب |
| Megajet | مجموعة من الأجسام المعاد بناؤها في تحليل Razor |
| Momentum | كمية الحركة |
| Transverse | اتجاه عمودي على مسار حزمة البروتونات |
| Missing Transverse Momentum | اختلال في توازن الزخم العرضي المقاس |
| Detector | جهاز بيرصد الجسيمات وخصائصها |
| Standard Model | النظرية الأساسية للجسيمات الأولية المعروفة |
| SUSY | Supersymmetry، نظرية بتقترح وجود جسيمات إضافية |
| Anomaly | حدث بيختلف عن النمط المتوقع |

---

## 6. Statistical Outliers vs. Physical Anomalies

### 6.1 Statistical Outliers

A statistical outlier is an observation that falls outside a statistically defined range.

For example, the IQR method identifies values beyond:

\[
Q_3 + 1.5 \times IQR
\]

**بالعربي:**

الـ Statistical Outlier هي قيمة بعيدة عن النطاق المعتاد إحصائيًا.

استخدمت IQR عشان أحدد القيم دي.

لكن لازم أفتكر إن ده مش معناه إنها غلط أو لازم أحذفها.

### 6.2 Physical Anomalies

A physical anomaly is an event that behaves differently from what is expected based on the physical model or known background processes.

**بالعربي:**

الـ Physical Anomaly مش مجرد رقم كبير أو صغير.

دي حالة بيكون سلوكها مختلف عن المتوقع فيزيائيًا، وده محتاج دراسة وتحقق.

### 6.3 Important Difference

**Not every statistical outlier is a physical anomaly.**

A statistically unusual event may be:

- A naturally rare but valid event.
- A detector or measurement effect.
- A physically interesting event.
- A potential signal requiring further investigation.

**بالعربي:**

مش كل Outlier هو Anomaly حقيقية.

ممكن تكون قيمة نادرة لكنها طبيعية، أو مشكلة في القياس، أو ظاهرة فيزيائية مهمة.

عشان كده مش هحذف الـ Outliers بشكل تلقائي.

هدفي أفهمها وأحقق فيها قبل ما أخد قرار بشأنها.

---

## 7. My Current Analysis Results

### MR Analysis

| Metric | Result |
|---|---|
| Analysis | Distribution and IQR-based outlier inspection |
| Shape | Right-skewed |
| Potential Outliers | 6.49% |

### Rsq Analysis

| Metric | Result |
|---|---:|
| Q1 | 0.0079072 |
| Q3 | 0.0316123 |
| IQR | 0.0237051 |
| Upper Fence | 0.0671700 |
| Potential Outliers | 1,001 |
| Percentage | 4.607% |

These results describe statistical properties of my dataset, not confirmed physical anomalies.

**بالعربي:**

دي النتائج اللي وصلت لها لحد دلوقتي من تحليل MR وRsq.

لازم أفتكر إنها نتائج إحصائية بتوصف البيانات، مش دليل على اكتشاف ظواهر فيزيائية جديدة.

---

## 8. Key Takeaways

1. MR describes a characteristic mass/momentum scale.
2. Rsq incorporates missing transverse momentum information.
3. Both variables are used in the Razor analysis framework.
4. Studying them together provides more information than studying each independently.
5. Statistical outliers are not automatically physical anomalies.
6. Physics knowledge is essential when interpreting Machine Learning results.

**بالعربي:**

- MR بيديني فكرة عن المقياس الفيزيائي للتصادم.
- Rsq بيدخل معلومات عن الـ Missing Momentum.
- الاتنين مهمين في تحليل Razor.
- لازم أفهم الـ Physics قبل ما أفسر نتائج الـ ML.
- مش هحذف أي قيمة لمجرد إنها Outlier.

---

## 9. References & Further Reading

- [CERN Open Data – Razor Filter and Analyzer for SUSY Searches](https://opendata.cern.ch/record/cms-553)
- [CERN – Large Hadron Collider](https://home.cern/science/accelerators/large-hadron-collider)
- [CMS Experiment](https://cms.cern/)

---

*These are my personal learning notes. I will update this document as I explore more physics concepts and verify feature definitions against the exact dataset and CMS analysis used in my project.*


---

**Prepared and documented by:**  
Basmala Hussein  
Software Industry & Multimedia Student  
Alexandria University

*Personal Research Notes — CERN Project*