import cv2
import numpy as np
import streamlit as st

# The stream-lit library is used to set up an interactive web-app!

# Setting the page configuration!
st.set_page_config(page_title = "Fabric Defect Inspector", layout = "wide")

# App header!
st.title("Fabric Defect Inspector")
st.markdown("Upload a photo of your fabric. The algorithm will isolate statistical color anomalies (stains, wrong threads) and mark them out!")

# File up-loader widget!
uploadedFile = st.file_uploader("Upload Fabric Image", type = ["png", "jpg", "jpeg"])

if uploadedFile is not None:
    # Stream-lit files are read as byte-streams, so we convert them into a numpy matrix!
    fileBytes = np.asarray(bytearray(uploadedFile.read()), dtype = np.uint8)
    userInput = cv2.imdecode(fileBytes, 1)

    # Converting B-G-R to R-G-B!
    fabric = cv2.cvtColor(userInput, cv2.COLOR_BGR2RGB)

    # Creating two columns for a side-by-side UI layout!
    columnOne, columnTwo = st.columns(2)

    with columnOne:
        st.subheader("Original Fabric")
        st.image(fabric, width = "stretch")
    
    # Interactive threshold slider!
    st.sidebar.header("Tuning Parameter(s)")
    st.sidebar.markdown("Increase the threshold if defects are being missed. Decrease if normal fabric is being flagged.")
    threshold = st.sidebar.slider("Frequency Threshold", min_value = 1, max_value = 200, value = 51)

    # Displaying a loading spinner while the matrix-calculates!
    with st.spinner("Analysing thread frequencies. . ."):
        pixels = np.reshape(fabric, (-1, 3))
        uniqueColors, counts = np.unique(pixels, axis = 0, return_counts = True)

        minimumCount = counts.min()
        infrequentColors = uniqueColors[counts < (minimumCount + threshold)]

        blobMask = np.zeros(np.shape(fabric)[:2], dtype = bool)
        for color in infrequentColors:
            # Only consider exact matches!
            colorMatch = np.all(fabric == color, axis = -1)
            blobMask = blobMask | colorMatch

        # Creating a copy to preserve the original!
        processedFabric = np.copy(fabric)
        processedFabric[blobMask] = [255, 0, 0]

    with columnTwo:
        st.subheader("Inspection Results")
        st.image(processedFabric, width = "stretch")
        st.success(f"Algorithm finished! Found {len(infrequentColors)} anomaly colors.")
