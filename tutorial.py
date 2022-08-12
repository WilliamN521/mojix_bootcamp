import streamlit as st

st.header("Remove duplicate list items")
st.caption("Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.")
code = '''
mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)
'''
st.code(code, language='python')
st.subheader("Application")
list_input = st.text_input("Enter a List, example: 1,1,2,3,4,4....")
list1 = list_input.split(",")
new_list = set(list1)
st.subheader("Output")
st.write(f"{new_list}")
