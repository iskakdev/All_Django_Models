import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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


with st.sidebar:
    name = st.radio(label='Models: ', options=['Info', 'Student', 'Titanic', 'House', 'Bank',
                                                'Diabetes', 'Avocado', 'Mushroom', 'Telecom'])

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
elif name == 'Student':
    check_student()
elif name == 'Titanic':
    check_titanic()
elif name == 'House':
    check_house()
elif name == 'Bank':
    check_bank()
elif name == 'Diabetes':
    check_diabetes()
elif name == 'Avocado':
    check_avocado()
elif name == 'Mushroom':
    check_mushroom()
elif name == 'Telecom':
    check_telecom()
