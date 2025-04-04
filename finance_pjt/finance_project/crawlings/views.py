from django.shortcuts import render
from .utils import get_toss_data
from .models import Comment
import os

def index(request):
    firm = ""
    stock_code = ""
    comments = []

    if request.method == 'POST':
        firm = request.POST.get('firm')

        if firm:
            # 1. 댓글 크롤링 실행 (utils.py에서 파일로 저장함)
            get_toss_data(firm)

            # 2. 저장된 텍스트 파일에서 댓글 읽어서 DB에 저장
            file_path = "comments_temp.txt"  # utils.py에서 이 경로에 저장해야 함

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        content = line.strip()
                        if content:
                            # 중복 저장 방지
                            if not Comment.objects.filter(company_name=firm, content=content).exists():
                                Comment.objects.create(
                                    company_name=firm,
                                    stock_code="N/A",  # 추출 불가능하므로 일단 N/A
                                    content=content
                                )

            # 3. DB에서 해당 기업의 댓글 최신순으로 가져오기
            comments = Comment.objects.filter(company_name=firm).order_by('-created_at')

    context = {
        'firm': firm,
        'stock_code': stock_code,
        'comments': [c.content for c in comments]
    }

    return render(request, "crawlings/stock_finder.html", context)
