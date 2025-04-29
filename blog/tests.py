from django.test import TestCase, Client

class TestView(TestCase):
    def setUp(self):
        self.client = Client()


    def test_post_list(self):
        # 1.1 포스트 목록 페이지를 가져온다.
        # 1.2 정상적으로 페이지가 로드된다.
        # 1.3 페이지 타이틀은 'Blog'이다.
        # 1.4 내비게이션 바가 있다.
        # 1.5 Blog, About Me라는 문구가 내비게이션 바에 있다.

        # 2.1 메인 영역에 게시물이 하나도 없다면
        # 2.2 '아직 게시물이 없습니다'라는 문구가 보인다.

        # 3.1 게시물이 2개 있다면
        # 3.2 포스트 목록 페이지를 새로고침했을 때
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다.
        # 3.4 '아직 게시물이 없습니다'라는 문구는 더 이상 보이지 않는다. 