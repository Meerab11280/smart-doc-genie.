def generate_cv(data):
    return f"""
Curriculum Vitae

Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Address: {data['address']}

Education:
{data['education']}

Skills:
{data['skills']}

Experience:
{data['experience']}

Hobbies:
{data['hobbies']}
"""

def generate_leave_application(data):
    return f"""
To,
{data['recipient']}

Subject: Leave Application

Dear Sir/Madam,

I am writing to request leave due to the following reason: {data['reason']}. I would like to take leave from {data['dates']}. I assure you that I will complete all pending tasks before my absence.

Kindly grant me leave for the mentioned period.

Sincerely,
{data['name']}
"""

def generate_job_application(data):
    return f"""
To,
The HR Manager,
{data['company']}

Subject: Job Application for the Position of {data['position']}

Dear Sir/Madam,

I am writing to express my interest in the position of {data['position']} at your esteemed organization. I have a background in {data['qualification']} and possess relevant experience as mentioned below.

Experience:
{data['experience']}

I believe my qualifications make me a suitable candidate for the role. I look forward to the opportunity to discuss how I can contribute to your team.

Sincerely,
{data['name']}
"""

def generate_further_study_application(data):
    return f"""
To,
The Dean,
{data['institute']}

Subject: Request for Further Study Permission

Dear Sir/Madam,

I am {data['name']} and I wish to pursue further studies in the field of {data['field']}. I kindly request your permission to continue my education alongside my current responsibilities.

Thank you for considering my request.

Sincerely,
{data['name']}
"""

def generate_character_certificate(data):
    return f"""
Character Certificate

This is to certify that {data['name']} was a student/employee of {data['institute']} for the duration of {data['duration']}. During this period, their behavior and conduct remained satisfactory and disciplined.

This certificate is issued upon their request for whatever purpose it may serve.

Authorized Signatory
"""

def generate_internship_application(data):
    return f"""
To,
The HR Department,
{data['company']}

Subject: Application for Internship

Dear Sir/Madam,

I am {data['name']}, a student of {data['institute']}, and I am writing to apply for an internship opportunity in the field of {data['field']}. I am keen to gain practical experience and contribute to your organization.

I look forward to your positive response.

Sincerely,
{data['name']}
"""

def generate_bank_account_application(data):
    return f"""
To,
The Branch Manager,
{data['bank']}

Subject: Request for Bank Account Opening

Dear Sir/Madam,

I, {data['name']}, request you to kindly open a {data['account_type']} account in my name at your branch. I am attaching all necessary documents for the process.

Thank you for your assistance.

Sincerely,
{data['name']}
"""

def generate_fee_concession_application(data):
    return f"""
To,
The Principal,
{data['institute']}

Subject: Application for Fee Concession

Respected Sir/Madam,

I am {data['name']} of class {data['class']}. Due to {data['reason']}, I am unable to pay the full fee. I request you to kindly grant me a concession in my fees so I can continue my studies.

Thanking you in anticipation.

Sincerely,
{data['name']}
"""

def generate_center_change_application(data):
    return f"""
To,
The Controller of Examinations

Subject: Request for Change of Examination Center

Respected Sir/Madam,

I am {data['name']} and currently assigned to {data['current_center']}. Due to personal circumstances, I kindly request a change of my examination center to {data['requested_center']}.

I shall be grateful for your consideration.

Sincerely,
{data['name']}
"""

def generate_experience_certificate(data):
    return f"""
Experience Certificate

This is to certify that {data['name']} worked at {data['organization']} as a {data['position']} from {data['duration']}. During their tenure, they displayed dedication and professionalism.

We wish them success in future endeavors.

Authorized Signatory
"""

def generate_freelance_contract(data):
    return f"""
Freelance Work Agreement

This agreement is made between {data['client_name']} (Client) and {data['freelancer_name']} (Freelancer).

Service Description: {data['services']}
Deadline: {data['deadline']}
Payment Amount: {data['payment_amount']}

Both parties agree to the terms stated and will honor the agreement in good faith.

Signed,
{data['client_name']} and {data['freelancer_name']}
"""

def generate_resignation_letter(data):
    return f"""
To,
The Manager,
{data['company']}

Subject: Resignation from the Position of {data['position']}

Dear Sir/Madam,

I am writing to formally resign from my position of {data['position']} at your company. The reason for my resignation is {data['reason']}. Kindly consider this letter as my official notice.

Thank you for the opportunity to work with your team.

Sincerely,
{data['name']}
"""

def generate_rental_agreement(data):
    return f"""
Rental Agreement

This rental agreement is made between {data['landlord']} (Landlord) and {data['tenant']} (Tenant) for the property located at {data['property']}.

Monthly Rent: {data['rent']}
Rental Duration: {data['duration']}

Both parties agree to the terms and conditions of this agreement and sign below as a mark of acceptance.

Signed,
{data['landlord']} and {data['tenant']}
"""
---

