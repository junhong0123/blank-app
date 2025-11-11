import streamlit as st
import clips
import logging

logging.basicConfig(level=15,format='%(messabe)s')

env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

name = st.text_input("Enter your name")

env.builder('(deftemplate result (slot name))')

env.assert_string(f'(result (name "(name)"))')