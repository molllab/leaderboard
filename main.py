# 사용자한테 텍스트파일 받는다
# 텍스트파일의 내용을 검증한다
# 점수를 업데이트 한다(leaderboard.md)


# leaderboard.md 커밋
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('git commit -m ' + '"업데이트 메시지"')
os.system('git push')