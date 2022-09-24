import gradio as gr
import matplotlib
matplotlib.use('Agg')
import re
import matplotlib.pyplot as plt

def _count_vocal(s):
    s.lower()
    list_vocal = ['a','i','u','e','o']
    total_char = []
    for vocal in list_vocal:
        total_char.append(s.count(vocal))

    fig = plt.figure()
    plt.bar(list_vocal,total_char)
    plt.title("jumlah huruf vokal")
    plt.xlabel("huruf vocal")
    plt.ylabel("jumlah")
    return fig

def _remove_punct(s):
    fig = _count_vocal(s)
    return re.sub(r"[^\w\d\s]+", "", s), fig

def tampil_text(s):
    return s

gradio_ui = gr.Interface(
    fn=_remove_punct,
    title="Simple Interface",
    inputs=[gr.Textbox(label="input text")],
    outputs=[gr.Textbox(label="output text"),gr.Plot()]
)

gradio_ui.launch()