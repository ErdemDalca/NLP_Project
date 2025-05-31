# 📚 NLP Tabanlı Metin Benzerliği ve Öneri Sistemi Projesi

## Giriş

Bu proje, doğal dil işleme (NLP) teknikleriyle, metinler arası benzerliği ve öneri kalitesini farklı modelleme yaklaşımları ile karşılaştırmalı olarak analiz etmek amacıyla geliştirilmiştir. Oyun tasarım belgeleri (Game Design Document – GDD) ve README dosyalarından toplanan cümleler üzerinde TF-IDF ve Word2Vec tabanlı öneri sistemleri oluşturulmuş, her bir modelin öneri başarısı objektif ve subjektif yöntemlerle değerlendirilmiştir.

- **Proje GitHub Linki:** [https://github.com/ErdemDalca/NLP_Project](https://github.com/ErdemDalca/NLP_Project)

---

## Proje Amacı

- Metin tabanlı öneri sistemlerinde, klasik TF-IDF ile dağıtımsal Word2Vec tabanlı yaklaşımların öneri performanslarını karşılaştırmak
- Model yapılandırmalarının (CBOW/SkipGram, pencere boyutu, vektör boyutu, veri temsili) başarıya etkisini incelemek
- Giriş cümlesine göre en benzer 5 cümleyi sıralayarak hem skor bazlı hem de sezgisel olarak değerlendirmek
- Modeller arası sıralama tutarlılığını Jaccard benzerliği ile analiz etmek

---

## Kullanılan Veri Seti

- **Kaynak:** GitHub’dan toplanan Game Design Document (GDD) ve README dosyaları
- **Açıklama:** Oyun projelerine, mekanik tanımlarına ve oyun içi içeriklere dair binlerce cümle
- **Önişleme Adımları:**
    - İngilizce filtreleme
    - HTML/URL/özel karakter temizliği
    - Cümlelere bölme ve hem lemmatized hem stemmed versiyonlarını üretme
    - Stopwords çıkarma
    - Son format: Her satırda `Book`, `Base Sentence`, `Lemmatized`, `Stemmed` sütunları

---

## Yöntem

### 1. TF-IDF Tabanlı Benzerlik
- Hem lemmatized hem stemmed cümleler için ayrı TF-IDF matrisleri (`TfidfVectorizer`) üretildi.
- Giriş cümlesinin vektörü ile tüm cümlelerin vektörleri arasında **cosine similarity** hesaplandı.
- Skoru en yüksek olan ilk 5 cümle öneri olarak sunuldu.

### 2. Word2Vec Tabanlı Benzerlik
- 16 farklı Word2Vec modeli:  
    - Mimari: CBOW & SkipGram  
    - Window: 4 & 10  
    - Dimension: 300 & 1000  
    - Veri tipi: Lemma & Stem  
- Cümle vektörleri, cümledeki kelimelerin ortalama Word2Vec vektörü ile temsil edildi.
- Giriş cümlesiyle tüm cümleler arasındaki cosine similarity hesaplandı ve en benzer 5 cümle listelendi.

---

## Kullanılan Modeller ve Teknikler

| Model Türü | Mimari     | Window | Dimension |
|------------|------------|--------|-----------|
| Lemma      | CBOW       | 4      | 300       |
| Lemma      | CBOW       | 4      | 1000      |
| Lemma      | CBOW       | 10     | 300       |
| Lemma      | CBOW       | 10     | 1000      |
| Lemma      | SkipGram   | 4      | 300       |
| Lemma      | SkipGram   | 4      | 1000      |
| Lemma      | SkipGram   | 10     | 300       |
| Lemma      | SkipGram   | 10     | 1000      |
| Stem       | CBOW       | 4      | 300       |
| Stem       | CBOW       | 4      | 1000      |
| Stem       | CBOW       | 10     | 300       |
| Stem       | CBOW       | 10     | 1000      |
| Stem       | SkipGram   | 4      | 300       |
| Stem       | SkipGram   | 4      | 1000      |
| Stem       | SkipGram   | 10     | 300       |
| Stem       | SkipGram   | 10     | 1000      |

---

## Sonuçlar ve Değerlendirme

### Her Model İçin İlk 5 Benzer Metin
- Tüm modeller için giriş cümlesine göre önerilen ilk 5 cümle ve cosine similarity skorları çıkarılmıştır.
- Skorların ve önerilerin ortalaması değerlendirilmiştir.
- **Detaylı sonuç dosyaları için:**  
  [manual_scoring_full_input.txt](https://github.com/ErdemDalca/NLP_Project/blob/main/analysis/manual_scoring_full_input.txt)

### Benzerlik Skoru Matrisi (Jaccard)
- Her modelin ilk 5 önerisinin birbiriyle örtüşme oranı Jaccard benzerliği ile hesaplanmıştır.
- En yüksek skorlar, birbirine çok benzer öneriler üreten modelleri gösterir.

### Hangi Model(ler) Daha Başarılı?
- En iyi ortalama skorları, **Word2Vec SkipGram + Stem** kombinasyonlu modeller üretmiştir.
- Özellikle `w2v_stem_skipgram_w10_d1000` modeli (window=10, dimension=1000) hem ortalama benzerlik hem de sezgisel değerlendirmede en başarılı modeldir.
- TF-IDF modelleri, sadece kelime frekansına dayalı olduğu için bağlamsal benzerlikte geride kalmıştır.

### Model Yapılandırmalarının Etkisi
- **SkipGram** mimarisi, CBOW'a göre daha iyi performans göstermiştir.
- **window=10** (geniş bağlam) ve **dimension=1000** (yüksek boyut) ayarları öneri kalitesini artırmıştır.
- **Stemmed veri** ile eğitilen modeller, lemmatized modellere kıyasla daha tutarlı sonuçlar vermiştir.

---

## Genel Çıkarımlar & Öneriler

- **Word2Vec (SkipGram + Stem + window=10, dim=1000)** yapılandırması, metin öneri sistemlerinde en güçlü sonuçları sunmaktadır.
- TF-IDF modelleri hızlı ve anahtar kelime tabanlı aramalar için uygundur; derin anlam ilişkisi gerektiren görevlerde Word2Vec modelleri tercih edilmelidir.
- Model başarısı, sadece algoritmadan değil, önişleme ve model parametrelerinden de büyük ölçüde etkilenmektedir.

---

## Model/Yöntem ve Uygun Olduğu Görevler

| Model / Yöntem            | Uygun Olduğu Görevler                                                    |
|---------------------------|--------------------------------------------------------------------------|
| TF-IDF                    | Yüzeysel benzerlik arama, hızlı indeksleme, anahtar kelime eşleşmeleri   |
| Word2Vec (CBOW)           | Küçük veri setlerinde hızlı ve basit öneri sistemleri                    |
| Word2Vec (SkipGram)       | Anlamsal yakınlık gerektiren öneri sistemleri, arama, diyalog sistemleri |
| SkipGram + Stem + w=10,d=1000 | Detaylı içerik önerileri, bağlam yoğun veri analizi                |

---

## Kullanım ve Kurulum

Öncelikle gerekli Python kütüphanelerini kurun ve ardından tüm adımları sırasıyla uygulayın:

```bash
pip install pandas nltk gensim scikit-learn beautifulsoup4 openpyxl joblib scipy

# Veri önişleme:
python tokenize.py
python lemmatize.py
python stem.py

# Vektörleştirme ve model eğitimi:
python generate_full_tfidf_sparse.py
python train_all_word2vec_models.py

# Top-5 öneri ve analiz:
python get_top5_all_word2vec.py
python get_top5_sparse_lemma.py
python get_top5_sparse_stem.py
