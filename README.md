## Cайт для изучения студентами условных топографических знаков

![Снимок экрана 2024-03-19 150319](https://github.com/Nikkri20/StudySignsProject/assets/114663524/e918c86e-f8f4-4813-b7fe-00a006be71b6)
___
### Backend-разработчик: Крылов Никита Андреевич 🛠️
### Frontend-разработчик: Карболин Сергей Александрович 🖥️
### Дизайнер: Стратюк Лада Александровна 🖌️

___

> [!NOTE]
> Данная документация по проекту была написана Backend-разработчиком (соответственно взгляд на проект может быть не полный). Я попытаюсь описать структуру проекта, описать проблемы и почему были приняты те или иные решения 

### Оглавление 📄
#### Общая информация
* [Для кого это ?](#1)
* [Описание проекта](#2)
* [Стек технологий](#3)
  
#### Как работает проект
* [Структура проекта](#4)

___

<a name="1"></a>

### Для кого это 👥
* Для тех, кто будет продолжать данный проект (eсли кто-то будет)
* Для интересующихся
* Для нас самих же, чтобы не забыть как функционирует проект

<a name="2"></a>

___

### Описание проекта 📝

Web-система с базой данных всего массива условных топографических знаков и их характеристик, дающая возможность тренироваться в чтении условных топографических знаков и позволяющая контролировать полученные знания с помощью теста и экзамена

<a name="3"></a>

___

### Стек технологий 📚
#### Frontend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" width="100" />
</p>

#### Backend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" width="100" />
  <img src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" width="100" />
</p>

#### Дизайн
<img src="https://user-images.githubusercontent.com/25181517/189715289-df3ee512-6eca-463f-a0f4-c10d94a06b2f.png" width="100" />

___

<a name="4"></a>

### Структура проекта 🗂️

> [!WARNING]
> Структура проекта будет со временем меняться, по возможности буду стараться дополнять эту часть

🔴 - не используется

🟢 - используется

>📁 ***app1***

>>📁 ***migrations***

>>>📄 ***__init__.py***

>>📄 ***__init__.py***

>>📄 ***admin.py***

>>📄 ***apps.py***

>>📄 ***forms.py***

>>📄 ***models.py***

>>📄 ***tests.py***

>>📄 ***views.py***

>📁 ***node_modules***

>>📄 ***.package-lock.json***

>📁 ***static***

>>📁 ***css***

>>>📄 ***admin.css***

>>>📄 ***exam-page-style.css***

>>>📄 ***index-style.css***

>>>📄 ***personal-account-page-style.css***

>>>📄 ***registration-login.css***

>>>📄 ***signs-page-style.css***

>>>📄 ***test-page-style.css***

>>📁 ***easytimer.js***

>>>📑 ***...***

>>📁 ***examresults***

>>>📄 ***ведомость.pdf***

>>📁 ***fonts***

>>>📄 ***DejaVuSansCondensed.cw127.pkl***

>>>📄 ***DejaVuSansCondensed.pkl***

>>>📄 ***DejaVuSansCondensed.ttf***

>>📁 ***img***

>>>📑 ***...***

>>📁 ***js***

>>>📄 ***const.js***

>>>📄 ***exam-page.js***

>>>📄 ***index.js***

>>>📄 ***personal-account-page.js***

>>>📄 ***test-page.js***

>📁 ***templates***

>>📁 ***admin***

>>>📄 ***base_site.html***

>>📄 ***base.html***

>>📄 ***exam-page.html***

>>📄 ***index.html***

>>📄 ***login.html***

>>📄 ***personal-account-page.html***

>>📄 ***project-page.html***

>>📄 ***registr.html***

>>📄 ***signs-page.html***

>>📄 ***signs-page.html***

>>📄 ***test-page.html***

>📁 ***Проект_по_созданию_обучающего_сайта_топографических_знаков***

>>📄 ***__init__.py***

>>📄 ***asgi.py***

>>📄 ***settings.py***

>>📄 ***urls.py***

>>📄 ***wsgi.py***

>📄 ***.gitignore***

>📄 ***README.md***

>📄 ***manage.py***

>📄 ***package-lock.json***

>📄 ***package.json***

>📄 ***requirements.txt***



> [!TIP]
> 123

> [!IMPORTANT]
> 123

> [!CAUTION]
> 123
