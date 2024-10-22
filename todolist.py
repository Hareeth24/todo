import streamlit as st

# Page title and layout
st.set_page_config(page_title="To-Do List", layout="centered")

# Set color styling
st.markdown("""
    <style>
    .title {
        color: #2E8B57;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .task {
        background-color: #FFFAF0;
        border-radius: 5px;
        padding: 10px;
        margin: 5px 0;
        color: #333;
        font-size: 18px;
        font-weight: bold;
    }
    .add-task-btn {
        background-color: #1E90FF;
        color: white;
        font-size: 18px;
        border-radius: 5px;
    }
    .remove-task-btn {
        background-color: #FF4500;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        margin-left: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<p class="title">My To-Do List</p>', unsafe_allow_html=True)

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Input for new tasks
new_task = st.text_input('Add a new task:')

# Add task to the list
if st.button('Add Task', key='add_task', help="Add new task", use_container_width=True):
    if new_task:
        st.session_state['tasks'].append(new_task)
        new_task = ''  # Clear input after adding

# Display tasks
st.markdown("<h3>Current Tasks</h3>", unsafe_allow_html=True)

for i, task in enumerate(st.session_state['tasks']):
    st.markdown(f'<div class="task">{task}</div>', unsafe_allow_html=True)
    
    # Option to remove tasks
    if st.button('Remove Task', key=f'remove_{i}', help=f"Remove {task}", use_container_width=True):
        st.session_state['tasks'].pop(i)

# Footer
st.markdown("<p style='color: #2E8B57; text-align: center;'>Stay organized with your colorful to-do list!</p>", unsafe_allow_html=True)
