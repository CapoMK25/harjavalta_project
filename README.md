# Duunin Vallassa-projekti 2024 ![Harjavalta vaakuna svg](https://github.com/CapoMK25/harjavalta_project/assets/151710380/833ac44a-466d-4ce6-b69a-88bfd5053de7)

The main repository for a future employment-related project dedicated to the betterment of the municipality of Harjavalta. Made with the Django framework, React and HTML/CSS. 

The GitHub pages website can be found here for now: https://capomk25.github.io/harjavalta_project/

Features to be developed in the future: 

- User profiles and resumes (Allow job seekers to create detailed profiles showcasing their skills, experience, and qualifications. Include features for uploading resumes and portfolios. Ensure profiles are searchable and accessible to employers.)

- Job Listings and Matching Algorithms (Create a robust job listing section where employers can post job openings. Implement matching algorithms that connect job seekers with relevant opportunities based on their skills, experience, and preferences.)

- Company Profiles and Culture Insights (Provide detailed company profiles, including information about the company culture, values, and work environment. This helps job seekers make informed decisions about potential employers.)

- Real-Time Communication Tools: (Include messaging or chat features that allow direct communication between job seekers and employers. Real-time communication streamlines the hiring process and facilitates quick and efficient conversations.)

- Employment Resource Center (Create a resource center with articles, guides, and videos on job searching, interview tips, and career development. This can serve as a knowledge hub for job seekers.)

- Community Forums and Support Groups (Establish community forums or support groups where job seekers can connect, share experiences, and offer mutual support. This sense of community can be invaluable during job searches.)

- Employee Referral Programs (Introduce features that allow employees to refer potential candidates to their employers. The more local for the platform, the better.)

- Data Analytics and Reporting: (Implement analytics tools to track platform usage, job placement rates, and other key performance indicators. Use this data to continually optimize and improve the platform.)

- Feedback and Ratings System: (Allow both job seekers and employers to provide feedback and ratings after the hiring process. This builds transparency and trust within the platform.)

- Incentives for Employers: (Provide incentives for companies to participate actively on the platform, such as reduced fees for job postings, access to a larger talent pool, or recognition for companies contributing to local employment.)


```
harjavalta_project
├─ .vscode
│  └─ settings.json
├─ brainstorming_harjavalta.txt
├─ harjavalta_project
│  ├─ db.sqlite3
│  ├─ dist
│  │  └─ main.js
│  ├─ harjavalta
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ babel.config.json
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-312.pyc
│  │  │     └─ __init__.cpython-312.pyc
│  │  ├─ models.py
│  │  ├─ package-lock.json
│  │  ├─ package.json
│  │  ├─ public
│  │  │  ├─ index.html
│  │  │  └─ jobs.html
│  │  ├─ src
│  │  │  ├─ admin
│  │  │  │  ├─ css
│  │  │  │  │  ├─ autocomplete.css
│  │  │  │  │  ├─ base.css
│  │  │  │  │  ├─ changelists.css
│  │  │  │  │  ├─ dark_mode.css
│  │  │  │  │  ├─ dashboard.css
│  │  │  │  │  ├─ forms.css
│  │  │  │  │  ├─ login.css
│  │  │  │  │  ├─ nav_sidebar.css
│  │  │  │  │  ├─ responsive.css
│  │  │  │  │  ├─ responsive_rtl.css
│  │  │  │  │  ├─ rtl.css
│  │  │  │  │  ├─ vendor
│  │  │  │  │  │  └─ select2
│  │  │  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │  │  │     ├─ select2.css
│  │  │  │  │  │     └─ select2.min.css
│  │  │  │  │  └─ widgets.css
│  │  │  │  ├─ img
│  │  │  │  │  ├─ calendar-icons.svg
│  │  │  │  │  ├─ gis
│  │  │  │  │  │  ├─ move_vertex_off.svg
│  │  │  │  │  │  └─ move_vertex_on.svg
│  │  │  │  │  ├─ icon-addlink.svg
│  │  │  │  │  ├─ icon-alert.svg
│  │  │  │  │  ├─ icon-calendar.svg
│  │  │  │  │  ├─ icon-changelink.svg
│  │  │  │  │  ├─ icon-clock.svg
│  │  │  │  │  ├─ icon-deletelink.svg
│  │  │  │  │  ├─ icon-hidelink.svg
│  │  │  │  │  ├─ icon-no.svg
│  │  │  │  │  ├─ icon-unknown-alt.svg
│  │  │  │  │  ├─ icon-unknown.svg
│  │  │  │  │  ├─ icon-viewlink.svg
│  │  │  │  │  ├─ icon-yes.svg
│  │  │  │  │  ├─ inline-delete.svg
│  │  │  │  │  ├─ LICENSE
│  │  │  │  │  ├─ README.txt
│  │  │  │  │  ├─ search.svg
│  │  │  │  │  ├─ selector-icons.svg
│  │  │  │  │  ├─ sorting-icons.svg
│  │  │  │  │  ├─ tooltag-add.svg
│  │  │  │  │  └─ tooltag-arrowright.svg
│  │  │  │  └─ js
│  │  │  │     ├─ actions.js
│  │  │  │     ├─ admin
│  │  │  │     │  ├─ DateTimeShortcuts.js
│  │  │  │     │  └─ RelatedObjectLookups.js
│  │  │  │     ├─ autocomplete.js
│  │  │  │     ├─ calendar.js
│  │  │  │     ├─ cancel.js
│  │  │  │     ├─ change_form.js
│  │  │  │     ├─ collapse.js
│  │  │  │     ├─ core.js
│  │  │  │     ├─ filters.js
│  │  │  │     ├─ inlines.js
│  │  │  │     ├─ jquery.init.js
│  │  │  │     ├─ nav_sidebar.js
│  │  │  │     ├─ popup_response.js
│  │  │  │     ├─ prepopulate.js
│  │  │  │     ├─ prepopulate_init.js
│  │  │  │     ├─ SelectBox.js
│  │  │  │     ├─ SelectFilter2.js
│  │  │  │     ├─ theme.js
│  │  │  │     ├─ urlify.js
│  │  │  │     └─ vendor
│  │  │  │        ├─ jquery
│  │  │  │        │  ├─ jquery.js
│  │  │  │        │  ├─ jquery.min.js
│  │  │  │        │  └─ LICENSE.txt
│  │  │  │        ├─ select2
│  │  │  │        │  ├─ i18n
│  │  │  │        │  │  ├─ af.js
│  │  │  │        │  │  ├─ ar.js
│  │  │  │        │  │  ├─ az.js
│  │  │  │        │  │  ├─ bg.js
│  │  │  │        │  │  ├─ bn.js
│  │  │  │        │  │  ├─ bs.js
│  │  │  │        │  │  ├─ ca.js
│  │  │  │        │  │  ├─ cs.js
│  │  │  │        │  │  ├─ da.js
│  │  │  │        │  │  ├─ de.js
│  │  │  │        │  │  ├─ dsb.js
│  │  │  │        │  │  ├─ el.js
│  │  │  │        │  │  ├─ en.js
│  │  │  │        │  │  ├─ es.js
│  │  │  │        │  │  ├─ et.js
│  │  │  │        │  │  ├─ eu.js
│  │  │  │        │  │  ├─ fa.js
│  │  │  │        │  │  ├─ fi.js
│  │  │  │        │  │  ├─ fr.js
│  │  │  │        │  │  ├─ gl.js
│  │  │  │        │  │  ├─ he.js
│  │  │  │        │  │  ├─ hi.js
│  │  │  │        │  │  ├─ hr.js
│  │  │  │        │  │  ├─ hsb.js
│  │  │  │        │  │  ├─ hu.js
│  │  │  │        │  │  ├─ hy.js
│  │  │  │        │  │  ├─ id.js
│  │  │  │        │  │  ├─ is.js
│  │  │  │        │  │  ├─ it.js
│  │  │  │        │  │  ├─ ja.js
│  │  │  │        │  │  ├─ ka.js
│  │  │  │        │  │  ├─ km.js
│  │  │  │        │  │  ├─ ko.js
│  │  │  │        │  │  ├─ lt.js
│  │  │  │        │  │  ├─ lv.js
│  │  │  │        │  │  ├─ mk.js
│  │  │  │        │  │  ├─ ms.js
│  │  │  │        │  │  ├─ nb.js
│  │  │  │        │  │  ├─ ne.js
│  │  │  │        │  │  ├─ nl.js
│  │  │  │        │  │  ├─ pl.js
│  │  │  │        │  │  ├─ ps.js
│  │  │  │        │  │  ├─ pt-BR.js
│  │  │  │        │  │  ├─ pt.js
│  │  │  │        │  │  ├─ ro.js
│  │  │  │        │  │  ├─ ru.js
│  │  │  │        │  │  ├─ sk.js
│  │  │  │        │  │  ├─ sl.js
│  │  │  │        │  │  ├─ sq.js
│  │  │  │        │  │  ├─ sr-Cyrl.js
│  │  │  │        │  │  ├─ sr.js
│  │  │  │        │  │  ├─ sv.js
│  │  │  │        │  │  ├─ th.js
│  │  │  │        │  │  ├─ tk.js
│  │  │  │        │  │  ├─ tr.js
│  │  │  │        │  │  ├─ uk.js
│  │  │  │        │  │  ├─ vi.js
│  │  │  │        │  │  ├─ zh-CN.js
│  │  │  │        │  │  └─ zh-TW.js
│  │  │  │        │  ├─ LICENSE.md
│  │  │  │        │  ├─ select2.full.js
│  │  │  │        │  └─ select2.full.min.js
│  │  │  │        └─ xregexp
│  │  │  │           ├─ LICENSE.txt
│  │  │  │           ├─ xregexp.js
│  │  │  │           └─ xregexp.min.js
│  │  │  ├─ App.js
│  │  │  ├─ autocomplete.css
│  │  │  ├─ base.css
│  │  │  ├─ bundle.js
│  │  │  ├─ changelists.css
│  │  │  ├─ dark_mode.css
│  │  │  ├─ dashboard.css
│  │  │  ├─ forms.css
│  │  │  ├─ Harjavalta.vaakuna.svg.png
│  │  │  ├─ index.js
│  │  │  ├─ login.css
│  │  │  ├─ main.css
│  │  │  ├─ main.js
│  │  │  ├─ nav_sidebar.css
│  │  │  ├─ redirect.js
│  │  │  ├─ responsive.css
│  │  │  ├─ responsive_rtl.css
│  │  │  ├─ rtl.css
│  │  │  ├─ test.js
│  │  │  ├─ vendor
│  │  │  │  └─ select2
│  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │     ├─ select2.css
│  │  │  │     └─ select2.min.css
│  │  │  └─ widgets.css
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  ├─ webpack.config.js
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ admin.cpython-312.pyc
│  │     ├─ apps.cpython-312.pyc
│  │     ├─ models.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ views.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ harjavalta_project
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ settings.cpython-312.pyc
│  │     ├─ urls.cpython-312.pyc
│  │     ├─ wsgi.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  └─ manage.py
└─ README.md

```