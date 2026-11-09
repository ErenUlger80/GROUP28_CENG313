# GROUP28_CENG313
CENG313 dersi için hazırladığımız bu projede Kaggle'daki LLM Classification Finetuning yarışmasını seçtik.
Yarışma bağlantısı: https://www.kaggle.com/competitions/llm-classification-finetuning
Grup üyeleri:
Eren Ülger-23118080034
Furkan Demiröz-23118080009

Projenin amacı:
Veride kullanıcı soruları, iki farklı dil modelinin cevapları ve kullanıcı tercihleri bulunmaktadır. Amaç, verilen soru ve cevaplara göre kullanıcının A cevabını mı, B cevabını mı tercih edeceğini veya beraberlik sonucunu tahmin etmektir.

Kullandığımız veri setinin özellikleri:
Eğitim dosyasında 57.477 satır ve 9 sütun bulunmaktadır. Kullanılan temel sütunlar:
- prompt: Kullanıcının soruları.
- response_a ve response_b: İki modelin cevapları.
- winner_model_a, winner_model_b ve winner_tie: Kullanıcı tercihini gösteren etiketler.
Soru ve cevap sütunları JSON biçimindeki metinlerden oluşmaktadır. Bunları Python listelerine dönüştürdük. Hedef sınıfları A kazanır için 0, B kazanır için 1, beraberlik için 2 olarak tanımladık.

Assignment 1: EDA ve başlangıç modeli
Bu bölümde:
- Veri tiplerini, eksik değerleri ve tekrar eden kayıtları kontrol ettik.
- Hedef etiketlerinin ve JSON yapısının geçerliliğini inceledik.
- Sınıf dağılımı, kelime sayıları ve konuşma turu sayıları için grafikler hazırladık.
- Veriyi eğitim ve doğrulama bölümlerine ayırdık.
