import streamlit as st
from rdflib import Graph
import requests
from langchain_core.messages import HumanMessage, SystemMessage 

def read_ontology_graph(rdf_content):
    g = Graph()
    g.parse(data=rdf_content, format="xml")

    # Execute the SPARQL query
#    results = g.query(query)

    return g

def verbalize_ontology(contents):
    url = "http://attempto.ifi.uzh.ch/service/owl_verbalizer/owl_to_ace"
    data = {
        'xml': contents,
        'format': 'ace'
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response_lines = response.text.split('\n')
        return [line for line in response_lines if line.strip() and not line.strip().startswith('/*')]
    return []

def convert_to_langchain_messages(messages):
    return [SystemMessage(content=msg) for msg in messages]

def main():
    st.title("Ontology chatbot")

    rdf_file = st.file_uploader("Upload RDF file", type=["rdf"])
    owl_file = st.file_uploader("Upload OWL 2 XML file", type=["owx"])

    if rdf_file is not None and owl_file is not None:
        rdf_content = rdf_file.read()
        owl_content = owl_file.read()

        ontology = read_ontology_graph(rdf_content)

        axioms = verbalize_ontology(owl_content)
        if axioms is not []:
            with st.expander("Verbalized axioms:"):
                st.code('\n'.join(axioms))

        model_axioms = convert_to_langchain_messages(axioms)

        st.subheader("Ask me questions about the ontology:")
        user_input = st.text_input("You:", key="user_input")
        if user_input:
            user_chat_msg = HumanMessage(content=user_input)
            model_axioms.append(user_chat_msg)
            answer = 'some AI ans'
#            answer = model.invoke(model_axioms)
            
            st.write("Human readable answer:")
            st.code(answer)

#           sparql_ql = other_model.invoke(model_axioms)
            sparql_ql = """
SELECT DISTINCT ?class
WHERE {
  ?s a ?class .
}
            """
            st.write("SPARQL query:")
            st.code(sparql_ql, language='sparql')
            
            model_axioms.pop()
            model_axioms.append(SystemMessage(content=answer))

            if st.button("Run SPARQL Query"):
                if sparql_ql:
                    results = ontology.query(sparql_ql)
                    query_results = [row for row in results]
                    st.subheader("Query Results:")
                    st.table(query_results)
                else:
                    st.warning("Please enter a SPARQL query.")

if __name__ == "__main__":
    main()

