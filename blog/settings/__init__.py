import os
# THIS WILL TRY TO GET THE OS ENV VARIABLE OR SET TO NONE IF IT DOES NOT EXISTS
get_os = os.environ.get("blog", None)
# THIS WILL LOAD THE DEVELOPMENT SETTINGS IF THE VALUE IS NONE
if get_os is None:
  from .dev_settings import * 
# THIS WILL LOAD THE DEVELOPMENT SETTINGS IF THE  BLOG KEY RETURNS A VALUE [(PROD) THAT IN SET ON THE WEB SERVER OS]
elif get_os == "prod":
  from .prod_settings import *

