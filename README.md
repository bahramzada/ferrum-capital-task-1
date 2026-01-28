# ferrum-capital-task-1  
## Sentiment Analysis – Emotion Classification

---

## 🇦🇿 Azərbaycan dili

### 📖 Layihə haqqında

Bu layihə Ferrum Capital tərəfindən təqdim edilmiş Süni İntellekt üzrə təcrübə proqramına müraciət üçün hazırlanmışdır. Layihənin məqsədi istifadəçi tərəfindən yazılmış cümlələr üzərində sentiment analysis apararaq həmin cümlənin hansı emosiyaya aid olduğunu müəyyən edən model qurmaqdır.

Dataset altı əsas emosiyanı əhatə edir:
- anger  
- fear  
- joy  
- love  
- sadness  
- surprise  

---

### 📂 Layihə strukturu

ferrum-capital-task-1/  
├── data/                # Orijinal və preprocessing-dən keçmiş dataset-lər  
├── models/              # Saxlanılmış model və TF-IDF vektorizatoru (.pkl)  
├── notebooks/           # EDA, Preprocessing, Modeling və Inference notebook-ları 
├── app.py/              # Gradio ilə yazılmış kiçik demo
├── requirements.txt   
└── README.md  

---

### 🔍 İcra olunan mərhələlər

#### 1. Exploratory Data Analysis (EDA)
- Dataset ölçüləri və strukturu analiz edilmişdir  
- Emosiyaların train, validation və test setlər üzrə paylanması yoxlanılmışdır  
- Mətn uzunluqları analiz edilmişdir  
- Negation strukturlarının (not, didn’t və s.) mövcudluğu müəyyən edilmişdir  

#### 2. Text Preprocessing
- Mətnlərin lowercase formata salınması  
- Rəqəmlərin və punktuasiyanın silinməsi  
- Artıq boşluqların təmizlənməsi  
- Negation-aware preprocessing tətbiqi  

#### 3. Model qurulması və müqayisə
Aşağıdakı modellər qurularaq validation set üzərində müqayisə edilmişdir:
- Logistic Regression  
- Multinomial Naive Bayes  
- Linear Support Vector Machine (SVM)  

Ən yaxşı nəticə Linear SVM modeli ilə əldə edilmişdir.

#### 4. Yekun model və test nəticələri
- Train və validation dataset-ləri birləşdirilərək model yenidən train edilmişdir  
- Test set üzərində yekun qiymətləndirmə aparılmışdır  
- Confusion matrix ilə nəticələr vizual analiz edilmişdir  

#### 5. Inference (Demo)
- Saxlanılmış modeldən istifadə edərək yeni cümlələr üçün sentiment proqnozu həyata keçirilmişdir  

---

### 🌐 Canlı Demo

Model üçün hazırlanmış sadə Gradio interfeysi Hugging Face Spaces üzərindən pulsuz şəkildə deploy edilmişdir. Demo bir müddət istifadə olunmadıqda bir neçə saniyə gec açıla bilər.

Canlı demo linki:  
https://huggingface.co/spaces/bahramzada/ferrum-capital-emotion-demo

---

### 🧠 Qarşılaşılan problemlər və məhdudiyyətlər

- Dataset annotasiyaları subyektiv xarakter daşıyır  
- Emosiyalar arasında semantik overlap mövcuddur (məsələn, anger–sadness–fear)  
- Bəzi cümlələrdə modelin verdiyi nəticə insan intuisiyası ilə tam üst-üstə düşməyə bilər  
- Negation-aware preprocessing tətbiq edilsə də, bu səhvləri tam aradan qaldırmaq mümkün olmamışdır  

Bu davranış modelin deyil, əsasən dataset-in xüsusiyyətləri ilə əlaqədardır.

---

### 🔮 Gələcək işlər (Future Work)
- Transformer əsaslı modellərin (məsələn, BERT) tətbiqi  
- Emotion classification probleminin multi-label yanaşma ilə həlli  
- Dataset balanslaşdırılması və ya data augmentation  

---

## 🇬🇧 English

### 📖 Project Overview

This project was developed as part of the application process for the Artificial Intelligence Internship Program at Ferrum Capital. The goal of the project is to build a sentiment analysis model that classifies user-written sentences into one of six emotion categories.

The dataset includes the following emotions:
- anger  
- fear  
- joy  
- love  
- sadness  
- surprise  

---

### 📂 Project Structure

ferrum-capital-task-1/
├── data/                # Raw and preprocessed datasets
├── models/              # Saved model and TF-IDF vectorizer (.pkl)
├── notebooks/           # EDA, Preprocessing, Modeling, and Inference notebooks
├── app.py               # Simple demo built with Gradio
├── requirements.txt     # Project dependencies
└── README.md

---

### 🔍 Project Workflow

#### 1. Exploratory Data Analysis (EDA)
- Analyzed dataset size and structure  
- Examined emotion class distributions  
- Analyzed text length statistics  
- Identified frequent negation patterns  

#### 2. Text Preprocessing
- Converted text to lowercase  
- Removed numbers and punctuation  
- Removed extra whitespaces  
- Applied negation-aware preprocessing  

#### 3. Model Training and Comparison
The following models were trained and evaluated on the validation set:
- Logistic Regression  
- Multinomial Naive Bayes  
- Linear Support Vector Machine (SVM)  

The Linear SVM model achieved the best overall performance.

#### 4. Final Model and Evaluation
- Train and validation sets were merged for final training  
- Final evaluation was performed on the test set  
- Results were analyzed using a confusion matrix  

#### 5. Inference (Demo)
- The trained model was used to predict emotions for custom input sentences  

---

### 🌐 Live Demo

A simple Gradio-based interface was deployed on Hugging Face Spaces.  
The demo may take a few seconds to load if it has been idle.

Live demo link:  
https://huggingface.co/spaces/bahramzada/ferrum-capital-emotion-demo

---

### 🧠 Challenges and Limitations

- Emotion labels are subjective and sometimes inconsistent  
- Significant semantic overlap exists between emotions (e.g., anger, sadness, fear)  
- Some predictions may differ from human intuition  
- Negation-aware preprocessing improved semantic handling but did not fully eliminate misclassifications  

These issues are mainly related to dataset characteristics rather than model implementation.

---

### 🔮 Future Work
- Apply transformer-based models such as BERT  
- Explore multi-label emotion classification  
- Perform dataset balancing or data augmentation  

---

### ✅ Final Note

This project demonstrates a complete and structured sentiment analysis pipeline, including data analysis, preprocessing, model comparison, evaluation, and inference. The limitations and challenges are openly discussed to ensure transparency and reproducibility.
