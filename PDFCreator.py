import pandas as pd
import plotly.io as pio
from fpdf import FPDF
from io import BytesIO

def create_pdf_report(dataframes_dict, plotly_figures, pdf_filename):
    class PDF(FPDF):
        #add title and logo
        def header(self):
            self.set_font('helvetica', 'B', 16)
            self.cell(0, 30, 'Population Modelling (Incidence/Prevelence)', 0, 1, 'C')
            #self.image('Images/long_logo.jpg', 10, 8, 33)
            self.ln(1)

        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', 'I', 8)
            self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

        def chapter_title(self, title):
            self.set_font('helvetica', 'B', 12)
            self.cell(0, 8, title, 0, 1, 'L')
            self.ln(1)

        def chapter_body(self, body):
            self.set_font('helvetica', '', 12)
            self.multi_cell(0, 8, body)
            self.ln(1)

        def add_plotly_figure(self, fig):
            img_bytes = pio.to_image(fig, format='png')
            self.image(BytesIO(img_bytes), w=180)

        def add_dataframe(self, df):
            self.set_font('helvetica', '', 8)
            self.ln(8)
            col_width = self.epw / len(df.columns)
            self.set_fill_color(200, 220, 255)
            for col in df.columns:
                self.cell(col_width, 8, str(col), border=1, fill=True)
            self.ln()
            for i in range(len(df)):
                for col in df.columns:
                    self.cell(col_width, 8, str(df[col].iloc[i]), border=1)
                self.ln()
            self.ln()

    pdf = PDF()
    pdf.add_page()

    for i, (df_name, df) in enumerate(dataframes_dict.items()):
        pdf.chapter_title(f'Table {i+1}')
        pdf.chapter_body(f'This table shows the parameters used for {df_name}')
        pdf.add_dataframe(df)

    for i, fig in enumerate(plotly_figures):
        pdf.add_page()
        pdf.chapter_title(f'Figure {i+1}')
        pdf.add_plotly_figure(fig)

    pdf.output(pdf_filename)