from pyscript import display, document

def collecting_data(event):
    # Get values from form
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    campus = document.getElementById("campus").value

    # Clear previous output first
    output_div = document.getElementById("output")
    output_div.innerText = ""

    # Use escape characters and multiline string
    message = f"""
    ==============================
           Student Profile
    ==============================
    Name   : \"{name}\"
    Age    : {age}\t years old
    Campus : {campus} \\ Campus
    """

    # Display inside output div
    display(message, target="output")