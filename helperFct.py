from tkPDFViewer import tkPDFViewer as pdf


def genimage(frame):
    graph_pdf = pdf.ShowPdf()
    new_frame = graph_pdf.pdf_view(frame, pdf_location=r"current_graph.pdf", bar=False, width=110,
                                   height=33)
    return new_frame
