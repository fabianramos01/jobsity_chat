# jobsity_chat
This is a chat-app implemented with Django (chat_app) that uses Django-channels for the communication, 
additional exist a decoupled bot (bot.py) that connect to the app with WebSockets.

The app have the next functionalities:
- Login/logout users
- Register users
- Create rooms
- Connect to a room and receive the messages
- Send messages

The bot have the next functionalities:
- Connect to the 'jobsity' room
- Response the messages that have the command /stock=stock_code, the message is based on the response of 
the API 'https://stooq.com/q/l/?s=stock_code&f=sd2t2ohlcv&h&e=csv'

The bot send error messages in these cases:
- If the stock_code is empty or null the message is 'Error: Ticker missing'
- If the .csv response of the API have the field 'Close' with the value 'N/D' 
the message is 'Error: Wrong stock code'

The error messages and the stock commands are not stored in the database.

Steps to execute the chat-app:

1. Execute 'pip install -r requirements.txt' to install the libraries
2. Create a file named '.env' and write 'CHAT_HOST={HOST}', replace '{HOST}' for the host where
will be running the chat-app. Example: if the app is running locally put '127.0.0.1:{PORT}'. This configuration
is for the connection of the bot.
3. Optional: If you delete the file 'db.sqlite3' you need to execute the next commands:
- python manage.py migrate 
- python manage.py shell
- from apps.chat.models import Room
- from apps.users.models import CustomUser
- bot_user = CustomUser.objects.create_user(username='bot', password='{some_password}')
- Room.objects.create(name='jobsity', owner=bot_user)
4. Execute the command 'python manage.py runserver' to run the app
5. After the app is up, execute this command 'python bot.py' for start the bot
6. Finally, the app is ready to use
