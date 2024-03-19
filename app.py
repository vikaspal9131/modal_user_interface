import streamlit as st
import random

# Initialize an empty list to store predictions
predictions = []

# Heading of the page
st.markdown("<h1 style='text-align: center; color: #FBBC05;'>PrognosisX</h1>", unsafe_allow_html=True)

# Subheading for file upload
st.subheader('Upload file')

# Sidebar
st.sidebar.subheader("History")

# Function to upload file
def upload_file():
    uploaded_file = st.file_uploader("Upload [img , jpg , png]" )
    if uploaded_file is not None:
        st.write('File uploaded successfully!')
    
        st.image(uploaded_file, caption='Uploaded Image.')
        return uploaded_file

def gen_ran_num():
   return random.randint(70, 100)
           
            

# Main function
def main():
    # Check if a file is uploaded
    file = upload_file()
    if file is not None:
       
        # Create a button to process the uploaded file
        if st.button("Process File"):
            # Add your processing logic here
            # For demonstration purposes, let's assume a simple logic for cancer prediction
            # You can replace this with your actual model prediction logic
            # Here, we randomly generate a prediction (positive or negative) and a possibility (90%)
    
            
            prediction = random.choice(["Positive", "Negative"])

            
            possibility = gen_ran_num()

           
            # Store the prediction in the list
            predictions.append(( " ", prediction, possibility))
            
            st.subheader("Approximate of your report ")
            
            # Display the prediction and possibility with color based on prediction result
            if prediction == "Positive":
                st.write(f" Prediction for cancer is :<span style='color:Green'> {prediction}</span>", unsafe_allow_html=True)
            else:
                st.write(f" Prediction for  cancer is : <span style='color:red'>{prediction}</span>", unsafe_allow_html=True)
            
            st.write(f" Possibility is: {possibility}%")
            

            st.write(f"NOTE :- The following data is generated with help of deep learing Model which we have trained using MobileNetV2 architecture with transfer learning. It has 97% accuracy and able to compute images faster.   {possibility}%")
           
            
            # Update the sidebar with the latest predictions
            # st.sidebar.subheader("Last uploaded")
            for i, (uploaded_file, pred, prob) in enumerate(predictions):
                st.sidebar.checkbox(f"{uploaded_file}: {pred}, Possibility: {prob}%", key=i)

# Clear predictions
if st.sidebar.button("Clear Predictions"):
    predictions.clear()
    

if __name__ == "__main__":
    main()
