import streamlit as st
from pag1 import main as  pag1
from pag2 import main as  pag2




def main():
	

	st.title("Tractor science")
	
	pag_name = ["pag1","pag2"]
	
	OPTIONS = pag_name
	sim_selection = st.selectbox('Cosa vuoi fare?', OPTIONS)

	if sim_selection == pag_name[0]:
		pag1()
	elif sim_selection == pag_name[1]:
		pag2()
	else:
		st.markdown("Something went wrong. We are looking into it.")


if __name__ == '__main__':
	main()