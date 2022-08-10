import streamlit as st
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from PIL import Image




st.sidebar.header("Entrez les paramètres de votre maison : ")



def user_input():
    sqft_living=st.sidebar.slider("L'espace de vie intérieur",290,13540,1910)
    grade=st.sidebar.slider('Niveau de qualité de la construction ',1, 13, 7)
    sqft_above=st.sidebar.slider("L'espace intérieur du logement qui est au-dessus du niveau du sol",290,9410,1560)
    sqft_living15=st.sidebar.slider("La superficie de l'espace de vie intérieur du logement pour les 15 voisins les plus proches" ,399,6210, 1490)
    bathrooms=st.sidebar.slider("Nombre de salles de bains, où 0,5 correspond à une chambre avec toilettes mais sans douche",2,8,3)
    view=st.sidebar.slider("Vue, un indice de 0 à 4 de la qualité de la vue de la propriété",0,4,0)
    sqft_basement=st.sidebar.slider("La superficie en pieds carrés de l'espace intérieur du logement qui est sous le niveau du sol",0, 3260, 0)
    bedrooms=st.sidebar.slider("Nombre de chambres",1,11,3)
    lat=st.sidebar.slider('Lattitude',47.1559, 47.7776, 47.1559)
    waterfront=st.sidebar.checkbox("Vue sur la mer : Oui/Non", 0,1)
    house_age=st.sidebar.slider("L'age de la maison",1, 115, 40)
    zipcode_98004=st.sidebar.checkbox('La code postale de la maison est 98004', 0,1)
    zipcode_98039=st.sidebar.checkbox('La code postale de la maison est 98039', 0,1)
    zipcode_98040=st.sidebar.checkbox('La code postale de la maison est 98040', 0,1)
    zipcode = st.sidebar.checkbox("Une autre code postale : ", 0, 1)


    data={'sqft_living':sqft_living,
    'grade':grade,
    'sqft_above':sqft_above,
    'sqft_living15':sqft_living15,
    'bathrooms':bathrooms,
    'view':view,
    'sqft_basement':sqft_basement,
    'bedrooms':bedrooms,
    'lat':lat,
    'waterfront': waterfront,
    'house_age':house_age,
    'zipcode_98004':zipcode_98004,
    'zipcode_98039':zipcode_98039,
    'zipcode_98040':zipcode_98040

    }

    maison_parametres=pd.DataFrame(data,index=[0])
    return maison_parametres

df=user_input()

#st.subheader('On veut calculer le prix pour cette maison')
#st.write(df)
X = pd.read_csv("/home/marina/Desktop/prix_maison/app/df_sans_header.csv")
y = pd.read_csv("/home/marina/Desktop/prix_maison/app/tafget_sans_header.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model1 = make_pipeline(StandardScaler(), Ridge())

model1.fit(X_train, y_train)

prediction = model1.predict(df)
#columns = ['sqft_living', 'grade', 'sqft_above', 'sqft_living15', 'bathrooms',
       #'view', 'sqft_basement', 'bedrooms', 'lat', 'waterfront', 'house_age',
       #'zipcode_98004', 'zipcode_98039', 'zipcode_98040']


#st.info('''
## Le prix de votre maison est:
#''')
prix = round(prediction[0][0],2)
st.write("# Le prix de votre maison est:", prix, "$")

image = Image.open('/home/marina/Desktop/prix_maison/app/maison.jpg')

st.image(image)
st.write("## Bonne chance!") 


