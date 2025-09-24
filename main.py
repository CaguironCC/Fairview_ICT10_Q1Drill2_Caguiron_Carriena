from pyscript import document

def generate_message(e):
    # Assign strings to variables
    title = "STUDENT PROFILE INFORMATION 👤"
    separator = "=" * 35
    profile_label = "Personal Details:"
    note_label = "Additional Information:"
    
    # Get input values
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value
    
    # Use multiline string
    prof = f"""{title}
{separator}
{profile_label}
\t• Name: {name}
\t• Age: {age}
\t• School: {school}

{note_label}
{name} is {age} years old and currently studying at {school}. 
This profile was generated using Python\'s string formatting features.
"""
    
    document.getElementById("message").innerText = prof
