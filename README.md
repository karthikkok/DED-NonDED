# *Title: Predicting the Severity Level of Dry Eye Disease (DED) in Individuals.*


**Objective:**

Dry Eye Disease (DED) is a common condition affecting millions of individuals worldwide, leading to discomfort, irritation, and potential vision problems. The severity of DED varies significantly from one person to another, making personalized diagnosis and treatment crucial for effective management.

The objective of this project is to predict the severity level of Dry Eye Disease (DED) in individuals based on a set of medical, behavioral, and demographic features. By accurately classifying the severity of DED (e.g., mild, moderate, severe, normal), healthcare providers can optimize treatment strategies and improve patient outcomes.

**Target Variable:**

The target variable for this project is the DED severity level, which can be categorized into distinct classes (e.g., mild, moderate, severe, normal). This target variable will depend on factors such as clinical measurements (e.g., tear break-up time (TBUT), Schirmer test, OSDI), and demographic information.

**Goal:**

The goal is to develop a robust predictive model capable of classifying individuals into appropriate DED severity categories. The model should be interpretable, reliable, and applicable in a clinical setting, enabling healthcare professionals to make data-driven decisions for patient management and care.

---

[DED Severity Prediction App Link](https://karthikkok-ded-nonded-me6iwghjst2dnaep3k24d8.streamlit.app/)

---

## Insights :


**Age :**
- Similar Age distribution between DED & NON DED
- Individuals with age <20 are facing DED in more number when compared to age > 20

**Gender :**
- Similar chances to both Females and Males to get DED 
- Even the severity level is similar. But there’s only less difference.
  - Females have more chances of getting Mild, Moderate severity level.
  - Males have high changes of Severe Severity level.

**Device types Used :**
- Individuals using (Gaming console, Smartphone, tablet), (Tablet, Smartphone) have more chances of DED. Less chances of DED for computer users.
- More chance of DED Severity level : SEVERE, MODERATE

**Average daily usage hours :**
- There is no proper relation between hour of usage and DED severity level. There is equal chance to every average hour.
- DED severity : There is equal chance to all severity levels

**Years of digital device usage :**
- There is non proper correlation between years of digital device usage and DED severity.
- DED severity : There is equal chance to all severity levels

**OSDI total score :**

- OSDI score between 0 - 20 : NON DED
- OSDI score between 60 - 100 : DED 

There is equal chance to all severity levels
- When OSDI `Score > 85` severity levels = Moderate, Severe
- Female are more likely to get `moderate` and `mild` severity when OSDI score is < 80
- Where as Males get SEVERE severity level, when OSDI score is > 80

**Schirmer Test  TBUT Test (Left & Right Eye) :**

- Schirmer's score between 0 - 5 : DED
- schirmer's score between 10 - 15 : NON DED
+ TBUT Test score between 0 - 5 : DED 
+ TBUT Test score between 10 - 15 : NON DED

There is no exact correlation between TEST score and Severity Level.

**Schirmer test left eye & TBUT Test right eye :**

- More chances of severe severity level when score is 4,5
- Average Values for DED are close to each other.

**Schirmer test right eye & TBUT Test left eye :**

- More chances of Severe severity level when score is 0,1 
- Average Values for DED are close to each other.

**Ocular surface staining Left & Right Eye :**

- If  ocular surface staining score = 0, then severity level is ‘Normal’ 

Left eye :
- If ocular surface left eye score = 2 , more chance of Severe severity level
- If ocular surface left eye score = 1 , more chance of Moderate severity level

Right Eye :
- If ocular surface right eye score = 1 , more chance of Severe severity level
- All other severity levels have equal chances.

**Higly Correlated Columns :** 

DED Diagnosis, OSDI total score, Schirmer Test Left Eye, Schirmer Test Right Eye, TBUT left eye, TBUT right eye, Ocular Surface Staining Left Eye, Ocular Surface Staining Right Eye, DED severity. All these columns are highly correlated with each other

--- 

Model name - Roc Auc Score
-

| Model Name	| Roc_Auc_Score |
| --- | ---- |
| Random Forest Classifier	| 0.996327|
| xgboost |	0.991457|
|	Gradient Boosting	|0.971135|
|Decision Tree	| 0.969673|
|	K-Neighbors Classifier	|0.913048|
|	Logistic Regression	|0.792562|
|	Adaboost	|0.776800|

--- 
**confucion Matrix :**

- RandomForestClassifier

![image](https://github.com/user-attachments/assets/ee5612cd-76dc-429f-b1cf-3be5457f0e2a)

---- 
