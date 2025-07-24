# document_templates.py

def generate_cv(data):
    return f"""
Curriculum Vitae (CV)
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}
Education: {data['education']}
Skills: {data['skills']}
Experience: {data['experience']}
Hobbies: {data['hobbies']}
"""

def generate_leave_application(data):
    return f"""
To: {data['recipient']}
Subject: Leave Application

Dear {data['recipient']},

I, {data['name']}, request leave due to {data['reason']} from {data['dates']}. Kindly approve.

Sincerely,
{data['name']}
"""

def generate_job_application(data):
    return f"""
Job Application

Name: {data['name']}
Position Applied For: {data['position']}
Company: {data['company']}
Qualification: {data['qualification']}
Experience: {data['experience']}

I am interested in the position and look forward to your response.
"""

def generate_further_study_application(data):
    return f"""
Further Study Application

Name: {data['name']}
Institution: {data['institute']}
Field of Study: {data['field']}

I request permission to pursue further studies in the above field.
"""

def generate_character_certificate(data):
    return f"""
Character Certificate

This is to certify that {data['name']} has been associated with {data['institute']} for {data['duration']} and is of good character.
"""

def generate_internship_application(data):
    return f"""
Internship Application

Name: {data['name']}
Institute: {data['institute']}
Company: {data['company']}
Field: {data['field']}

I am interested in applying for the internship position.
"""

def generate_bank_account_application(data):
    return f"""
Bank Account Opening Application

Name: {data['name']}
Bank: {data['bank']}
Account Type: {data['account_type']}

I request to open a bank account of the specified type.
"""

def generate_fee_concession_application(data):
    return f"""
Fee Concession Application

Name: {data['name']}
Reason: {data['reason']}
Class: {data['class']}
Institute: {data['institute']}

Kindly grant fee concession on the above grounds.
"""

def generate_center_change_application(data):
    return f"""
Examination Center Change Application

Name: {data['name']}
Current Center: {data['current_center']}
Requested Center: {data['requested_center']}

Please approve the change of exam center.
"""

def generate_experience_certificate(data):
    return f"""
Experience Certificate

This certifies that {data['name']} worked at {data['organization']} as {data['position']} for {data['duration']}.
"""

def generate_freelance_contract(data):
    return f"""
Freelance Contract Agreement

This agreement is made between {data['freelancer_name']} and {data['client_name']} on {data['deadline']}.
Service Description: {data['services']}
Payment Amount: {data['payment_amount']}
"""

def generate_resignation_letter(data):
    return f"""
Resignation Letter

I, {data['name']}, hereby resign from my position as {data['position']} at {data['company']} due to {data['reason']}.
"""

def generate_rental_agreement(data):
    return f"""
Rental Agreement

Landlord: {data['landlord']}
Tenant: {data['tenant']}
Property: {data['property']}
Rent: {data['rent']}
Duration: {data['duration']}
"""
