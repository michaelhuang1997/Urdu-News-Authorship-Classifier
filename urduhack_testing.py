import urduhack
import tensorflow

# Downloading models
urduhack.download()

nlp = urduhack.Pipeline()
# with open ("/Users/michaelhuang/Dropbox/Projects/ابنِ صفی/projects in progress/safi's political and social projects/sources/jd_txt/خوفناک جنگل.txt", "r") as file:
#     text= file.read()

text= "ڈاکٹر شوکت اپنی چھوٹی سی خوبصورت کار میں بیٹھ کر شہر کی طرف روانہ ہو گیا۔ وہ سول ہسپتال میں اسسٹنٹ سرجن کی حیثیت سے کام کر رہا تھا۔ دماغ کے آپریشن کا ماہر ہونے کی  حیثیت سے اس کی شہرت دور دور تک تھی۔ حالانکہ ابھی اس کی عمر کچھ ایسی نہ تھی وہ چوبیس پچیس برس کا ایک خوبصورت اور وجیہہ نوجوان تھا۔ اپنی عادات واطوار اور سلیقہ مندی کی بناء پر وہ سوسائٹی میں عزت کی نظروں سے دیکھا جاتا تھا۔ قربانی کا جزبہ تو اس کی فطرت ثانیہ بن گیا تھا۔ آج کا آپریشن وہ کل پر بھی ٹال سکتا تھا لیکن اس کے ضمیرن نے گوارہ نہ کیا۔"

doc = nlp(text)

for sentence in doc.sentences:
    print(sentence.text)
    for word in sentence.words:
        print(f"{word.text}\t{word.pos}")

    for token in sentence.tokens:
        print(f"{token.text}\t{token.ner}")