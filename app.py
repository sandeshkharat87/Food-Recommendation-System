import streamlit as st
import pandas as pd
import joblib

model = joblib.load('/content/drive/MyDrive/models/cc_foodrcmdns.pkl')
df = pd.read_csv('dataset/indianfoodMAIN.csv')


recp_name = st.selectbox("Select Recipe", df['recp_name'].values)

st.write(recp_name)
def findRcmdn(value):
    data = []
    index = df[df['recp_name'] == value].index[0]
    distances = sorted(list(enumerate(model[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
    #         print(df.iloc[i[0]].translatedrecipename,df.iloc[i[0]].cuisine)
        print(f"{df.iloc[i[0]]['recp_name']  } , Cuisin : {df.iloc[i[0]].cuisine}")


        allvalues = {  "recp_name":  df.iloc[i[0]]['recp_name'],
                        "cuisine":  df.iloc[i[0]]['cuisine'],
                        "image-url": df.iloc[i[0]]['image-url'],
                        "url": df.iloc[i[0]]["url"],

                       }
        data.append(allvalues)
    return data



def custom_markdown(name, img_url, URL,csn):
    mymark = f"""
    <div class="w3-container w3-red">
    <h1> {name} </h1>
    <h5>Cuisine: {csn}</h5>
    </div>

    <img src={img_url} alt="" style="width:50%">

    <div class="w3-container">
    <p> Recipe Instructions: <a href={URL} target="_blank" >Read...</a> </p>
    </div>

    <div class="w3-container w3-red">

    </div>

    """


    return mymark

if st.button("Show"):
    st.text("Recipe Recommendations....")

    recommendations = findRcmdn(recp_name)


    for result in recommendations:

        st.markdown(custom_markdown(name= result['recp_name'], img_url=result['image-url'], URL=result["url"],csn=result["cuisine"] ), True )
        # st.info(result['recp_name'])
