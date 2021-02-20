import smtplib, ssl

############## EMAIL INPUTS ################
sender_email = "sender0@gmail.com"
receiver_email = "receiver@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
############################################

port = 465  # For SSL - Secure Sockets Layer. Could be port 587 / 465
password = input("Type your password and press enter: ")
allowed = False

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:  #using this means the connection is automatically closed after indented block
   
   while allowed == False:
        try:
            server.login("sender@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message)
            allowed = True
            print("Message Sent!")
        except:
            print("Incorrect Password")
            password = input("Type your password and press enter: ")
        
    
    




