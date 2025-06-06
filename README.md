تحلیل رفتار مشتری با یادگیری عمیق روی نظرات فارسی
 
 پروژه چیست؟

این پروژه به کمک یادگیری عمیق و پردازش زبان طبیعی (NLP) به تحلیل و پیش‌بینی رفتار مشتریان فارسی‌زبان بر اساس نظرات متنی آن‌ها می‌پردازد.
دیتاست اول مربوط به سایت اسنپ (شامل برچسب رفتار) برای آموزش (Training) و فاین‌تیون است. سپس از مدل آموزش‌دیده برای پیش‌بینی رفتار کاربران در نظرات بدون برچسب مربوط به سایت دیجی‌کالا استفاده می‌کنیم.

 هدف پروژه

  فاین تیون کردن مدل زبانی فارسی روی دیتاست برچسب‌خورده‌ی اسنپ


   پیش‌بینی رفتار مشتری روی نظرات بدون لیبل دیجی‌کالا


   تحلیل و مصورسازی رفتار کاربران


   ارائه معیارهای ارزیابی: دقت (Accuracy)، خطا، زمان اجرا


ساختار فایل‌ها

    project/
    │
    │
    │
    │── notebooks/
    │   ├── 01_preprocessing.ipynb     
    │   ├── 02_model_training.ipynb     
    │   ├── 03_prediction_visual.ipynb   
    │
    ├── data/
    │   ├── snapp_dataset.csv            
    │   ├── digikala_dataset.csv         
    │
    ├── models/
    │   └── saved_model/                 
    │
    └── README.md                        


تکنولوژی‌ها و ابزارها

    زبان برنامه‌نویسی: Python 3.x

    مدل زبانی: ParsBERT


  کتابخانه‌ها:

        transformers

        datasets

        hazm

        pandas, numpy, matplotlib, seaborn

        scikit-learn

 دیتاست‌ها
 
1. Snapp Dataset (Train + Label)


    فایل: Snappfood - Sentiment Analysis.csv


    ستون‌ها:

        text: متن نظر مشتری

        label: نوع رفتار (مثلاً 0: منفی، 1: خنثی، 2: مثبت)

2. Digikala Dataset (Test + No Label)

    فایل: comment.csv

    ستون‌ها:

        text: متن نظر مشتری

 مراحل اجرای پروژه

  پیش‌پردازش داده‌ها

 نرمال‌سازی و پاک‌سازی متون فارسی با استفاده از hazm

  آموزش مدل (Fine-tune)

  فاین‌تیون ParsBERT با داده‌های برچسب‌خورده اسنپ

  پیش‌بینی و تحلیل

  پیش‌بینی رفتار مشتری دیجی‌کالا و مصورسازی

  ارزیابی و خروجی

   دقت مدل، گزارش طبقه‌بندی، ماتریس سردرگمی

 نحوه اجرا (گام‌به‌گام)

  نصب پکیج‌های موردنیاز:
  
          pip install transformers datasets hazm scikit-learn matplotlib seaborn

 خروجی‌ها

    مدل آموزش‌دیده‌ی ParsBERT ذخیره‌شده

    فایل CSV از پیش‌بینی‌های انجام‌شده روی داده‌های دیجی‌کالا

    نمودار توزیع رفتارها (بارچارت، pie chart)

    ماتریس سردرگمی برای ارزیابی مدل
    نویسنده

   نام:
  
   https://github.com/MRTahasaadat
   
   https://github.com/amirerfann 
   
   https://github.com/shervinnd
  
   ایمیل:
 
   mrtahasaadat@gmail.com

   shervindanesh8282@gmail.com
    

    تاریخ شروع: اردیبهشت 1404
