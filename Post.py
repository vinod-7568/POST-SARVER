from flask import Flask, request
import requests
import time
from time import sleep

app = Flask('Jutt')
logo = """


$$$$$$$\  $$$$$$$$\ $$\    $$\ $$$$$$\ $$\       
$$  __$$\ $$  _____|$$ |   $$ |\_$$  _|$$ |      
$$ |  $$ |$$ |      $$ |   $$ |  $$ |  $$ |      
$$ |  $$ |$$$$$\    \$$\  $$  |  $$ |  $$ |      
$$ |  $$ |$$  __|    \$$\$$  /   $$ |  $$ |      
$$ |  $$ |$$ |        \$$$  /    $$ |  $$ |      
$$$$$$$  |$$$$$$$$\    \$  /   $$$$$$\ $$$$$$$$\ 
\_______/ \________|    \_/    \______|\________|
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
                            \033[1;36m[•GAND FAR TOOL•]
                            \x1b[38;5;46m [•TOOL OWNERS•]
                    [•\x1b[38;5;46mABHI - XD x \x1b[38;5;48mABHI - DEVA•]
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆"""

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

def get_random_port():
    return random.randint(5000, 9999)  # You can adjust the port range as needed

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        # Handle the form submission and message sending logic here
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        tee = int(request.form.get('time'))

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
                    time.sleep('tee')
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ABHI-SARVER</title>
    <style>
        /* CSS for styling elements */
        .header {
            display: flex;
            align-items: center;
        }
        .header h1 {
            margin: 0 20px;
        }
        .header img {
            max-width: 250px; /* Adjust as needed */
            margin-right: 20px;
        }
        .random-img {
            max-width: 400px; /* Adjust image size as needed */
            margin: 10px;
        }
        /* Add more CSS styles for other elements as needed */
        /* For example, you can use classes to style form elements and buttons */
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <img src="https://i.ibb.co/vLf3gxw/1689662945266.jpg" alt="Image from Imgur">
        <h1 class="mb-3" style="color: cyan;">9BHII - XD S4RV3R</h1>
        <h1 class="mt-3" style="color: red;"></h1>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken" style="color:red;">𝐄𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐭𝐨𝐤𝐞𝐧 : 💌</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId" style="color: orange;">𝐄𝐧𝐭𝐞𝐫 𝐠𝐫𝐨𝐮𝐩/ 𝐢𝐧𝐛𝐨𝐱 𝐮𝐢𝐝 : 🤠</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx" style="color: green;">𝐄𝐧𝐭𝐞𝐫 𝐡𝐚𝐭𝐞𝐫 𝐧𝐚𝐦𝐞 : ✍🏻</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile" style="color: cyan;">𝐒𝐞𝐥𝐞𝐜𝐭 𝐲𝐨𝐮𝐫 𝐧𝐨𝐭𝐩𝐚𝐝 𝐟𝐢𝐥𝐞 : 📩</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time" style="color: Magenta;">𝐒𝐩𝐞𝐞𝐝 𝐢𝐧 𝐬𝐞𝐜𝐨𝐧𝐝𝐬 : ⏱️</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">𝐒𝐚𝐫𝐯𝐞𝐫 𝐫𝐮𝐧𝐧𝐢𝐧𝐠 ✅</button>
        </form>
    </div>

    <div class="random-images">
        <img src="https://i.ibb.co/vLf3gxw/1689662945266.jpg" alt="Random Image 1" class="random-img">
        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">
        <p>© 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐦𝐚𝐝𝐞 𝐛𝐲 : 𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯 🌿 </p>
        <p style="color: #F535AA;">𝐆𝐫𝐨𝐮𝐩 /𝐢𝐧𝐛𝐨𝐱 𝐥𝐨𝐝𝐞𝐫 𝐬𝐚𝐫𝐯𝐞𝐫 ⚡</p>
        <p>𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 𝐛𝐲: <a href="https://www.facebook.com/100006623113766" style="color: #F535AA;">𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯🏆</a></p>
    </footer>
</body>
</html>

            '''

if __name__ == '__main__':
    app.run(debug=True)
