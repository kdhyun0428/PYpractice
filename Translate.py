# 1. 구글번역 라이브러리를 가져옵니다.
import googletrans

# 2. 번역기 객체를 생성합니다.
translator = googletrans.Translator()

# 3. 번역할 단어를 입력받습니다.
inStr = input("\n번역할 문장을 입력해 주세요.\n")

# 4. 번역될 언어를 선택합니다.
destLang = input("\n원하는는 언어를 입력해 주세요. 영어(en), 일본어(ja), 한국어(ko)\n")

# 5. 라이브러리를 사용하여 번역합니다.
outStr = translator.translate(inStr, dest = destLang)

# 6. 결과를 출력합니다.
print(f"\n{inStr} => {outStr.text}")