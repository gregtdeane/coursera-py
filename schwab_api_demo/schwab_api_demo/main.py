import requests

appKey = "uc8RM0JmZLDGJXlPBNyGaxyIM4aSNtYA"
appSecret = "SthZ0aKCyunI6pyb"

appMachineName = "prod-gregtd93gmailcom-1a2438ce-58e4-4b22-b314-249e83b1d58a"

# authURL = f"https://api.schwabapi.com/v1/oauth/authorize?response_type=code&client_id=fnB6k1X6JSFlQHravRt6T9m86AZlkD04&scope=readonly&redirect_uri=https://developer.schwab.com/oauth2-redirect.html"

authURL = f"https://api.schwabapi.com/v1/oauth/authorize?response_type=code&client_id={appKey}&scope=readonly&redirect_uri=https://127.0.0.1"

print(f"Click to authenticate: {authURL}")