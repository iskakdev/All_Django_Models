import os, sys, importlib
from pathlib import Path

BASE = Path(r"C:\Users\Lenovo\PycharmProjects\All_Django_Models\all_projects/all_projects")

print("BASE exists:", BASE.exists())
print("settings exists:", (BASE / "all_projects" / "settings.py").exists())

sys.path.insert(0, str(BASE))
print("sys.path[0]:", sys.path[0])

m = importlib.import_module("all_projects.all_projects.settings")
print("IMPORTED:", m.__file__)

os.environ["DJANGO_SETTINGS_MODULE"] = "all_projects.all_projects.settings"
import django
django.setup()
import streamlit as st
import requests
from all_projects.frontend.student_front import check_student
from all_projects.frontend.titanic_front import check_titanic
from all_projects.frontend.house_front import check_house
from all_projects.frontend.bank_front import check_bank
from all_projects.frontend.diabetes_front import check_diabetes
from all_projects.frontend.avocado_front import check_avocado
from all_projects.frontend.mushroom_front import check_mushroom
from all_projects.frontend.telecom_front import check_telecom
from all_projects.frontend.hre_front import check_hre
from all_projects.frontend.mobile_predict_front import check_mobile_price


with st.sidebar:
    name = st.radio(label='Models: ', options=['Info', 'Student Django', 'Titanic Django', 'House Django', 'Bank Django',
                                               'Diabetes Django', 'Avocado Django', 'Mushroom, Django', 'Telecom Django',
                                               'HR Django', 'Mobile Price Django'])

if name == 'Info':
    st.title('Welcome')
    st.write('- **Student** — предсказание успеваемости студентов')
    st.write('- **Titanic** — предсказание выживаемости на Титанике')
    st.write('- **House** — предсказание стоимости недвижимости')
    st.write('- **Bank** — банковская аналитика')
    st.write('- **Diabetes** — диагностика диабета')
    st.write('- **Avocado** — предсказание цен на авокадо')
    st.write('- **Mushroom** — классификация грибов')
    st.write('- **Telecom** — отток клиентов телекома')
elif name == 'Student Django':
    check_student()
elif name == 'Titanic Django':
    check_titanic()
elif name == 'House Django':
    check_house()
elif name == 'Bank Django':
    check_bank()
elif name == 'Diabetes Django':
    check_diabetes()
elif name == 'Avocado Django':
    check_avocado()
elif name == 'Mushroom Django':
    check_mushroom()
elif name == 'Telecom Django':
    check_telecom()
elif name == 'HR Django':
    check_hre()
elif name == 'Mobile Price Django':
    check_mobile_price()
