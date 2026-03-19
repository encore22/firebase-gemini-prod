# Configuration for Telegram bot

# Telegram Bot Token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Firebase Settings
FIREBASE_SETTINGS = {
    'type': 'service_account',
    'project_id': 'YOUR_PROJECT_ID',
    'private_key_id': 'YOUR_PRIVATE_KEY_ID',
    'private_key': '-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n',
    'client_email': 'YOUR_CLIENT_EMAIL',
    'client_id': 'YOUR_CLIENT_ID',
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_x509_cert_url': 'YOUR_CLIENT_X509_CERT_URL'
}

# Pub/Sub Topics
PUBSUB_TOPICS = {
    'topic_name_1': 'projects/YOUR_PROJECT_ID/topics/YOUR_TOPIC_NAME_1',
    'topic_name_2': 'projects/YOUR_PROJECT_ID/topics/YOUR_TOPIC_NAME_2'
}

# Automation Parameters
AUTOMATION_PARAMS = {
    'param1': 'value1',
    'param2': 'value2'
}