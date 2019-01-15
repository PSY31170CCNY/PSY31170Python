#Twitter API credentials
import json

# Enter your keys/secrets as strings in the following fields
credentials = {}  
credentials['CONSUMER_KEY'] = 'lO7Nqln9q2im3wiqXTOxi6K0W'  
credentials['CONSUMER_SECRET'] = '176qoo7fc2NB2JPExxFBXIrEG3ZI7Q6Lo1DrUF6FvHK2bNrM0w'
credentials['ACCESS_TOKEN'] = '1084832981095759872-g8m0M2RHp69S53mUm24EQTGRFEkhdO'  
credentials['ACCESS_SECRET'] = 'hcuTNOInFzXAmcKoqY5rh6JMTzpGMKOZKMKmN1TwX8y5E'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)
