import streamlit as st

st.title("Title -> GeeksforGeeks")                  # Title
st.header("Header -> GeeksforGeeks")                # Header
st.subheader("Subheader -> GeeksforGeeks")          # Subheader
st.text("Text -> GeeksforGeeks")                    # Text

st.subheader('Markdown')
st.markdown(' # Hi')                              # Markdown
st.markdown(' ## Hi')
st.markdown(' ### Hi')
st.markdown(' #### Hi')
st.markdown(' ##### Hi')

st.success('Success!')                                            # Success
st.info('Information!')                                           # Information
st.warning('Warning!')                                            # WARNING
st.error('Error!')                                                # Error
st.exception(ZeroDivisionError('Division not possible'))          # Exception
st.help(ZeroDivisionError)                                        # Help used to know what the function do

st.subheader('Write')
st.write("range(1,10)")                                           # Write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.subheader('code')
st.code('x = 10 \n' 'for i in range (x):\n'  '\tprint(i)')        # Code

st.subheader('Checkbox')
st.checkbox('Male')                                               # Checkbox
if(st.checkbox('Adult')):                                         # Checkbox with Validation
    st.write("You'r Adult!")

st.subheader('Radio Buttom')
radioButton = st.radio('Select : ', ('Male','Female','Other'))     # Radio
if(radioButton == "Male"):                                         # Radio with conditions
    st.write("You'r Male")
elif(radioButton == "Female"):
    st.write("You'r Female")
elif(radioButton == "Other"):
    st.write("You'r an Other Gender")

st.subheader('Select Box')                                         # SelectBox
selectbox = st.selectbox("Data Science  : ", ['Data Analysis','Machine Learning ','Web Scraping',
                                'Deep Learning','Natural Language Processing',
                                'Computer Vision ', 'Image Processings'])
st.write("You've selected : " , selectbox)


st.subheader('Multiselectbox')                         # Multiselectbox
multiselectbox = st.multiselect("Data Science  : ", ['Data Analysis','Machine Learning ','Web Scraping',
                                'Deep Learning','Natural Language Processing',
                                'Computer Vision ', 'Image Processings'])
st.write("You've selected : ",len(multiselectbox),'courses')

st.subheader('Button')                                   # Button
if(st.button('Click me')):
    st.write('Thanks For Clicking Me')

st.subheader('Slider')                                  # Slider
vol = st.slider('Select the volume : ', 0,100 , step = 1)
st.write('Volume is : ',vol)

st.subheader('Text Input')                              # Text-Input
username = st.text_input('Username  :' )
password = st.text_input('Password : ', type = 'password')

st.subheader('Text Area')                               # Text-Area
st.text_area('Write somethings intresting about yourself')

st.subheader('Input Number')                               # Input Number
st.number_input("Select your age : " , 18,110)

st.subheader('Input Date')                               # Input Date
st.date_input("Date")

st.subheader('Input Time')                               # Input Time
st.time_input('Time')
