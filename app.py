import streamlit as st

def main():
    st.title("RDF File Uploader")

    uploaded_file = st.file_uploader("Upload RDF file", type=["rdf"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # You can process the uploaded file here
        # For example, you can read and display the contents of the file
        rdf_content = uploaded_file.read()
        st.write(rdf_content)

if __name__ == "__main__":
    main()

