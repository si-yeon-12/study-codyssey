''' 
flask : 앱 프레임워크
request : 클라이언트(웹 브라우저)의 요청 정보를 담고 있는 객체
render_template : HTML 템플릿 파일을 화면에 그려주느느 함수
gTTS : Google Text To Speech 라이브러리
BytesIO : 오디오 데이터를 파일로 저장하지 않고 메모리에서 직접 다루기 위해 사용
base64 : 바이너리 데이터를 텍스트(ASCII) 형태로 변환하기 위해 사용
'''
from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64

# 기본 언어를 한국어로 설정, flask 경로를 __name__이라는 모듈로 설정
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

# '/' 주소에 대한 요청을 처리하는 함수 정의
# 함수가 GET과 POST 두 가지 방식의 요청을 모두 처리
@app.route('/', methods=['GET', 'POST'])
def tts_service():
    """
    메인 페이지를 렌더링하고 TTS 변환 요청을 처리
    - GET 요청: 사용자가 텍스트를 입력하고 언어를 선택할 수 있는 폼 제공
    - POST 요청: 입력된 텍스트와 선택된 언어를 받아 음성으로 변환
                변환된 음성을 재생할 수 있는 페이지를 다시 렌더링
    """
    audio_b64 = None      # 음성 데이터(base64 인코딩)를 저장할 변수
    error_message = None  # 오류 메시지를 저장할 변수
    user_text = ""        # 사용자가 입력한 텍스트를 저장할 변수
    selected_lang = "ko"  # 사용자가 선택한 언어를 저장할 변수 (기본값 'ko')

    # 만약 요청 방식이 'POST'라면 (즉, 사용자가 '음성 듣기' 버튼을 눌렀다면)
    if request.method == 'POST':
        try:
            # HTML 폼(form)에서 'input_text'와 'lang' 이름으로 전송된 데이터 변수에 저장
            user_text = request.form.get('input_text')
            selected_lang = request.form.get('lang')

            # strip()으로 앞뒤 공백을 제거했을 때 내용이 없으면 오류 메시지를 설정
            if not user_text.strip():
                error_message = "음성으로 변환할 텍스트를 입력해주세요."
            else:
                # gTTS 라이브러리를 사용해 텍스트를 음성으로 변환
                tts = gTTS(text=user_text, lang=selected_lang)
                
                # 음성 데이터를 저장할 메모리 버퍼(임시 저장 공간) 생성
                fp = BytesIO()
                # 생성된 음성 데이터를 메모리 버퍼에 덮어쓰기
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