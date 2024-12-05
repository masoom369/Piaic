# Install fpdf library if necessary
!pip install fpdf

# Import required libraries
from fpdf import FPDF
from google.colab import files
from IPython.display import display, Image

# Define user details
name = "masoom" #@param {type:"string"}
email = "masoom@gmail.com" #@param {type:"string"}
phone_number = "1234" #@param {type:"string"}
profile_pic = "/content/logo.png"  #@param {type:"string"}

# Print the details
print("Name:", name)
print("Email:", email)
print("Phone Number:", phone_number)

# Display the image (if exists)
try:
    display(Image(profile_pic))
except FileNotFoundError:
    print("Image not found at the specified path.")

# Create a PDF using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Name: " + name, ln=True, align="L")
pdf.cell(200, 10, txt="Email: " + email, ln=True, align="L")
pdf.cell(200, 10, txt="Phone Number: " + phone_number, ln=True, align="L")

# Add image to the PDF (if found)
try:
    pdf.image(profile_pic, x=10, y=50, w=100)
except FileNotFoundError:
    print("Image not found at the specified path.")

# Save the PDF file
pdf_file = "profile.pdf"
pdf.output(pdf_file)

# Provide a direct download link for the PDF
files.download(pdf_file)

print(f"{pdf_file} is ready for download.")
