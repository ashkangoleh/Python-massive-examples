# importing the module
import pywhatkit
 
# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+98********",
                        "*******************",
                        9, 18
                        )
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")