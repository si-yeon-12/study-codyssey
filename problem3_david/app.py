from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tts_service():
    audio_b64 = None     
    error_message = None 
    user_text = ""        
    selected_lang = "ko"  

    if request.method == 'POST':
        try:
            user_text = request.form.get('input_text')
            selected_lang = request.form.get('lang')

            if not user_text.strip():
                error_message = "음성으로 변환할 텍스트를 입력해주세요."
            else:
                tts = gTTS(text=user_text, lang=selected_lang)
                
                # 음성 데이터를 저장할 메모리 버퍼(임시 저장 공간) 생성
                fp = BytesIO()
                tts.write_to_fp(fp)
                # 버퍼의 커서(읽기 시작 위치)를 맨 앞으로 이동
                fp.seek(0)
                
                # 메모리 버퍼에 있는 바이너리(0과 1로 된) 음성 데이터를 base64로 인코딩
                # base64는 바이너리 데이터를 decode('utf-8')을 붙여 바이트 문자열을 일반 문자열로 변환해 HTML에 입력
                audio_b64 = base64.b64encode(fp.getvalue()).decode('utf-8')

        except Exception as e:
            error_message = f"음성 변환 중 오류가 발생했습니다: {e}"
            print(f"Error: {e}")

    # render_template 함수를 호출하여 'index.html' 파일을 렌더링(화면에 표시)
    return render_template(
        'index.html', 
        audio=audio_b64,
        error=error_message,
        user_text=user_text,
        selected_lang=selected_lang
    )

if __name__ == '__main__':
    app.run('0.0.0.0', 80)