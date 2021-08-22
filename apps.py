# Importing the necessary libraries
import streamlit as st

# Title of Web App
st.title("Venmurasu Programming Contest")
st.write("""Welcome to our UI. Check out our team members in the Home Page, in the drop-down.""")

# Team Members

team = st.expander("Our Team", False)
team.write("Kavin Aravindhan R (20Z325)")
team.write("Manuvikash S (20Z329)")
team.write("Sharan S S (20Z341)")
team.write("Tharunkumar Dhanasekaran (20Z352)")
team.markdown("----")


st.write("""On the left, you will see three drop down lists and one checkbox. 

The first one is to parallelly view clean Tamil data and corresponding clean English data. To visualise only the cleaned data, ensure the second drop-down option is set to ‘None’.

The second and third drop down list shows the given English texts, and English translations of their corresponding Tamil texts with AI4Bharat and GoogleAPI Models. The BLEU score for each translation is given with each pair of lines, and the average BLEU score per section has also been provided at the top. To only view this, make sure to set all the other dropdown options to 'NONE'.

Final Checkbox displays the Comparison between the two models.""")
st.markdown("----")

# ------------------------------------Adding file name---------------------------------------------------------
files = ["None"]
for i in range(22, 32):
    files.append("File Number " + str(i))


# -------------------------------------Parallel Dataset---------------------------------------------------------
st.sidebar.markdown("View __Parallel Dataset__ after Cleaning and Aligning")
option = st.sidebar.selectbox("Please select the File Name", files)

if option != "None":
    eng_path = open(
        rf"VenmurasuKMST-main\data\{option[-2:]}eng_final.txt", encoding="utf8", mode="rt")
    tam_path = open(
        rf"VenmurasuKMST-main\data\{option[-2:]}tam_final.txt", encoding="utf8", mode="rt")

    eng = eng_path.readlines()
    tam = tam_path.readlines()
    st.subheader(f"Parallel Dataset - File Number {option[-2:]}")
    j = 1
    for i in range(0, len(eng), 2):
        st.markdown(f"__English Line {j}__")
        st.write(eng[i])
        st.markdown(f"__Tamil Line {j}__")
        st.write(tam[i])
        st.markdown("----")
        j += 1
    eng_path.close()
    tam_path.close()

# ---------------------------Translated text and bleu score(AI4 Bharat)-----------------------------------------------
st.sidebar.markdown(
    "View Translated text along with corresponding Bleu score for (__AI4Bharat Model__)")

option1 = st.sidebar.selectbox(
    "Please select the Translated Text(Ai4Bharat)", files)

if option1 != "None":
    eng1_path = open(
        fr"VenmurasuKMST-main\Evaluation\{option1[-2:]}-score.txt", encoding="utf8", mode="rt")

    ls = eng1_path.readlines()
    arr = []
    for i in range(len(ls)):
        if ls[i] == "\n":
            pass
        else:
            arr.append(ls[i])
    k = 0
    l = 0
    st.subheader("Translated Text(AI4Bharat Model)")
    st.subheader(f"File Number: {option1[-2:]}")
    st.subheader(f"Average Bleu Score: {arr[-1][10:]}")
    st.markdown("----")
    for i in range(len(arr)-1):
        if "--->" in arr[i]:
            k += 1
            arr1 = arr[i].split("--->")
            for j in range(len(arr1)):
                if j == 0:
                    st.markdown(f"__English Original Sentence {k}:__")
                    st.write(arr1[j])
                elif j == 1:
                    st.markdown(f"__English Translated Sentence {k}:__")
                    st.write(arr1[j])
        else:
            l += 1
            st.markdown(f"__Bleu Score for Sentence {l} :__")
            st.write(arr[i])
            st.markdown("----")

# ----------------------------------Translated text and bleu score(Google API)------------------------------------------
st.sidebar.markdown(
    "View Translated text along with corresponding Bleu score for (__Google API Model__)")
option2 = st.sidebar.selectbox(
    "Please select the Translated Text(Google API)", files)

if option2 != "None":
    eng2_path = open(
        fr"VenmurasuKMST-main\Google API\Evaluation\{option2[-2:]}-GScore.txt", encoding="utf8", mode="rt")
    lt = eng2_path.readlines()
    arr2 = []
    for i in range(len(lt)):
        if lt[i] == "\n":
            pass
        else:
            arr2.append(lt[i])
    m = 0
    n = 0
    st.subheader("Translated Text(Google API Model)")
    st.subheader(f"File Number: {option2[-2:]}")
    st.subheader(f"Average Bleu Score: {arr2[-1][10:]}")
    st.markdown("----")

    for i in range(len(arr2)-1):
        if "--->" in arr2[i]:
            m += 1
            arr3 = arr2[i].split("--->")
            for j in range(len(arr3)):
                if j == 0:
                    st.markdown(f"__English Original Sentence {m}:__")
                    st.write(arr3[j])
                elif j == 1:
                    st.markdown(f"__English Translated Sentence {m}:__")
                    st.write(arr3[j])
        else:
            n += 1
            st.markdown(f"__Bleu Score for Sentence {n} :__")
            st.write(arr2[i])
            st.markdown("----")

# ------------------------------------Comparison between The Two Models---------------------------------------
st.sidebar.markdown("Comparison between Two Models")
plot = st.sidebar.checkbox(
    "Please select this Checkbox and set all other options to None")

if plot:
    score_path = open(
        fr"VenmurasuKMST-main\Google API\aggScores.txt", encoding="utf8", mode="rt")
    scores = score_path.readlines()
    st.subheader(scores[-3])
    st.subheader("AI4Bharat : " + str(scores[-2][10:]))
    st.subheader("Google API : " + str(scores[-1][9:]))
    st.image("VenmurasuKMST-main\Images\plot.png")
    st.markdown("----")

    for i in range(len(scores)-3):
        if scores[i] != "\n":
            if scores[i][0] == "F":
                st.subheader(scores[i])
            else:
                if scores[i][0] == "A":
                    sk = str(scores[i][10:])
                    st.subheader("AI4Bharat  : "+sk)
                else:
                    sk = str(scores[i][9:])
                    st.subheader("Google API : "+sk)
        else:
            st.markdown("----")
