import streamlit as st
from rdflib import Graph

def execute_sparql_query(rdf_content, query):
    g = Graph()
    g.parse(data=rdf_content, format="xml")

    # Execute the SPARQL query
    results = g.query(query)

    return results

def main():
    st.title("RDF File Uploader & SPARQL Query Executor")

    uploaded_file = st.file_uploader("Upload RDF file", type=["rdf"])

    if uploaded_file is not None:
#        st.success("File uploaded successfully!")

        # Display the contents of the uploaded file
        rdf_content = uploaded_file.read()
#        st.subheader("Uploaded RDF File Contents:")
#        st.code(rdf_content, language="xml")

        # Get the SPARQL query from the user
        query = st.text_area("Enter SPARQL Query")

        # Execute the SPARQL query when the user clicks the button
        if st.button("Run SPARQL Query"):
            if query:
                results = execute_sparql_query(rdf_content, query)

                # Convert query results to a list of tuples for display
                query_results = [row for row in results]

                # Display query results in a table
                st.subheader("Query Results:")
                st.table(query_results)
            else:
                st.warning("Please enter a SPARQL query.")

if __name__ == "__main__":
    main()

