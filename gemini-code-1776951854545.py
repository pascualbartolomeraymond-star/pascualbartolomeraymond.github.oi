import base64

# Function to encode local images to base64 for embedding in HTML
def encode_image(path):
    with open(path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

# Image paths based on uploaded files
img1 = "input_file_0.png" # Church/Floral dress
img2 = "input_file_1.png" # Polaroids/Hug
img3 = "input_file_2.png" # Arena Selfie
img4 = "input_file_3.png" # Arena Blue top
img5 = "input_file_4.png" # Neon lights

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Surprise for Jackie</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --soft-pink: #fce4ec;
            --deep-rose: #f06292;
            --accent-gold: #d4af37;
            --text-color: #4a4a4a;
        }}

        body, html {{
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            background-color: var(--soft-pink);
            color: var(--text-color);
            overflow-x: hidden;
        }}

        /* Password Screen */
        #password-screen {{
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            transition: opacity 0.8s ease;
        }}

        .lock-icon {{
            font-size: 50px;
            margin-bottom: 20px;
        }}

        #password-input {{
            padding: 12px;
            border: 2px solid var(--deep-rose);
            border-radius: 25px;
            text-align: center;
            outline: none;
            font-size: 16px;
            width: 200px;
        }}

        #unlock-btn {{
            margin-top: 15px;
            padding: 10px 30px;
            background: var(--deep-rose);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 600;
        }}

        /* Main Content */
        #main-content {{
            display: none;
            opacity: 0;
            transition: opacity 1.5s ease;
        }}

        header {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(rgba(252, 228, 236, 0.7), rgba(252, 228, 236, 0.7)), url('{img2}');
            background-size: cover;
            background-position: center;
        }}

        h1 {{
            font-family: 'Dancing Script', cursive;
            font-size: 3.5rem;
            color: var(--deep-rose);
            margin-bottom: 10px;
        }}

        .scroll-down {{
            position: absolute;
            bottom: 30px;
            animation: bounce 2s infinite;
            font-size: 24px;
        }}

        @keyframes bounce {{
            0%, 20%, 50%, 80%, 100% {{transform: translateY(0);}}
            40% {{transform: translateY(-10px);}}
            60% {{transform: translateY(-5px);}}
        }}

        /* Story Sections */
        .section {{
            padding: 60px 20px;
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }}

        .photo-card {{
            background: white;
            padding: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-radius: 5px;
            margin-bottom: 30px;
            transform: rotate(-2deg);
            transition: transform 0.3s;
        }}

        .photo-card:nth-child(even) {{
            transform: rotate(2deg);
        }}

        .photo-card img {{
            width: 100%;
            border-radius: 2px;
        }}

        .message-block {{
            font-size: 1.1rem;
            line-height: 1.8;
            margin: 40px 0;
            background: rgba(255,255,255,0.5);
            padding: 25px;
            border-radius: 15px;
            border-left: 5px solid var(--deep-rose);
        }}

        .heart {{
            color: var(--deep-rose);
            font-size: 20px;
        }}

        footer {{
            padding: 50px 20px;
            background: white;
            text-align: center;
            font-family: 'Dancing Script', cursive;
            font-size: 2rem;
            color: var(--deep-rose);
        }}

        .floating-hearts {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
            z-index: -1;
        }}
    </style>
</head>
<body>

    <div id="password-screen">
        <div class="lock-icon">🔒</div>
        <p>Enter the special date to enter</p>
        <input type="text" id="password-input" placeholder="M/DD/YYYY">
        <button id="unlock-btn">Open My Heart</button>
        <p id="error-msg" style="color: red; margin-top: 10px; display: none;">Oops! That's not the date, babe.</p>
    </div>

    <div id="main-content">
        <div class="floating-hearts" id="heart-container"></div>

        <header>
            <h1>Happy Birthday, Jackie!</h1>
            <p>To my one and only, my love.</p>
            <div class="scroll-down">↓</div>
        </header>

        <div class="section">
            <div class="photo-card">
                <img src="{img1}" alt="Jackie at Church">
            </div>
            
            <div class="message-block">
                Happy, happy birthday to my one and only, my love, <strong>Jackie Manzano</strong>. 🎉
                <br><br>
                My wish for you is that all your dreams continue to come true, and that you keep reaching everything your heart desires. 
            </div>

            <div class="photo-card">
                <img src="{img4}" alt="Jackie in Blue">
            </div>

            <div class="message-block">
                I’m always praying for your success and for all the goals you still want to achieve in life. You deserve every good thing coming your way.
                <br><br>
                I hope you never change, especially with how you are with me even if we’re far from each other.
            </div>

            <div class="photo-card">
                <img src="{img3}" alt="Together at the Arena">
            </div>

            <div class="message-block">
                I’m truly happy that I met you, and I hope you feel the same way too. I’m so grateful for you, especially for always understanding me, even during my dramatic moments. 
                <br><br>
                Thank you for your patience and for staying by my side.
            </div>

            <div class="photo-card">
                <img src="{img5}" alt="Together Neon">
            </div>

            <div class="message-block">
                Please continue taking care of your family and never forget your faith, your worship, and your responsibilities. I admire that about you so much.
                <span class="heart">❤</span>
            </div>

            <div class="message-block" style="border-left: none; border-right: 5px solid var(--deep-rose);">
                You already know how much I love you. No matter what happens between us, I’ll always be here for you, supporting you and loving you from where I am.
            </div>
        </div>

        <footer>
            Thank you for being part of my life.<br>
            I love you more, babe. 💖
        </footer>
    </div>

    <script>
        const passInput = document.getElementById('password-input');
        const unlockBtn = document.getElementById('unlock-btn');
        const passScreen = document.getElementById('password-screen');
        const mainContent = document.getElementById('main-content');
        const errorMsg = document.getElementById('error-msg');

        unlockBtn.addEventListener('click', () => {{
            if(passInput.value === '4/19/2026') {{
                passScreen.style.opacity = '0';
                setTimeout(() => {{
                    passScreen.style.display = 'none';
                    mainContent.style.display = 'block';
                    setTimeout(() => {{
                        mainContent.style.opacity = '1';
                    }}, 50);
                }}, 800);
            }} else {{
                errorMsg.style.display = 'block';
            }}
        }});

        // Create floating hearts
        function createHeart() {{
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.style.position = 'absolute';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = '100vh';
            heart.style.opacity = Math.random();
            heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
            heart.innerHTML = '🌸';
            
            document.getElementById('heart-container').appendChild(heart);
            
            let pos = 100;
            const int = setInterval(() => {{
                pos -= 1;
                heart.style.top = pos + 'vh';
                if(pos < -10) {{
                    clearInterval(int);
                    heart.remove();
                }}
            }}, 50);
        }}

        setInterval(createHeart, 1000);
    </script>
</body>
</html>
"""

with open("jackie_birthday_surprise.html", "w", encoding="utf-8") as f:
    f.write(html_content)